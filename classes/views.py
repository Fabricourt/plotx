from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from subjects.models import Subject
from students.models import Student
from lessons.models import *
from notice_board.models import Notice
from exercises.models import Exercise
from  users.models import *
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



class ClassListView(generic.ListView):
    model = Class
    paginate_by = 50
    template_name = 'classes/classes.html'
    context_name = 'classes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        return context



class ClassDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login'
    redirect_field_name = '/accounts/login'
    model = Class


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = Account.objects.all()
        context['notices'] = Notice.objects.all()
        context['subjects'] = Subject.objects.all()
        context['topics'] = Topic.objects.all()
        context['lessons'] = Lesson.objects.all()
        context['students'] = Student.objects.all()
        context['exercises'] = Exercise.objects.order_by("-created_on").filter(is_published=True)[:10]
        return context



class UserClassListView(ListView):
    model = Class
    template_name = 'classes/user_class.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'classes'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')   
  
class Class_nameListView(generic.ListView):
    model = Class_name
    paginate_by = 50
    template_name = 'classes/class_names.html'
    context_name = 'class_names'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_names'] = Class_name.objects.all()
        return context


class Class_nameDetailView(LoginRequiredMixin, generic.DetailView):
    model = Class_name
    template_name = 'classes/class_name.html'
    context_name = 'class_name'


