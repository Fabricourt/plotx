from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from classes.models import *
from django.utils import timezone
from django.db import models
from PIL import Image
from django.urls import reverse








class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.CharField(max_length=100, blank=True, null=True)
    id_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f' username--> {self.user.username} ---Fullnames--> {self.user.first_name}-{self.user.last_name} '

    def save(self, **kwargs):
        super().save()
 

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Account(models.Model):
    accountname = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE,)
    fullname = models.CharField(max_length=250, blank=False, null=True)
    slug = models.SlugField(max_length=250, null=True, blank=False)
    user_class = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="created_by",  blank=False, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    is_parent = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.fullname
    
    def get_absolute_url(self):
        return reverse('account-detail',  kwargs={'slug': self.slug})



