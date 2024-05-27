import io
import PyPDF2
import fitz  # PyMuPDF
import docx
import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ease.forms import TranscriptUploadForm
from ease.models import Course, NewCatalog,OldCatalog, Transcript
from django.contrib.auth.decorators import login_required


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

def user_logout(request):
    logout(request)
    return redirect('login') 

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
    transcripts = Transcript.objects.select_related('courseO', 'courseN').all()
    return render(request, 'course_catalog.html', {'transcripts': transcripts})

@login_required
def old_catalog(request):
    old_courses = OldCatalog.objects.all()

    return render(request, 'old_catalog.html',{'old_courses': old_courses})

@login_required
def new_catalog(request):
    new_courses = NewCatalog.objects.all()

    return render(request, 'new_catalog.html', {'new_courses': new_courses})

def process_pdf_text(file):
   
    data = {
        'Code': [],
        'Title of Course': [],
        'ECTS Credits': [],
        'Grade': [],
        'Credits': [],
        'Gr.Pts': []
    }

    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        text = page.extract_text()
        lines = text.split('\n')
        columns = ['Code', 'Title of Course', 'ECTS Credits', 'Grade', 'Credits', 'Gr.Pts']
        header_found = False

        for line in lines:
            if not header_found:
                # Check if the current line matches the expected columns
                if all(col in line for col in columns):
                    header_found = True
                continue

            if header_found:
                fields = line.split()
                if len(fields) >= 6:
                    data['Code'].append(fields[-5])
                    data['Title of Course'].append(' '.join(fields[1:-4]))
                    data['ECTS Credits'].append(fields[-3])
                    data['Grade'].append(fields[-4])
                    data['Credits'].append(fields[-2])
                    data['Gr.Pts'].append(fields[-1])

    df = pd.DataFrame(data)
    df = clean_data(df)  # Clean the DataFrame
    return df

def process_text_data(text):
    data = {
        'Code': [],
        'Title of Course': [],
        'ECTS Credits': [],
        'Grade': [],
        'Credits': [],
        'Gr.Pts': []
    }
    
    lines = text.split('\n')
    columns = ['Code', 'Title of Course', 'ECTS Credits', 'Grade', 'Credits', 'Gr.Pts']
    header_found = False

    for line in lines:
        if not header_found:
            # Check if the current line matches the expected columns
            if all(col in line for col in columns):
                header_found = True
            continue
        
        if header_found:
            fields = line.split()
            if len(fields) >= 6:
            
                data['Code'].append(fields[-5])
                data['Title of Course'].append(' '.join(fields[1:-4]))
                data['ECTS Credits'].append(fields[-3])
                data['Grade'].append(fields[-4])
                data['Credits'].append(fields[-2])
                data['Gr.Pts'].append(fields[-1])          
    
    df = pd.DataFrame(data)
    df = clean_data(df)  # Clean the DataFrame
    return df

def clean_data(df):
    # Fetch all course codes from the database
    valid_course_codes = set(Course.objects.values_list('course_code', flat=True))
    
    # Keep only rows with valid course codes
    df = df[df['Code'].isin(valid_course_codes)]
    
    # Drop rows with any NaN values
    df = df.dropna()
    
    return df

def process_docx_text(file):
    doc = docx.Document(file)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return process_text_data(text)

def process_txt_text(file):
    text = file.read().decode('utf-8')
    return process_text_data(text)

@login_required
def upload_transcript(request):
    if request.method == 'POST':
        form = TranscriptUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']

            if file.name.endswith('.pdf'):
                df = process_pdf_text(file)
            else:
                df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)

            # Filter the DataFrame based on the course catalog
            course_codes = Course.objects.values_list('course_code', flat=True)
            df = df[df['Code'].isin(course_codes)]

            columns = ['Code', 'Title of Course', 'ECTS Credits', 'Grade', 'Credits', 'Gr.Pts']
            # rearrange the columns of the DataFrame
            df = df.reindex(columns=columns)

            # remove any extra columns
            df = df[columns]

            # Transfer the grade to the course catalog
            for index, row in df.iterrows():
                code = row['Code']
                title = row['Title of Course']
                ects_credits = row['ECTS Credits']
                grades = row['Grade']
                credits = row['Credits']
                grade_points = row['Gr.Pts']

                try:

                    course, created = Course.objects.get_or_create(course_code=code,title=title)
                    print(f"Updating course {course.course_code} with grade {grades}")
                    course.grade = grades
                    course.save()

                    transcript, created = Transcript.objects.update_or_create(code=code)
                    transcript.grades = grades
                    transcript.save()
                
                except Course.DoesNotExist:
                    continue

            return redirect('course_catalog')

    else:
        form = TranscriptUploadForm()
    return render(request, 'upload_transcript.html', {'form': form})