from django.urls import path
from . import views
from towns.models import Town
from locations.models import Location
from .views import (
    PlotListView,
    PlotDetailView,
    PlotCreateView,
    PlotUpdateView,
    PlotDeleteView
)

urlpatterns = [
    path('plot/new/', PlotCreateView.as_view(), name='plot-new'),
    path('plots/', views.PlotListView.as_view(), name='plots'),
    path('plot/<int:pk>', views.PlotDetailView.as_view(), name='plot-detail'),
    path('plot/<int:pk>', views.CompanyPlotDetailView.as_view(), name='companyplot-detail'),
    path('plot/<int:pk>/update/', views.PlotUpdateView.as_view(), name='plot-update'),
    path('plot/<int:pk>/delete/', views.PlotDeleteView.as_view(), name='plot-delete'),
  
    path('realtors/', views.RealtorListView.as_view(), name='realtors'),
    path('realtor/create/', views.RealtorCreate.as_view(), name='realtor_create'),
    path('realtor/<int:pk>/update/', views.RealtorUpdate.as_view(), name='realtor_update'),
    path('realtor/<int:pk>/delete/', views.RealtorDelete.as_view(), name='realtor_delete'),
    path('realtor/<int:pk>', views.RealtorDetailView.as_view(), name='realtor-detail'),
   
    path('companys/', views.CompanyListView.as_view(), name='companys'),
    path('company/<int:pk>', views.CompanyDetailView.as_view(), name='company-detail'), 
    path('company/create/', views.CompanyCreate.as_view(), name='company_create'),
    path('company/<int:pk>/update/', views.CompanyUpdate.as_view(), name='company_update'),
    path('company/<int:pk>/delete/', views.CompanyDelete.as_view(), name='company_delete'),

   
    path('towns/', views.TownListView.as_view(), name='towns'),
    path('town/<int:pk>', views.TownDetailView.as_view(), name='town-detail'),
    path('towns/create/', views.TownCreate.as_view(), name='town_create'),
    path('town/<int:pk>/update/', views.TownUpdate.as_view(), name='town_update'),
    path('town/<int:pk>/delete/', views.TownDelete.as_view(), name='town_delete'),


    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
    path('locations/create/', views.LocationCreate.as_view(), name='location_create'),
    path('location/<int:pk>/update/', views.LocationUpdate.as_view(), name='location_update'),
    path('location/<int:pk>/delete/', views.LocationDelete.as_view(), name='location_delete'),
    
    path('myplots/', views.LoanedPlotsByUserListView.as_view(), name='my-loaned'),
    path('loaned/', views.LoanedPlotsAllListView.as_view(), name='all-loaned'), # Added for challenge

]

