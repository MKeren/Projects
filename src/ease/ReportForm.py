from django import forms
from .models import Grade

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

    def graduation_GPA(self):
        total_gpa = 0
        total_credits = 0
        for grade in self.grades.all():
            if grade.is_passed():
                total_gpa += grade.course.gpa * grade.credits_attempted
                total_credits += grade.credits_attempted
        if total_credits == 0:
            return 0
        else:
            return total_gpa / total_credits