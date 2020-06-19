from django.db import models

class Exam(models.Model):
    question=models.CharField(max_length=100, null=True, blank=False)
    option1=models.CharField(max_length=100, null=True, blank=False)
    option2=models.CharField(max_length=100, null=True, blank=False)
    option3=models.CharField(max_length=100, null=True, blank=False)
    option4=models.CharField(max_length=100, null=True, blank=False)
    corrans=models.CharField(max_length=100, null=True, blank=False)

    class Meta:
        db_table="exam_room"