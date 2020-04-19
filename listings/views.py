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

from towns.models import Town
from .models import Listing
from django.contrib.auth.models import User


class ListingListView(ListView):
    model = Listing
    template_name = 'listings/listings.html'
    context_object_name = 'listings'
    ordering = ['-date_posted']
    paginate_by = 5




class ListingDetailView(DetailView):
    model = Listing

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['towns'] = Town.objects.all()
        return context

class UserListingListView(ListView):
    model = Listing
    template_name = 'listings/user_listings.html' 
    context_object_name = 'listings'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Listing.objects.filter(created_by=user).order_by('-date_posted')   
  



class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ListingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Listing
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        listing = self.get_object()
        if self.request.user == listing.created_by:
            return True
        return False


class ListingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Listing
    success_url = '/'

    def test_func(self):
        listing = self.get_object()
        if self.request.user == listing.created_by:
            return True
        return False