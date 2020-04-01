from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Town
from locations.models import Location
from listings.models import Listing,  Bg_color, Color, Text_color, Border_color, Hover_color, Footer_color, Hover_border_color, Hover_text_color, Plot_size, Plot_status, Plot_type, Payment_plan, Road, Population, Development, Neighbor
from companys.models import Business, Business_type, Bg_color, Color, Text_color, Border_color, Hover_color, Footer_color, Hover_border_color, Hover_text_color
from realtors.models import Broker



 

class TownListView(generic.ListView):
    """Generic class-based view for a list of plots."""
    model = Town
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations']  = Location.objects.order_by('name').filter(is_published=True)
        context['listings']  = Listing.objects.order_by('name').filter(is_published=True) 
        context['kiambu_businesss'] = Business.objects.all().filter(is_kiambu=True)
        context['ruiru_businesss'] = ruiru_businesss = Business.objects.all().filter(is_ruiru=True)
        context['thika_businesss'] = thika_businesss = Business.objects.all().filter(is_thika=True)
        context['maimahiu_businesss'] = maimahiu_businesss = Business.objects.all().filter(is_maimahiu=True)
        context['gatundu_businesss'] = gatundu_businesss = Business.objects.all().filter(is_gatundu=True)
        return context


class TownDetailView(generic.DetailView):
    """Generic class-based detail view for a plot."""
    model = Town

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Towns
        context['towns'] = Town.objects.all()
        return context