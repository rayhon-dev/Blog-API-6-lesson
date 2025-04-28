from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
