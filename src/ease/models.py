from django.db import models
from django.contrib.auth.models import AbstractUser

class Course(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField(null=True, blank=True)
    hours_tutorial = models.IntegerField(null=True, blank=True)
    hours_lab = models.IntegerField(null=True, blank=True)
    pre_requisite = models.TextField(null=True, blank=True)
    ects_credit = models.IntegerField(null=True, blank=True)
    total_credits = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=255)
    grade_color = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.course_code
    
class OldCatalog(Course):
    pass

class NewCatalog(Course):
    pass

class CustomUser(AbstractUser):
    
    ROLES = [
        ('teacher', 'Teacher'),
        ('supervisor', 'Supervisor'),
    ]
    roles = models.CharField(max_length=20, choices=ROLES, default='supervisor')

    def __str__(self):
        return self.username
    
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Supervisor(CustomUser):
    pass
    
class Student(models.Model):
    name = models.CharField(max_length=255)
    student_no = models.CharField(max_length=20)
    faculty = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_of_registration = models.DateField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    catalog_type = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.catalog_type}"


class Transcript(models.Model):
    code = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    ects_credits = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    grades = models.CharField(max_length=10, blank=True, null=True)
    credits = models.CharField(max_length=10, blank=True, null=True)
    grade_points = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.grades}"

class Role(models.Model):
    NAME_CHOICES = [
        ('supervisor', 'Supervisor'),
        ('teacher', 'Teacher'),
    ]
    name = models.CharField(max_length=10, choices=NAME_CHOICES)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.name}"
    
