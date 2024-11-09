from django.db import models
from django.contrib.auth.models import User

class Folder(models.Model):
    name = models.CharField(max_length=100,unique=True)
    files = models.ManyToManyField('File', related_name='folders', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subfolders')


    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=100,null=True)
    file = models.FileField(upload_to='uploads/')
    file_size = models.BigIntegerField(default=0)  
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL,null=True, blank=True)  
    category = models.CharField(max_length=10,null=True)
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size 
        super().save(*args, **kwargs)
