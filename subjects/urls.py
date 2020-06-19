from django.urls import path
from .views import (
    SubjectListView,
    SubjectDetailView,
)
from . import views


urlpatterns = [
    path('subjects', SubjectListView.as_view(), name='subjects'),
    path('subject/<slug:slug>/', SubjectDetailView.as_view(), name='subject-detail'),
]