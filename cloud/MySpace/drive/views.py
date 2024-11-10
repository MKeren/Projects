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

@login_required
def home(request):
    # Get recent files, ordered by last activity date, adjust according to your needs
    recent_files = File.objects.all().order_by('-last_activity')[:5]  # Get the top 5 recent files

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
            return redirect('files')
    else:
        form = FolderForm()
    return render(request, 'create_folder.html', {'form': form})

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        folder_id = request.POST.get('folder')

        if form.is_valid():
            
            file = form.save(commit=False)
            if folder_id:
               
                folder = Folder.objects.get(id=folder_id)
                file.folder = folder
            file.save()
            return redirect('files')  

    else:
        form = FileUploadForm()
        folders = Folder.objects.all()
    
    return render(request, 'upload.html', {'form': form, 'folders': folders})

@login_required
def file_list(request):
    folders = Folder.objects.all()
    folder_id = request.GET.get('folder')

    if folder_id:
        folder = Folder.objects.get(id=folder_id)
        files = folder.files.all() 
    else:
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
