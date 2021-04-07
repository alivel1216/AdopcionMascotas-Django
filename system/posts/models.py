"""Posts.models"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete= models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    create=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

