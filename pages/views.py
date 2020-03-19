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

    # Render the HTML template index.html with the data in the context variable.
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
           
            },
    )


def Dashboard(request):
    return render(request, 'dashboard.html') 


@staff_member_required
def mobile(request):
    return render(request, 'pages/mobile.html') 

@staff_member_required
def tablet(request):
    return render(request, 'pages/tablet.html') 

@staff_member_required
def laptop(request):
    return render(request, 'pages/laptop.html') 