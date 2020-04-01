from django.urls import path
from .views import (
    UserChurchListView,
    ChurchListView,
    ChurchDetailView,
    ChurchCreateView,
    ChurchUpdateView,
    ChurchDeleteView,
    UservideoListView,
    videoListView,
    videoDetailView,
    videoCreateView,
    videoUpdateView,
    videoDeleteView
)
from . import views


urlpatterns = [
    path('church-list/', ChurchListView.as_view(), name='church-list'),
    path('user/<str:username>', UserChurchListView.as_view(), name='user-churches'),
    path('church/<int:pk>/', ChurchDetailView.as_view(), name='church-detail'),
    path('church/new/', ChurchCreateView.as_view(), name='church-create'),
    path('church/<int:pk>/update/', ChurchUpdateView.as_view(), name='church-update'),
    path('church/<int:pk>/delete/', ChurchDeleteView.as_view(), name='church-delete'),

    #videos urls
    path('video-list/', videoListView.as_view(), name='video-list'),
    path('user/<str:username>', UservideoListView.as_view(), name='user-videoes'),
    path('video/<int:pk>/', videoDetailView.as_view(), name='video-detail'),
    path('video/new/', videoCreateView.as_view(), name='video-create'),
    path('video/<int:pk>/update/', videoUpdateView.as_view(), name='video-update'),
    path('video/<int:pk>/delete/', videoDeleteView.as_view(), name='video-delete'),

]
