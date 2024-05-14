"""
URL configuration for AcademEase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ease import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('logout/', views.user_logout, name='logout'),
    path('', views.user_login, name='login'),
    path('home/', views.home, name='home'), 
    path('assign_role/', views.assign_role, name='assign_role'),
    path('supervisor_dashboard/', views.AdminDashboardView, name='supervisor_dashboard'),
    path('teacher_dashboard/', views.TeacherDashboardView, name='teacher_dashboard'),
    path('transcript/', views.StudentTranscriptView, name='transcript'),
    path('course_catalog/', views.Course_catalog, name='course_catalog'),
    path('old_catalog/', views.old_catalog, name='old_catalog'),
    path('new_catalog/', views.new_catalog, name='new_catalog'),

]
