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
from .models import Broker
from django.contrib.auth.models import User
from towns.models import Town


class BrokerListView(ListView):
    model = Broker
    template_name = 'brokers/brokers.html'
    context_object_name = 'brokers'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Towns
        context['towns'] = Town.objects.all()
        return context


class BrokerDetailView(DetailView):
    model = Broker

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Towns
        context['towns'] = Town.objects.all()
        return context


class UserBrokerListView(ListView):
    model = Broker
    template_name = 'brokers/user_brokers.html' 
    context_object_name = 'brokers'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Broker.objects.filter(created_by=user).order_by('-date_posted') 

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Towns
        context['towns'] = Town.objects.all()
        return context



class BrokerCreateView(LoginRequiredMixin, CreateView):
    model = Broker
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Towns
        context['towns'] = Town.objects.all()
        return context


class BrokerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Broker
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        broker = self.get_object()
        if self.request.user == broker.created_by:
            return True
        return False

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the towns
        context['towns'] = Town.objects.all()
        return context


class BrokerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Broker
    success_url = '/'

    def test_func(self):
        broker = self.get_object()
        if self.request.user == broker.created_by:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the towns
        context['towns'] = Town.objects.all()
        return context