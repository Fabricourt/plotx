from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from colors.models import *
from classes.models import Class
from subjects.models import *
from lessons.models import *



# Create your models here.
class Student(models.Model):
    useraccount = models.ForeignKey(User, on_delete=models.DO_NOTHING,  related_name="studentuseraccount", blank=False, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=250,unique_for_date='date_posted')
    
    age = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    address =  models.CharField(max_length=200, blank=True, null=True)
    
    profile = models.ImageField(default='avatar.jpg', upload_to='profiles/%Y/%m/%d/', blank=True)
    st_video_link = models.CharField(max_length=1000, blank=True, null=True, help_text="student external video link")
    student_video = models.FileField(upload_to='videos/', null=True, blank=True, help_text="student internal video link")
    about_student = models.TextField(max_length=1000, blank=True, null=True, help_text="Enter a brief description of the Realtor.")
    
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)

    classname = models.ForeignKey(Class, on_delete=models.DO_NOTHING,  blank=False, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="createdby",  blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_mvp = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)



    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.first_name