from django.db import models
from django.utils import timezone

# Create your models here.
class Background(models.Model):
    title = models.CharField(max_length=100)
    bgimg = models.ImageField(upload_to='bgimg/', blank=True, null=True)
    bgimg_1 = models.ImageField(upload_to='bgimg/', blank=True, null=True)
    bgimg_2 = models.ImageField(upload_to='bgimg/', blank=True, null=True)
    bgimg_3 = models.ImageField(upload_to='bgimg/', blank=True, null=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title