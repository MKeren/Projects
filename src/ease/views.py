import io
import os
import PyPDF2
from django.contrib import messages
from docx import Document
import pandas as pd
import tabula
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ease.forms import TranscriptUploadForm
from ease.models import Course, NewCatalog,OldCatalog,Student, Transcript
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

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
       
def has_role(user, role):
    return user.role == role

def Home(request):
        old_courses = OldCatalog.objects.all()
        new_courses = NewCatalog.objects.all()
        courses = list(old_courses) + list(new_courses)
        return render(request, 'home.html', {'courses': courses})

@login_required
def TeacherDashboardView(request):
    students = Student.objects.all()
    return render(request,'teacher_template/teacher_dashboard.html', {'students': students})
    
def StudentTranscriptView(request):
    transcripts = Transcript.objects.all()
    
    return render(request, 'transcript.html',{'transcripts': transcripts})

@login_required
def AdminDashboardView(request):
    students = Student.objects.all()
    return render(request,'supervisor_template/supervisor_dashboard.html', {'students': students})

def Course_catalog(request):
    transcripts = Transcript.objects.select_related('student', 'courseO', 'courseN').all()
    return render(request, 'course_catalog.html', {'transcripts': transcripts})

def old_catalog(request):
    old_courses = OldCatalog.objects.all()

    return render(request, 'old_catalog.html',{'old_courses': old_courses})

def new_catalog(request):
    new_courses = NewCatalog.objects.all()

    return render(request, 'new_catalog.html', {'new_courses': new_courses})

#@login_required
def upload_transcript(request):
    if request.method == 'POST':
        form = TranscriptUploadForm(request.POST, request.FILES)
        directory = ''
        if form.is_valid():
            file = form.cleaned_data['file']
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith('.xlsx') or file.name.endswith('.xls'):
                df = pd.read_excel(file)
    
            elif file.name.endswith('.pdf'):
                pdf_file = open(file.name, 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
            elif file.name.endswith('.txt'):
                text_file = open(file.name, 'r')
                text_data = text_file.read()
        
            elif file.name.endswith('.docx'):
                doc = Document(file.name)
                doc_text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
            
            else:
                pass

            for index, row in df.iterrows():
                code = row['Code']
                title = row['Title of Course']
                ects_credits = row['ECTS Credits']
                grades = row['Grade']
                credits = row['Credits']
                grade_points = row['Gr.Pts']

                # Transfer the grade to the course catalog
                course, created = Course.objects.get_or_create(course_code=code, title=title, ects_credit=ects_credits)
                course.grade = grades
                course.save()
                transcript, created = Transcript.objects.get_or_create(code=code,title=title,ects_credits=ects_credits,credits=credits,grade_points=grade_points)
                transcript.grades = grades
                transcript.save()

            return redirect('transcript')

    else:
        form = TranscriptUploadForm()
    return render(request, 'upload_transcript.html', {'form': form})