from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from PIL import Image
from classes.models import Class
from colors.models import *




# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, blank=False, null=True, unique_for_date='date_posted', help_text="repeat the title here replace spaces with dashes e.g. class alert = class-alert")
    notice = RichTextField(blank=False, null=True)
    class_name = models.ManyToManyField(Class, blank=False, help_text='please select all classes you would like this notice to go to')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    
    def get_absolute_url(self):
        return reverse('notice-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title