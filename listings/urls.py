from django.urls import path
from .views import (
    UserListingListView,
    ListingListView,
    ListingDetailView,
    ListingCreateView,
    ListingUpdateView,
    ListingDeleteView
)
from . import views


urlpatterns = [
    path('listings/', ListingListView.as_view(), name='listings'),
    path('user/<str:username>', UserListingListView.as_view(), name='user-listings'),
    path('listing/<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('listing/new/', ListingCreateView.as_view(), name='listing-create'),
    path('listing/<int:pk>/update/', ListingUpdateView.as_view(), name='listing-update'),
    path('listing/<int:pk>/delete/', ListingDeleteView.as_view(), name='listing-delete'),
]
