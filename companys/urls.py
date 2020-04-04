from django.urls import path
from .views import (
    UserBusinessListView,
    BusinessListView,
    BusinessDetailView,
    BusinessCreateView,
    BusinessUpdateView,
    BusinessDeleteView,
    SearchResultsListView
)
from . import views


urlpatterns = [
    path('business-list/', BusinessListView.as_view(), name='business-list'),
    path('user/<str:username>', UserBusinessListView.as_view(), name='user-businesss'),
    path('business/<int:pk>/', BusinessDetailView.as_view(), name='business-detail'),
    path('business/new/', BusinessCreateView.as_view(), name='business-create'),
    path('business/<int:pk>/update/', BusinessUpdateView.as_view(), name='business-update'),
    path('business/<int:pk>/delete/', BusinessDeleteView.as_view(), name='business-delete'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
