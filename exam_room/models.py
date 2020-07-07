from django.db import models
from subjects.models import *
from teachers.models import *
from students.models import *


MARKED = ((0, "Unmarked"), (1, "Marked"))
STATUS = ((0, "Wrong"), (1, "Correct"))

class ExamPaper(models.Model):
    title = models.CharField(max_length=100, null=True, blank=False)
    slug = models.SlugField(max_length=200, blank=False, null=True, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=False, null=True,)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True,)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=False, null=True,)
    created_on = models.DateTimeField(default=timezone.now)
    marked = models.IntegerField(choices=MARKED, default=0)
    score = models.FloatField(blank=True, null=True,)




class Exam(models.Model):
    question=models.CharField(max_length=100, null=True, blank=False)
    option1=models.CharField(max_length=100, null=True, blank=False)
    option2=models.CharField(max_length=100, null=True, blank=False)
    option3=models.CharField(max_length=100, null=True, blank=False)
    option4=models.CharField(max_length=100, null=True, blank=False)
    corrans=models.CharField(max_length=100, null=True, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        db_table="exam_room"