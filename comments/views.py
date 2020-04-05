from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from companys.models import Business
from towns.models import Town
from django.contrib.admin.views.decorators import staff_member_required
from .models import Review
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

"""def reviews(request):
  reviews = Review.objects.order_by('-pub_date').filter(is_published=True)

  paginator = Paginator(reviews, 25)
  page = request.GET.get('page')
  paged_reviews = paginator.get_page(page)

  context = {
    'reviews': paged_reviews
  }

  return render(request, 'reviews/reviews.html', context)

def review(request, review_id):
  review = get_object_or_404(Review, pk=review_id)

  context = {
    'review': review
  }

  return render(request, 'reviews/review.html', context)"""
