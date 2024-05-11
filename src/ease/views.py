from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from ease.forms import UserRoleForm
from ease.models import Course, Grade, Student, CustomUser, Role
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import TemplateView

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
    
def has_role(user, role):
    return user.role == role

def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def assign_role(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        role = request.POST.get('role')
        user = CustomUser.objects.get(id=user_id)
        user.role = role
        user.save()
        return redirect('home')
    users = CustomUser.objects.filter(role='teacher')
    return render(request, 'assign_role.html', {'users': users})

def TeacherDashboardView(request):
    return render(request, 'teacher_template/teacher_dashboard.html')

def StudentTranscriptView(request):
    return render(request, 'transcript.html')

def AdminDashboardView(request):
    return render(request, 'supervisor_template/supervisor_dashboard.html')

def Course_catalog(request):
    return render(request, 'course_catalog.html')