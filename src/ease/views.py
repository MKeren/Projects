from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course, Grade

class CourseListView(ListView):
    model = Course
    template_name = 'course_catalog.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.object
        grades = Grade.objects.filter(course=course)
        context['grades'] = grades
        return context