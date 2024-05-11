from django import forms
from django.contrib.auth.models import User

class RoleAssignmentForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
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
