from django.shortcuts import render
from .models import *

def exam_room(request):
    results=Exam.objects.all()
    return render(request, 'exam_room/exam_room.html', {"Exam" :results})