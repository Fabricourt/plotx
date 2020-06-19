from . import views
from django.urls import path, include
from .views import (
    #UserAnswertListView,
    #--AnswerDetailView,
    AnswerUpdateView,
    UserExerciseListView,
)


urlpatterns = [
    path('exercise-list', views.ExerciseList.as_view(), name='exercise-list'),
    path("<slug:slug>/", views.exercise, name="exercise"),
    path('answer/<int:pk>/update/', AnswerUpdateView.as_view(), name='answer-update'),
    path('<int:answer_id>', views.answer, name='answer'),
    path('user/<str:username>', UserExerciseListView.as_view(), name='user-exercises'),
]   