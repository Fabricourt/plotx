from django.urls import path
from . import views



urlpatterns = [
   
    path('towns/', views.TownListView.as_view(), name='towns'),
    path('town/<int:pk>', views.TownDetailView.as_view(), name='town-detail'),


]

