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
from .models import Business
from towns.models import Town
from django.contrib.auth.models import User


class BusinessListView(ListView):
    model = Business
    ordering = ['-date_posted']
    paginate_by = 49

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the towns
        context['towns'] = Town.objects.all()
        return context
  


class BusinessDetailView(DetailView):
    model = Business

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the townss
        context['towns'] = Town.objects.all()
        return context


class UserBusinessListView(ListView):
    model = Business
    template_name = 'companys/user_businesss.html' 
    context_object_name = 'businesss'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Business.objects.filter(created_by=user).order_by('-date_posted')   
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the towns
        context['towns'] = Town.objects.all()
        return context
  



class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the towns
        context['towns'] = Town.objects.all()
        return context
  


class BusinessUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Business
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.created_by:
            return True
        return False

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the towns
        context['towns'] = Town.objects.all()
        return context
  


class BusinessDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Business
    success_url = '/'

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.created_by:
            return True
        return False

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the towns
        context['towns'] = Town.objects.all()
        return context
  