import io
from django.contrib import messages
import pandas as pd
import csv
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ease.forms import TranscriptUploadForm
from ease.models import Course, NewCatalog,OldCatalog,Student, Transcript
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
        try:
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'This is not a CSV file')
                return redirect('upload_transcript')

            # Decode the file and read into a pandas DataFrame
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            df = pd.read_csv(io_string)

            # Check if necessary columns are in DataFrame
            required_columns = ['Code', 'Grade']
            if not all(column in df.columns for column in required_columns):
                messages.error(request, 'CSV file must contain StudentNo, CourseCode, and Grade columns.')
                return redirect('upload_transcript')

            for index, row in df.iterrows():
                
                code = row['Code']
                grades = row['Grade']

                try:
                    student = Transcript.objects.get(code=code,grades=grades)
                except Course.DoesNotExist:
                    messages.error(request, f'Student with student number {code}does not exist.')
                    continue
                
                try:
                    # Determine which catalog to use based on student data
                    if student.is_old_course:
                        course = OldCatalog.objects.get(code=code)
                    else:
                        course = NewCatalog.objects.get(code=code)
                except (OldCatalog.DoesNotExist, NewCatalog.DoesNotExist):
                    messages.error(request, f'Course with code {code} does not exist in the catalog.')
                    continue

                transcript, created = Transcript.objects.update_or_create(
                    student=student,
                    courseO=course if student.is_old_course else None,
                    courseN=course if not student.is_old_course else None,
                )

            messages.success(request, 'Transcript successfully uploaded')
            return redirect('upload_transcript')
        except Exception as e:
            messages.error(request, f'Error processing file: {e}')
            return redirect('upload_transcript')

    return render(request, 'upload_transcript.html')