from django.shortcuts import render, redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .forms import *
from classes.models import *
from students.models import *
from django.views.generic.base import TemplateView
from subjects.models import *
from lessons.models import *
from exercises.models import *
from users.models import *
from django.shortcuts import render, get_object_or_404 
from django.views import generic
from classes.models import *
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)





def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('classes')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'users/login.html')


@login_required
def profile(request):
    classes = Class.objects.order_by('class_name').filter(is_published=True)
    students = Student.objects.order_by('first_name').filter(is_published=True)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'classes':classes,
        'students':students,
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

class AccountListView(ListView):
    model = Account
    queryset = Account.objects.all().order_by("-created_on")
    template_name = "account_list.html"
    paginate_by = 10


class AccountDetailView(DetailView):
    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.all()
        context['students'] = Student.objects.all()
        context['exercises'] = Exercise.objects.all()
        context['classes'] = Class.objects.all()
        return context

class UserAccountListView(ListView):
    model = Account
    template_name = 'users/user_accounts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'accounts'
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.all()
        context['students'] = Student.objects.all()
        context['exercises'] = Exercise.objects.all()
        context['classes'] = Class.objects.all()
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Account.objects.filter(accountname=user).order_by("-created_on") 


class AccountEnrollClass_nameView(LoginRequiredMixin, FormView):
    Class_name = None
    form_class = Class_nameEnrollForm

    def form_valid(self, form):
        self.class_name = form.cleaned_data['class_name']
        self.class_name.account.add(self.request.user)
        return super().form_valid(form)




 

