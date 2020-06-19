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
from .models import Student
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from classes.models import Class
from exercises.models import *





class StudentListView(ListView):
    model = Student
    template_name = 'students/students.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'students'
    ordering = ['-date_posted']
    paginate_by = 5


class StudentDetailView(DetailView):
    model = Student

 
      
  

#teacher students
class TeacherStudentListView(ListView):
    model = Student
    template_name = 'students/teacher_students.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'students'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Student.objects.filter(created_byr=user).order_by('-date_posted')   

#student
class UserStudentListView(ListView):
    model = Student
    template_name = 'students/teacher_students.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'students'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Student.objects.filter(created_byr=user).order_by('-date_posted')   
  
  

class UserExerciseListView(ListView):

    model = Exercise
    template_name = 'exercises/user_exercises.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'exercises'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.all()
        context['students'] = Student.objects.all()
        context['exercises'] = Exercise.objects.all()
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Exercise.objects.filter(teacher=user).order_by("-created_on") 

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Student
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user == student.created_by:
            return True
        return False


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Student
    success_url = 'students'

    def test_func(self):
        student = self.get_object()
        if self.request.user == student.created_by:
            return True
        return False

