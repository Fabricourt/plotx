from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Exercise, Answer
from subjects.models import *
from students.models import *
from .forms import AnswerForm
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class ExerciseList(generic.ListView):
    queryset = Exercise.objects.filter(is_published=True).order_by("-created_on")
    template_name = "exercise_list.html"
    paginate_by = 10


# class ExerciseDetail(generic.DetailView):
#     model = Exercise
#     template_name = 'exercise_detail.html'


def exercise(request, slug):
    template_name = "exercise.html"
    exercise = get_object_or_404(Exercise, slug=slug)
    answers = exercise.answers.filter(active=True).order_by("-created_on")
    classes = Class.objects.order_by('class_name').filter(is_published=True)
    new_answer = None
    # answer exercise
    if request.method == "POST":
        answer_form = AnswerForm(request.POST, request.FILES)
        if answer_form.is_valid():
            # Create answer object but don't save to database yet
            new_answer = answer_form.save(commit=False)
            # Assign the current exercise to the answer
            new_answer.exercise = exercise

            new_answer.save()
    else:
        answer_form = AnswerForm()
    context = {
            "classes": classes,
            "exercise": exercise,
            "answers": answers,
            "new_answer": new_answer,
            "answer_form": answer_form,
    }
    return render(request, "exercises/exercise.html", context )



def answer(request, answer_id):
  answer = get_object_or_404(Answer, pk=answer_id)
  queryset = Exercise.objects.filter(status=1).order_by("-created_on")
  classes = Class.objects.order_by('class_name').filter(is_published=True)
  
  context = {
    'queryset': queryset,
    'answer': answer,
    "classes": classes,
  }
  return render(request, 'exercises/answer.html', context)


class UserExerciseListView(generic.ListView):

    model = Exercise
    template_name = 'exercises/user_exercises.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'exercises'
    paginate_by = 10

 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.all()
        context['students'] = Student.objects.all()
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Exercise.objects.filter(teacher=user).order_by("-created_on") 
          



def answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    context = {
        'answer': answer
    }

    return render(request, 'exercises/answer.html', context)

class AnswerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Answer
    fields = '__all__'

    def form_valid(self, form):
        form.instance. answer.exercise.teacher = self.request.user
        return super().form_valid(form)

    def test_func(self):
        answer = self.get_object()
        if self.request.user == answer.exercise.teacher:
            return True
        return False

