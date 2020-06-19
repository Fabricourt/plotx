from django.urls import path
from .views import (
    TeacherStudentListView,
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView
)
from . import views


urlpatterns = [
    path('students', StudentListView.as_view(), name='students'),
    path('user/<str:username>', TeacherStudentListView.as_view(), name='teacher-students'),
    path('student/<slug:slug>/', StudentDetailView.as_view(), name='student-detail'),
    path('student/new/', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

]