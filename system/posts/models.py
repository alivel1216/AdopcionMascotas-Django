"""Posts.models"""
from django.db import models

# Create your models here.

class User(models.Model):
    email=models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)