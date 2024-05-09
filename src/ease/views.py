from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from ease.models import Course, Grade, Student

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


def home(request):
    return render(request, 'home.html')

def course_catalog(request, student_no):
    courses = Course.objects.all()
    student = Student.objects.get(id = student_no)
    grades = Grade.objects.filter(student=student)
    context = {
        'student': student,
        'courses': courses,
        'grades': grades,
    }
    return render(request, 'course_catalog.html', context)

def transcript(request):
    grades = Grade.objects.filter(student=request.user)
    return render(request, 'transcript.html', {'grades': grades})