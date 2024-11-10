<<<<<<< HEAD
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

=======
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

>>>>>>> 6617550fcf715d2b591290a52794c37762d08141
        folder = forms.ModelChoiceField(queryset=Folder.objects.all(), required=False)