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
from .models import Teacher
from django.contrib.auth.models import User
from classes.models import Class



class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teachers.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'teachers'
    ordering = ['-date_posted']
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        return context


class TeacherDetailView(DetailView):
    model = Teacher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        return context



class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TeacherUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Teacher
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        teacher = self.get_object()
        if self.request.user == teacher.created_by:
            return True
        return False


class TeacherDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Teacher
    success_url = 'teachers'

    def test_func(self):
        teacher = self.get_object()
        if self.request.user == teacher.created_by:
            return True
        return False
