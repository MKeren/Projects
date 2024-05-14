from django.db import models
from django.contrib.auth.models import AbstractUser

class OldCatalog(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField()
    hours_tutorial = models.IntegerField()
    hours_lab = models.IntegerField()
    pre_requisite = models.TextField()
    ects_credit = models.IntegerField()
    total_credits = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class NewCatalog(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField()
    hours_tutorial = models.IntegerField()
    hours_lab = models.IntegerField()
    pre_requisite = models.TextField()
    ects_credit = models.IntegerField()
    total_credits = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    ROLES = [
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("supervisor", "Supervisor"),
    ]
    custom_role = models.CharField(max_length=20, choices=ROLES, default="student")

    def has_perm(self, perm, obj=None):
        if perm == 'change_role' and self.role == 'supervisor':
            return True
        return super().has_perm(perm, obj)

class Student(models.Model):
    name = models.CharField(max_length=255)
    student_no = models.CharField(max_length=20)
    faculty = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_of_registration = models.DateField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transcript(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    courseO = models.ForeignKey(OldCatalog, on_delete=models.SET_NULL, null=True, blank=True)
    courseN = models.ForeignKey(NewCatalog, on_delete=models.SET_NULL, null=True, blank=True)
    is_old_course = models.BooleanField(default=False)
    grades = models.CharField(max_length=10, blank=True, null=True)
    grade_points = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    def __str__(self):
        if self.is_old_course:
            return f"{self.student.name} - {self.courseO.title}"
        else:
            return f"{self.student.name} - {self.courseN.title}"

class Grade(models.Model):
    transcript = models.ForeignKey(Transcript, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    grade_points = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"{self.transcript.student.name} - {self.transcript.course.title} - {self.grade}"

class Role(models.Model):
    NAME_CHOICES = [
        ('supervisor', 'Supervisor'),
        ('teacher', 'Teacher'),
    ]
    name = models.CharField(max_length=10, choices=NAME_CHOICES)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.name}"