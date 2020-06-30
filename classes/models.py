from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from PIL import Image
from teachers.models import Teacher
from colors.models import *
from users.models import *




# Create your models here.
class Class_name(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Class(models.Model):
    class_name = models.CharField(max_length=100, blank=False, null=True)
    slug = models.SlugField(max_length=250, blank=False, null=True, unique_for_date='date_posted', help_text='You must re enter the class name using dashes e.g class 7 west = class-7-west on the slug field')
    class_teacher =  models.ForeignKey(Teacher, on_delete=models.DO_NOTHING,  blank=True, null=True, related_name='class_teacher')
    class_monitor = models.CharField(max_length=200, blank=True, null=True)
    class_prefect = models.CharField(max_length=200, blank=True, null=True)
    account = models.ManyToManyField(Account, blank=True,  help_text="pick authorized personel to view class")

    about_class = RichTextField(blank=False, null=True)
    class_pic = models.ImageField(upload_to='class_pics/%Y/%m/%d/',null=True, blank=True)
    class_video_link = models.CharField(max_length=1000, blank=True, null=True)
    class_video = models.FileField(upload_to='class_videos/', null=True, blank=True)

    bg_color = models.ForeignKey(Bg_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    bg_color_2 = models.ForeignKey(Bg_color_2, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    bg_color_3 = models.ForeignKey(Bg_color_3, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    hover_color = models.ForeignKey(Hover_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    border_color = models.ForeignKey(Border_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    text_color = models.ForeignKey(Text_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    hover_text_color = models.ForeignKey(Hover_text_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    footer_color = models.ForeignKey(Footer_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')

    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'

    def get_absolute_url(self):
        return reverse('class-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.class_name

