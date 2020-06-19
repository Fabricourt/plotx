from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from classes.models import Class
from teachers.models import Teacher
from subjects.models import Subject
from students.models import *


class Topic(models.Model):
    teacher = models.ForeignKey(Teacher,  on_delete=models.CASCADE, blank=False, null=True)
    subject = models.ForeignKey(Subject,  on_delete=models.CASCADE, blank=False, null=True)
    title = models.CharField(max_length=200, blank=False, null= True)
    slug = models.SlugField(max_length=200, blank=False, null=True, unique=True)
    overview = RichTextField(blank=True, null=True, help_text='input specific learning outcomes, val-ues, pcl, & core competence')
    date_posted = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Strand'
        verbose_name_plural = 'Strands'
        ordering = ['date_posted']

    def __str__(self):
        return self.title

class Lesson(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,  on_delete=models.CASCADE, blank=False, null=True)
    lesson_title = models.CharField(max_length=100, blank=False, null=True)
    slug = models.SlugField(max_length=250, blank=False, null=True, unique_for_date='date_posted')
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=False)
    content = models.TextField(blank=False, null=True)
    lesson_pic = models.ImageField(upload_to='lesson_pics/%Y/%m/%d/',null=True, blank=True)
    lesson_video_link = models.CharField(max_length=1000, blank=True, null=True)
    lesson_video = models.FileField(upload_to='lesson_videos/', null=True, blank=True)

    date_posted = models.DateTimeField(default=timezone.now)
    
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,  blank=False, null=True)

    is_mvp = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Sub_strand'
        verbose_name_plural = 'Sub_strands'

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.lesson_title



class Lesson_exercise(models.Model):
    ex_class = models.ForeignKey(Class, on_delete=models.CASCADE, blank=False, null=True)
    ex_subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING,  blank=False, null=True)
    ex_topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING,  blank=False, null=True)
    ex_lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING,  blank=False, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True,)
    slug = models.SlugField(max_length=250, blank=False, null=True, unique_for_date='date_posted')

    ex_teacher = models.ForeignKey(User, on_delete=models.DO_NOTHING,  blank=False, null=True, related_name='ex_teacher')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,  blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_mvp = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('exercise-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Exercise_question(models.Model):
    ex_class = models.ForeignKey(Class, on_delete=models.CASCADE, blank=False, null=True)
    exercise = models.ForeignKey(Lesson_exercise, on_delete=models.CASCADE, related_name='exercise')
    diagram = models.ImageField(upload_to='diagrams/%Y/%m/%d/', null=True, blank=True)
    question=models.CharField(max_length=100, null=True, blank=False)
    option1=models.CharField(max_length=100, null=True, blank=False)
    option2=models.CharField(max_length=100, null=True, blank=False)
    option3=models.CharField(max_length=100, null=True, blank=False)
    option4=models.CharField(max_length=100, null=True, blank=False)
    corrans = models.TextField(blank=False, null=True)


    class Meta:
        db_table="lessons"
 
      

    def __str__(self):
        return self.question



