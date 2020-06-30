from django.urls import path
from . import views
from .views import (
    ClassListView,
    ClassDetailView,
    #ClassCreateView,
    #ClassUpdateView,
    #ClassDeleteView
)

urlpatterns = [
   
    path('classes/', ClassListView.as_view(), name='classes'),
    path('class/<slug:slug>/', ClassDetailView.as_view(), name='class-detail'),


]
