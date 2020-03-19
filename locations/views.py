from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Location

class LocationListView(generic.ListView):
    """Generic class-based view for a list of plots."""
    model = Location
    paginate_by = 100


class LocationDetailView(generic.DetailView):
    """Generic class-based detail view for a plot."""
    model = Location