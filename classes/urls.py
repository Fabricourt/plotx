from django.urls import path
from . import views
from .views import (
    ClassListView,
    ClassDetailView,
    Class_nameListView,
    Class_nameDetailView,
    #ClassCreateView,
    #ClassUpdateView,
    #ClassDeleteView
)

urlpatterns = [
   
    path('classes/', ClassListView.as_view(), name='classes'),
    path('class/<slug:slug>/', ClassDetailView.as_view(), name='class-detail'),
    path('class_names/', Class_nameListView.as_view(), name='class_names'),
    path('class_name/<int:pk>/', Class_nameDetailView.as_view(), name='class_name-detail'),


]
