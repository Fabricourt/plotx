from django.urls import path
from django.views.generic import RedirectView
from . import views



urlpatterns = [
    path('exam_room', views.exam_room, name='exam_room'),
]