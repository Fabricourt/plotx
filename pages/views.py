from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from catalog.models import Contactus, Plot_size, Plot_type, Payment_plan, Road, Population, Development, Neighbor, Realtor, Company, Plot, PlotInstance
from towns.models import Town
from locations.models import Location
from listings.models import Listing,  Bg_color, Color, Text_color, Border_color, Hover_color, Footer_color, Hover_border_color, Hover_text_color, Plot_size, Plot_status, Plot_type, Payment_plan, Road, Population, Development, Neighbor

from companys.models import Business, Business_type, Bg_color, Color, Text_color, Border_color, Hover_color, Footer_color, Hover_border_color, Hover_text_color

from realtors.models import Broker

# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_plots = Plot.objects.all().count()
    num_towns = Town.objects.all().count()
    num_locations = Location.objects.all().count()
    num_instances = PlotInstance.objects.all().count()
    # Available copies of plots
    num_instances_available = PlotInstance.objects.filter(status__exact='a').count()
    num_realtors = Realtor.objects.count()  # The 'all()' is implied by default.
    num_companys = Company.objects.count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    towns = Town.objects.order_by('name').filter(is_published=True)
    locations = Location.objects.order_by('name').filter(is_published=True)
    listings = Listing.objects.order_by('name').filter(is_published=True) 
    companys = Company.objects.order_by('name').filter(is_published=True)

    # Render the HTML template index.html with the data in the context variable.
    kiambu_businesss = Business.objects.all().filter(is_kiambu=True)
    ruiru_businesss = Business.objects.all().filter(is_ruiru=True)
    thika_businesss = Business.objects.all().filter(is_thika=True)
    maimahiu_businesss = Business.objects.all().filter(is_maimahiu=True)
    gatundu_businesss = Business.objects.all().filter(is_gatundu=True)

    return render(
        request,
        'pages/index.html',
        context={
            'num_plots':num_plots,
            'num_towns':num_towns,
            'num_locations':num_locations,
            'num_instances':num_instances,'num_instances_available':num_instances_available,
            'num_companys':num_companys,
            'num_realtors':num_realtors,
            'num_visits':num_visits,
            'towns':towns,
            'locations': locations,
            'companys' : companys,
            'listings' : listings,
            'thika_businesss': thika_businesss,
            'kiambu_businesss': kiambu_businesss,
            'ruiru_businesss': ruiru_businesss,
            'gatundu_businesss': gatundu_businesss,
            'maimahiu_businesss': maimahiu_businesss

            },
    )


def Dashboard(request):
    num_towns = Town.objects.all().count()
    num_locations = Location.objects.all().count()
    # Available copies of plots
    num_realtors = Realtor.objects.count()  # The 'all()' is implied by default.
    num_businesss = Business.objects.count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    towns = Town.objects.order_by('name').filter(is_published=True)
    locations = Location.objects.order_by('name').filter(is_published=True)
    listings = Listing.objects.order_by('name').filter(is_published=True) 
    businesss = Business.objects.order_by('business_name').filter(is_published=True)

    kiambu_businesss = Business.objects.all().filter(is_kiambu=True)
    ruiru_businesss = Business.objects.all().filter(is_ruiru=True)
    thika_businesss = Business.objects.all().filter(is_thika=True)
    maimahiu_businesss = Business.objects.all().filter(is_maimahiu=True)
    gatundu_businesss = Business.objects.all().filter(is_gatundu=True)

    context = {
        'num_towns':num_towns,
        'num_locations':num_locations,
        'num_businesss':num_businesss,
        'num_realtors':num_realtors,
        'num_visits':num_visits,
        'towns' : towns,
        'locations': locations,
        'businesss' :businesss,
        'listings' : listings,
        'thika_businesss': thika_businesss,
        'kiambu_businesss': kiambu_businesss,
        'gatundu_businesss': gatundu_businesss,
        'maimahiu_businesss': maimahiu_businesss,
        'ruiru_businesss': ruiru_businesss        

    }
    return render(request, 'pages/dashboard.html', context) 


@staff_member_required
def mobile(request):
    return render(request, 'pages/mobile.html') 

@staff_member_required
def tablet(request):
    return render(request, 'pages/tablet.html') 

@staff_member_required
def laptop(request):
    return render(request, 'pages/laptop.html') 