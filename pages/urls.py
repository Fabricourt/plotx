from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mobile', views.mobile, name='mobile'), 
    path('tablet', views.tablet, name='tablet'),
    path('laptop', views.laptop, name='laptop'),
    path('churchdetail', views.churchdetail, name='churchdetail'),
    path('dashboard', views.Dashboard, name='dashboard'),
]