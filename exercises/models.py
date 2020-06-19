from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from classes.models import Class
from subjects.models import Subject
from lessons.models import *
from teachers.models import Teacher
from students.models import Student

STATUS = ((0, "Draft"), (1, "Publish"))

class Exercise(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True, unique=True)
    slug = models.SlugField(max_length=200, blank=False, null=True, unique=True)
    questions = RichTextField(blank=False, null=True, unique=True)
    file_name = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, null=True,)
    diagram = models.ImageField(upload_to='diagrams/%Y/%m/%d/', null=True, blank=True)
    classname = models.ForeignKey(Class, on_delete=models.CASCADE, blank=False, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING,  blank=False, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING,  blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING,  blank=True, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher_questions")
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    is_published = models.BooleanField(default=True)


    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("exercise", kwargs={"slug": str(self.slug)})



class Answer(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True, related_name="student_answering")
    #slug = models.SlugField(max_length=200, blank=False, null=True, unique=True)
    answers = RichTextField(blank=False, null=True)
    file_name = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, null=True,)
    diagram = models.ImageField(upload_to='diagrams/%Y/%m/%d/', null=True, blank=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="answers")
    #classname = models.ForeignKey(Class, on_delete=models.DO_NOTHING, related_name="ansclass", blank=True, null=True, help_text="Pick your class")
    #subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING,  blank=True, null=True)
    #topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING,  blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]
        
    def __str__(self):
        return "Answer {} by {}".format(self.exercise, self.name)


    def get_absolute_url(self):
        return reverse('answer-detail', kwargs={'pk': self.pk})