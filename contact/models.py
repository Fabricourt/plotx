from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from PIL import Image
from django.utils import timezone
from django.contrib.auth.models import User
from catalog.models import Company, Realtor

class Contact(models.Model):
    business = models.CharField(max_length=200)
    business_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    header = models.CharField(max_length=300, blank=True, null=True )
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)  
    user_id = models.IntegerField(blank=True)
    
    def get_absolute_url(self):
        return reverse('plot-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Contactk(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    header = models.CharField(max_length=300, blank=True, null=True )
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)  
    user_id = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name