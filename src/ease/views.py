from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from ease.forms import UserRoleForm
from ease.models import NewCatalog,OldCatalog, CustomUser, Transcript
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login_page.html', {'error': error_message})
    else:
        return render(request, 'login_page.html')
      
def user_logout(request):
        logout(request)
        return HttpResponseRedirect("/")
    
def has_role(user, role):
    return user.role == role

def home(request):
    old_courses = OldCatalog.objects.all()
    new_courses = NewCatalog.objects.all()
    courses = list(old_courses) + list(new_courses)
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
    users = CustomUser.objects.exclude(is_superuser=True)
    return render(request, 'assign_role.html', {'users': users})

def TeacherDashboardView(request):
    return render(request, 'teacher_template/teacher_dashboard.html')

def StudentTranscriptView(request):
    transcripts = Transcript.objects.all()
    
    return render(request, 'transcript.html',{'transcripts': transcripts})

def AdminDashboardView(request):
    return render(request, 'supervisor_template/supervisor_dashboard.html')

def Course_catalog(request):
    return render(request, 'course_catalog.html')

def old_catalog(request):
    old_courses = OldCatalog.objects.all()

    return render(request, 'old_catalog.html',{'old_courses': old_courses})

def new_catalog(request):
    new_courses = NewCatalog.objects.all()

    return render(request, 'new_catalog.html', {'new_courses': new_courses})