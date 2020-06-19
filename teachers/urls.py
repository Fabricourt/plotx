from django.urls import path
from .views import (
    TeacherListView,
    TeacherDetailView,
    TeacherCreateView,
    TeacherUpdateView,
    TeacherDeleteView
)
from . import views


urlpatterns = [
    path('teachers', TeacherListView.as_view(), name='teachers'),
    path('teacher/<slug:slug>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('teacher/new/', TeacherCreateView.as_view(), name='teacher-create'),
    path('teacher/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher-update'),
    path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher-delete'),
  
]