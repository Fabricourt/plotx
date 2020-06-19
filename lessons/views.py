from django.shortcuts import render
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
from django.contrib.auth.models import User
from exercises.models import *



class LessonListView(ListView):
    model = Lesson
    template_name = 'lessons/lessons.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'lessons'
    ordering = ['-date_posted']
    paginate_by = 5


class LessonDetailView(DetailView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        context['subjects'] = Subject.objects.all()
        context['topics'] = Topic.objects.all()
        context['lessons'] = Lesson.objects.all()
        context['exercises'] = Exercise.objects.filter(status=1).order_by("-created_on")
        context['results'] = Exercise_question.objects.all()
        return context
    


class TeacherLessonListView(ListView):
    model = Lesson
    template_name = 'lessons//teacher_lessons.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'lessons'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(created_by=user).order_by('-date_posted')   
  



class LessonCreateView(LoginRequiredMixin, CreateView):
    model = Lesson
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class LessonUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lesson
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == lesson.created_by:
            return True
        return False


class LessonDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lesson
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == lesson.created_by:
            return True
        return False

class Lesson_exerciseListView(ListView):
    model = Lesson_exercise
    template_name = 'lessons/lesson_exercises.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'lessson_exercises'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        context['subjects'] = Subject.objects.all()
        context['Topics'] = Topic.objects.all()
        context['lessons'] = Lesson.objects.all()
        context['lesson_exercises'] = Lesson_exercise.objects.all()
        context['results'] = Exercise_question.objects.all()
        return context

    


class Lesson_exerciseDetailView(DetailView):
    model = Lesson_exercise

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        context['subjects'] = Subject.objects.all()
        context['Topics'] = Topic.objects.all()
        context['lessons'] = Lesson.objects.all()
        context['lesson_exercises'] = Lesson_exercise.objects.all()
        context['results'] = Exercise_question.objects.all()
        return context
    
 

