from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Town

class TownListView(generic.ListView):
    """Generic class-based view for a list of plots."""
    model = Town
    paginate_by = 100


class TownDetailView(generic.DetailView):
    """Generic class-based detail view for a plot."""
    model = Town

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Towns
        context['towns'] = Town.objects.all()
        return context