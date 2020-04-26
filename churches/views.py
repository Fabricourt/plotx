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
from .models import Church, Weekly_theme, Theme_of_the_year, Schedule, Announcement, Hymn, Hymn_of_the_week, Video, Photo, Sermon
from towns.models import Town
from django.contrib.auth.models import User


class ChurchListView(ListView):
    model= Church
    ordering = ['-date_posted']
    paginate_by = 12

class ChurchDetailView(DetailView, LoginRequiredMixin,
PermissionRequiredMixin):
    model = Church
    permission_required = 'churches.view_church'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Towns
        context['weekly_themes'] = Weekly_theme.objects.all()[:1]
        return context

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Towns
        context['theme_of_the years'] = Theme_of_the_year.objects.all()[:1]
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedules'] = Schedule.objects.all()[:1]
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcement'] = Announcement.objects.all()[:1]
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo'] = Photo.objects.all()[:1]
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video'] = Video.objects.all()[:1]
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hymn_of_the_week'] = Hymn_of_the_week.objects.all()[:1]
        return context


class UserChurchListView(ListView):
    model = Church
    template_name = 'companys/user_churches.html' 
    context_object_name = 'user-churches'
    paginate_by = 5

class ChurchCreateView(LoginRequiredMixin, CreateView):
    model = Church
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ChurchUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Church
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        church = self.get_object()
        if self.request.user == church.created_by:
            return True
        return False

class ChurchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Church
    success_url = '/'

    def test_func(self):
        church = self.get_object()
        if self.request.user == church.created_by:
            return True
        return False


class videoListView(ListView):
    model= Video
    ordering = ['-date_posted']
    paginate_by = 12

class videoDetailView(DetailView):
    model = Video


class UservideoListView(ListView):
    model = Video
    template_name = 'churches/user_videos.html' 
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



class photoListView(ListView):
    model= Photo
    ordering = ['-date_posted']
    paginate_by = 12

class photoDetailView(DetailView):
    model = Photo


class UserphotoListView(ListView):
    model = Photo
    template_name = 'companys/user_photo.html' 
    context_object_name = 'user-photo'
    paginate_by = 5

class Weekly_themeCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class Weekly_themeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        weekly_theme = self.get_object()
        if self.request.user == photo.created_by:
            return True
        return False

class photoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    success_url = '/'

    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.created_by:
            return True
        return False


class Weekly_themeListView(ListView):
    model= Weekly_theme
    ordering = ['-date_posted']
    paginate_by = 12

class Weekly_themeDetailView(DetailView):
    model = Weekly_theme


class UserWeekly_themeListView(ListView):
    model = Weekly_theme
    template_name = 'companys/user_weekly_themes.html' 
    context_object_name = 'user-weekly_themes'
    paginate_by = 5

class Weekly_themeCreateView(LoginRequiredMixin, CreateView):
    model = Weekly_theme
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class Weekly_themeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Weekly_theme
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        weekly_theme = self.get_object()
        if self.request.user == weekly_theme.created_by:
            return True
        return False

class Weekly_themeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Weekly_theme
    success_url = '/'

    def test_func(self):
        weekly_theme = self.get_object()
        if self.request.user == weekly_theme.created_by:
            return True
        return False


class sermonListView(ListView):
    model= Sermon
    ordering = ['-date_posted']
    paginate_by = 12

class sermonDetailView(DetailView):
    model = Sermon


class UsersermonListView(ListView):
    model = Sermon
    template_name = 'companys/user_sermons.html' 
    context_object_name = 'user-sermons'
    paginate_by = 5

class sermonCreateView(LoginRequiredMixin, CreateView):
    model = Sermon
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class sermonUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Sermon
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        sermon = self.get_object()
        if self.request.user == sermon.created_by:
            return True
        return False

class sermonDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Sermon
    success_url = '/'

    def test_func(self):
        sermon = self.get_object()
        if self.request.user == sermon.created_by:
            return True
        return False