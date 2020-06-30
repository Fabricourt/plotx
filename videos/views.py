from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
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
# Create your views here.

class videoListView(ListView):
    model= Video
    ordering = ['-date_posted']
    paginate_by = 12

class videoDetailView(DetailView):
    model = Video


class UservideoListView(ListView):
    model = Video
    template_name = 'user/user_videos.html' 
    context_object_name = 'user-videos'
    paginate_by = 5

class videoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class videoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.created_by:
            return True
        return False

class videoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    success_url = '/'

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.created_by:
            return True
        return False

