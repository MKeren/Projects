
from django import forms
from .models import File,Folder

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']  

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent_folder']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file', 'folder']


        folder = forms.ModelChoiceField(queryset=Folder.objects.all(), required=False)