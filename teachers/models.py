from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
  
    def __str__(self):
        return self.name

# Create your models here.
class Teacher(models.Model):
    useraccount = models.ForeignKey(User, on_delete=models.DO_NOTHING,  related_name="teacheruseraccount", blank=False, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    
    slug = models.SlugField(max_length=250,unique_for_date='date_posted')
    title = models.CharField(max_length=100, blank=True, null=True)

    skills = models.ManyToManyField(Skill, blank=True, help_text="add your skills")
    languages = models.ManyToManyField(Language, blank=True, help_text="add your languages")
  
    address =  models.CharField(max_length=200, blank=True, null=True)

    profile = models.ImageField(default='avatar.jpg', upload_to='profiles/%Y/%m/%d/', blank=True)
    st_video_link = models.CharField(max_length=1000, blank=True, null=True, help_text="teacher external video link")
    teacher_video = models.FileField(upload_to='videos/', null=True, blank=True, help_text="teacher internal video link")
    about_teacher = models.TextField(max_length=1000, blank=True, null=True, help_text="Enter a brief description of the Teacher.")

    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    

    def get_absolute_url(self):
        return reverse('teacher-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.first_name