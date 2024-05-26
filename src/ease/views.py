import csv
import io
import os
import PyPDF2
from django.contrib import messages
from docx import Document
import pandas as pd
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import pdfplumber
import tabula
from ease.forms import TranscriptUploadForm
from ease.models import Course, NewCatalog,OldCatalog, Transcript
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login_page.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login_page.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required
def Home(request):
        old_courses = OldCatalog.objects.all()
        new_courses = NewCatalog.objects.all()
        courses = list(old_courses) + list(new_courses)
        return render(request, 'home.html', {'courses': courses})

@login_required
def StudentTranscriptView(request):
    transcripts = Transcript.objects.all()
    
    return render(request, 'transcript.html',{'transcripts': transcripts})

@login_required
def Course_catalog(request):
    transcripts = Transcript.objects.select_related('student', 'courseO', 'courseN').all()
    return render(request, 'course_catalog.html', {'transcripts': transcripts})

@login_required
def old_catalog(request):
    old_courses = OldCatalog.objects.all()

    return render(request, 'old_catalog.html',{'old_courses': old_courses})

@login_required
def new_catalog(request):
    new_courses = NewCatalog.objects.all()

    return render(request, 'new_catalog.html', {'new_courses': new_courses})

@login_required
def process_pdf_text(text):
    
    data = {
        'Code': [],
        'Title of Course': [],
        'ECTS Credits': [],
        'Grade': [],
        'Credits': [],
        'Gr.Pts': []
    }
    
    lines = text.split('\n')
    for line in lines:
        if is_valid_row(line):
            fields = line.split()  # Adjust based on your PDF structure
            data['Code'].append(fields[0])
            data['Title of Course'].append(' '.join(fields[1:-4]))  # Adjust indices as necessary
            data['ECTS Credits'].append(fields[-4])
            data['Grade'].append(fields[-3])
            data['Credits'].append(fields[-2])
            data['Gr.Pts'].append(fields[-1])
    
    df = pd.DataFrame(data)
    df = clean_data(df)  # Clean the DataFrame
    return df

def is_valid_row(line):
    if not line.strip():
        return False
    fields = line.split()
    if len(fields) < 6:  # Adjust based on expected number of fields
        return False
    if not fields[0].isalnum():  # Adjust based on expected course code format
        return False
    return True

def clean_data(df):
    df = df.dropna()  # Drop rows with any NaN values
    df = df[df['Code'].apply(lambda x: x.isalnum())]  

@login_required
def process_word(file):
    doc = Document(file)
    data = []

    for para in doc.paragraphs:
        if para.text.strip():
            data.append(para.text.split())

    # Convertir en DataFrame
    df = pd.DataFrame(data)
    return df

@login_required
def process_text(file):
    data = []
    for line in file:
        if line.strip():
            data.append(line.decode('utf-8').strip().split())

    # Convertir en DataFrame
    df = pd.DataFrame(data)
    return df

@login_required
def transfer_grades(df_transcript, df_course_catalog):
   # Vérifier les duplicatas dans les codes de cours
    if df_course_catalog['code'].duplicated().any():
        df_course_catalog = df_course_catalog.drop_duplicates(subset='code')

    # Associer les notes du fichier de transcription avec le catalogue de cours
    df_course_catalog.set_index('code', inplace=True)
    for index, row in df_transcript.iterrows():
        code = row['Code']
        if code in df_course_catalog.index:
            df_course_catalog.at[code, 'grade'] = row['Grade']
    return df_course_catalog

@login_required
def upload_transcript(request):
    if request.method == 'POST':
        form = TranscriptUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']

            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith('.xlsx') or file.name.endswith('.xls'):
                df = pd.read_excel(file)    
            elif file.name.endswith('.pdf'):
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                df = process_pdf_text(text)  # Custom function to process PDF text into DataFrame
            elif file.name.endswith('.docx') or file.name.endswith('.doc'):
                df = process_word(file)
            elif file.name.endswith('.txt'):
                df = process_text(file)
            else:
                return HttpResponse("Unsupported file format")

            columns = ['Code', 'Title of Course', 'ECTS Credits', 'Grade', 'Credits', 'Gr.Pts']
            # rearrange the columns of the DataFrame
            df = df.reindex(columns=columns)

            # remove any extra columns
            df = df[columns]
        
            for index, row in df.iterrows():
                code = row['Code']
                title = row['Title of Course']
                ects_credits = row['ECTS Credits']
                grades = row['Grade']
                credits = row['Credits']
                grade_points = row['Gr.Pts']

                # Transfer the grade to the course catalog
                course, created = Course.objects.update_or_create(course_code=code, title=title)
                course.grade = grades
                course.save()
                transcript, created = Transcript.objects.update_or_create(code=code,title=title,ects_credits=ects_credits,credits=credits,grade_points=grade_points)
                transcript.grades = grades
                transcript.save()

            return redirect('course_catalog')

    else:
        form = TranscriptUploadForm()
    return render(request, 'upload_transcript.html', {'form': form})