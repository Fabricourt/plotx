from django.urls import path

from . import views

urlpatterns = [
  path('contactk', views.contactk, name='contactk'),
  path('contact', views.contact, name='contact')
]