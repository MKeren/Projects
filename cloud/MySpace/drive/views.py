from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from drive.forms import FileForm, FileUploadForm, FolderForm
from drive.models import File, Folder
from django.shortcuts import get_object_or_404, redirect


def home(request):
    # Fetch recent files for the last activity table
    recent_files = File.objects.filter(user=request.user).order_by('-last_activity_date')[:10]

    # Calculate storage space used (in MB)
    user_storage_used = sum(file.size for file in recent_files)  # example in MB
    user_total_storage = 10240  # Example: 10 GB in MB
    
    context = {
        'recent_files': recent_files,
        'user_storage_used': user_storage_used,
        'user_total_storage': user_total_storage,
    }

    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

#@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_instance = File(user=request.user, file=uploaded_file)
        file_instance.save()
        return redirect('file_list')
    return render(request, 'upload.html')

#@login_required
def file_list(request):
    files = File.objects.filter(user=request.user)
    return render(request, 'file_list.html',{'files': files})

def manage_storage(request):
    # Get all files for the current user
    user_files = File.objects.filter(user=request.user)

    # Calculate storage usage
    total_storage = 10240  # Example: 10 GB in MB
    used_storage = sum(file.size for file in user_files)  # Sum of file sizes (in MB)

    context = {
        'user_files': user_files,
        'used_storage': used_storage,
        'total_storage': total_storage,
    }
    
    return render(request, 'manage_storage.html', context)

def delete_file(request, file_id):
    file = get_object_or_404(File, id=file_id, user=request.user)
    file.delete()
    return redirect('manage_storage')
