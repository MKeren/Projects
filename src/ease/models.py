
from django.db import models
from django.contrib.auth.models import AbstractUser

class Course(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField()
    hours_tutorial = models.IntegerField()
    hours_lab = models.IntegerField()
    pre_requisite = models.TextField()
    ects_credit = models.IntegerField()

    def __str__(self):
        return self.title
    
class CustomUser(AbstractUser):
    ROLES = [
        ("teacher", "Teacher"),
        ("supervisor", "Supervisor"),
    ]
    role = models.CharField(max_length=20, choices=ROLES, default="supervisor")

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

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Transcript(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grades = models.CharField(max_length=10)
    Gr_Pts = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student.name} - {self.course.title}"

class Grade(models.Model):

    grade = models.ForeignKey(Transcript, on_delete=models.CASCADE)
      
    def __str__(self):
        return f"{self.student} - {self.course.title} - {self.grade}"
    
class Role(models.Model):
    NAME_CHOICES = [
        ('supervisor', 'Supervisor'),
        ('teacher', 'Teacher'),
    ]
    name = models.CharField(max_length=10, choices=NAME_CHOICES)

    def __str__(self):
        return self.name