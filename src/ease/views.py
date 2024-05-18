import pandas as pd
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ease.forms import TranscriptUploadForm
from ease.models import NewCatalog,OldCatalog,Student, Transcript
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
        form = TranscriptUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            df = pd.read_excel(file)  # Assuming the file is an Excel file

            for index, row in df.iterrows():
                student_no = row['student_no']
                course_code = row['course_code']
                grade = row['grade']
                grade_points = row['grade_points']
                is_old_course = row.get('is_old_course', False)  # This column should be present in the file

                student = Student.objects.get(student_no=student_no)
                if is_old_course:
                    course = OldCatalog.objects.get(course_code=course_code)
                    transcript, created = Transcript.objects.get_or_create(student=student, course_old=course, is_old_course=True)
                else:
                    course = NewCatalog.objects.get(course_code=course_code)
                    transcript, created = Transcript.objects.get_or_create(student=student, course_new=course, is_old_course=False)

                transcript.grade = grade
                transcript.grade_points = grade_points
                transcript.save()

            return redirect('transcript')

    else:
        form = TranscriptUploadForm()
    return render(request, 'upload_transcript.html', {'form': form})