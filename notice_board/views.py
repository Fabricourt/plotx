from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Class
from subjects.models import Subject
from students.models import Student
from lessons.models import *
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



class NoticeListView(generic.ListView):
    model = Class
    paginate_by = 100
    template_name = 'notice_board/notices.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        context['subjects'] = Subject.objects.all()
        context['topics'] = Topic.objects.all()
        context['lessons'] = Lesson.objects.all()
        context['students'] = Student.objects.all()
        return context



   

class NoticeDetailView(generic.DetailView):
    model = Class


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        context['subjects'] = Subject.objects.all()
        context['topics'] = Topic.objects.all()
        context['lessons'] = Lesson.objects.all()
        context['students'] = Student.objects.all()
        return context








