from django.db import models

class Course(models.Model):
    semester = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    hours_lecture = models.IntegerField(null=True, blank=True)
    hours_tutorial = models.IntegerField(null=True, blank=True)
    hours_lab = models.IntegerField(null=True, blank=True)
    pre_requisite = models.TextField(null=True, blank=True)
    ects_credit = models.CharField(max_length=255,null=True, blank=True)
    total_credits = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255)

    def __str__(self):
        return self.course_code
    
class OldCatalog(Course):
    pass

class NewCatalog(Course):
    pass
    
class Transcript(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    ects_credits = models.CharField(max_length=255, blank=True, null=True)
    grades = models.CharField(max_length=255, blank=True, null=True)
    credits = models.CharField(max_length=255, blank=True, null=True)
    grade_points = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.grades}"
