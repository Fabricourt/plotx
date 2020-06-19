from django.urls import path
from . import views
from .views import (
    NoticeListView,
    NoticeDetailView,
    #NoticeCreateView,
    #NoticeUpdateView,
    #NoticeDeleteView
)

urlpatterns = [
   
    path('notices/', NoticeListView.as_view(), name='notices'),
    path('notice/<slug:slug>/', NoticeDetailView.as_view(), name='notice-detail'),

]
