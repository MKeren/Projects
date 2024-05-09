from django import forms
from .models import Course, Grade
from django.contrib.auth.forms import AuthenticationForm

class ReportForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['grade', 'passed_with_d']

    def clean(self):
        cleaned_data = super().clean()
        grade = cleaned_data.get('grade')
        passed_with_d = cleaned_data.get('passed_with_d')
        if grade is not None and not self.instance.is_passed():
            self.add_error('grade', 'This grade is not valid for this student.')
        if passed_with_d is not None and not self.instance.is_passed():
            self.add_error('passed_with_d', 'This student did not pass the course.')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']