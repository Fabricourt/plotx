from django.urls import path
from .views import (
    TeacherLessonListView,
    LessonListView,
    LessonDetailView,
    LessonCreateView,
    LessonUpdateView,
    LessonDeleteView
)
from . import views


urlpatterns = [
    path('lessons', LessonListView.as_view(), name='lessons'),
    path('user/<str:username>', TeacherLessonListView.as_view(), name='teacher-lessons'),
    path('lesson/<slug:slug>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('lesson/new/', LessonCreateView.as_view(), name='lesson-create'),
    path('lesson/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson-update'),
    path('lesson/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson-delete'),

   
]