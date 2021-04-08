"""Users models."""
#Django

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Profile (models.Model):
    """Profile Model."""
    """Proxy model that extends the base data with other information"""
    user =models.OneToOneField(User,on_delete=models.CASCADE)    
    website=models.URLField(max_length=200,blank=True)
    biography=models.TextField(blank=True)
    phone_number=models.CharField(max_length=20,blank=True)
    picture=models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    create=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

class Report (models.Model):
    """Report post model."""
    report = models.CharField(max_length=200, null=False)
    create=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('posts:feed')
    