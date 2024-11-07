"""
URL configuration for MySpace project.

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
from django.urls import include, path
from drive import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('upload/', views.upload_file, name='upload'),
    path('files/', views.file_list, name='files'),
    path('manage-storage/', views.manage_storage, name='manage_storage'),
    path('delete-file/<int:file_id>/', views.delete_file, name='delete_file'),
]