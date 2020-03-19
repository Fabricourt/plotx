from django.urls import path
from . import views


urlpatterns = [
   
    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),


]

