from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from colors.models import *
from ckeditor.fields import RichTextField
from classes.models import Class
from teachers.models import Teacher





# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=250,unique_for_date='date_posted')
    specific_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='eg class 7 or class 7 North')
    bg_color = models.ForeignKey(Bg_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    bg_color_2 = models.ForeignKey(Bg_color_2, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    bg_color_3 = models.ForeignKey(Bg_color_3, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    hover_color = models.ForeignKey(Hover_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    border_color = models.ForeignKey(Border_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    text_color = models.ForeignKey(Text_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    hover_text_color = models.ForeignKey(Hover_text_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    footer_color = models.ForeignKey(Footer_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, blank=False, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Learning_area'
        verbose_name_plural = 'Learning_areas'
        ordering = ['subject_name']
    

    def get_absolute_url(self):
        return reverse('subject-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.subject_name

    
