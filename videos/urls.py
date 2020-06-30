from django.urls import path
from .views import (
    videoListView,
    UservideoListView,
    videoDetailView,
    videoCreateView,
    videoUpdateView,
    videoDeleteView
)
from . import views

urlpatterns = [
    #videos urls
    path('video-list/', videoListView.as_view(), name='video-list'),
    path('user/<str:username>', UservideoListView.as_view(), name='user-videoes'),
    path('video/<slug:slug>/', videoDetailView.as_view(), name='video-detail'),
    path('video/new/', videoCreateView.as_view(), name='video-create'),
    path('video/<int:pk>/update/', videoUpdateView.as_view(), name='video-update'),
    path('video/<int:pk>/delete/', videoDeleteView.as_view(), name='video-delete'),

]