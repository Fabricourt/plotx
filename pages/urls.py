from django.urls import path
from django.views.generic import RedirectView
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('homework', views.homework, name='homework'),
    path('gallery', views.gallery, name='gallery'),
    path('mobile', views.mobile, name='mobile'), 
    path('tablet', views.tablet, name='tablet'),
    path('laptop', views.laptop, name='laptop'),
    path('dashboard', views.Dashboard, name='dashboard'),
]