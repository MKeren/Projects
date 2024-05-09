
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class CourseCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    hours_lecture = models.IntegerField()
    hours_tutorial = models.IntegerField()
    hours_lab = models.IntegerField()
    pre_requisite = models.TextField()
    ects_credit = models.IntegerField()

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=255)
    student_no = models.CharField(max_length=20)
    faculty = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    # date_of_registration = models.DateField(default=datetime.now)
    date_of_registration = models.DateField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student} - {self.course.title} - {self.grade}"
    
class Transcript(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.course.title}"