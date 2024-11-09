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


def Home(request):
    # Fetch recent files for the last activity table
    recent_files = File.objects.all().order_by('-last_activity')[:10]

    # Calculate storage space used (in MB) for the files fetched
    total_storage_used = sum(file.file_size for file in recent_files)  # assuming file size is in bytes
    total_storage_limit = 10240 * 1024 * 1024  # Example: 10 GB in bytes
    
    context = {
        'recent_files': recent_files,
        'total_storage_used': total_storage_used / (1024 * 1024),  # Convert bytes to MB
        'total_storage_limit': total_storage_limit / (1024 * 1024),  # Convert bytes to MB
    }
    
    return render(request, 'home.html', context)

@login_required
def home(request):
    recent_files = File.objects.filter(uploaded_by=request.user).order_by('-last_activity')[:10]
    context = {
        'recent_files': recent_files,
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


def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request, 'Folder created successfully!')
            return redirect('files')
    else:
        form = FolderForm()
    return render(request, 'create_folder.html', {'form': form})

@login_required
def Upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.uploaded_by = request.user
            file_instance.save()
            #messages.success(request, 'File uploaded successfully!')
            return redirect('files')
    else:
        form = FileForm()
    return render(request, 'upload.html', {'form': form})


def upload_file(request):
    # Get all folders from the database
    folders = Folder.objects.all()

    # Handle file upload
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the file, and you can also assign the folder here if required
            file = form.save()
            # Redirect to a success page or file list
            return redirect('files')  # Replace with the appropriate redirect URL
    else:
        form = FileUploadForm()

    return render(request, 'upload.html', {'form': form, 'folders': folders})



@login_required
def file_list(request):
    folders = Folder.objects.all()
    files = File.objects.all()

    if request.method == 'POST':
        folder_form = FolderForm(request.POST)
        if folder_form.is_valid():
            folder_form.save()
            return redirect('files') 
    return render(request, 'file_list.html', {
        'folders': folders,
        'files': files,
    })

def folder_contents(request, folder_name):
    folder = Folder.objects.get(name=folder_name)

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the file and associate it with the current folder
            file = form.save(commit=False)
            file.folder = folder
            file.save()
            return redirect('folder_contents', folder_name=folder_name)
    else:
        form = FileUploadForm()

    # Get all files in the folder
    files_in_folder = File.objects.filter(folder=folder)

    return render(request, 'folder_contents.html', {
        'folder': folder,
        'form': form,
        'files_in_folder': files_in_folder
    })
