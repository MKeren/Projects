from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Folder(models.Model):
    """Model to represent a folder."""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class File(models.Model):
    """Model to represent a file."""
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="files")
    name = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')  # Adjust the path as necessary
    file_size = models.BigIntegerField(default=0)  # File size in bytes
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class StorageUsage(models.Model):
    """Model to track user storage usage."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    used_space = models.BigIntegerField(default=0)  # in bytes
    total_space = models.BigIntegerField(default=15 * 1024 * 1024 * 1024)  # e.g., 15GB

    def __str__(self):
        return f"{self.user.username}'s storage usage"

    def update_used_space(self):
        """Calculate and update used storage space."""
        files = File.objects.filter(uploaded_by=self.user)
        total_size = sum(f.file.size for f in files)
        self.used_space = total_size
        self.save()
