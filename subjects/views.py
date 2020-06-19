from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404 
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import *
from lessons.models import *

from django.contrib.auth.models import User

class TopicListView(ListView):
    model = Topic

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lessons'] = Lesson.objects.all()
        context['topics'] = Topic.objects.all()
        return context


class SubjectListView(ListView):
    model = Subject
    template_name = 'Subjects/subjects.html' 
    context_object_name = 'subjects'
    ordering = ['-date_posted']
    paginate_by = 5

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lessons'] = Lesson.objects.all()
        context['topics'] = Topic.objects.all()
        return context


class SubjectDetailView(DetailView):
    model = Subject

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lessons'] = Lesson.objects.all()
        context['topics'] = Topic.objects.all()
        return context


class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')
    
    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
        password=cd['password1'])
        login(self.request, user)
        return result