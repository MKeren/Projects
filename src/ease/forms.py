from django import forms
from django.contrib.auth.models import User
from ease.models import CustomUser, Student, Transcript

from ease.models import NewCatalog, OldCatalog

class RoleAssignmentForm(forms.Form):
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    role = forms.ChoiceField(choices=[('teacher', 'Teacher'), ('supervisor', 'Supervisor')])

    def __init__(self, *args, **kwargs):
        self.supervisor = kwargs.pop('supervisor', False)
        super(RoleAssignmentForm, self).__init__(*args, **kwargs)

        if self.supervisor:
            self.fields['user'].queryset = User.objects.filter(role__in=['teacher', 'supervisor'])

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        role = cleaned_data.get('role')


    if role == 'supervisor':
        user.role = role
        user.save()


class StudentLookupForm(forms.Form):
    student_no = forms.CharField(max_length=20, label="Student Number")

class TranscriptUploadForm(forms.Form):
    file = forms.FileField()


                