from django.urls import path

from users.views import (
    AccountListView,
    AccountDetailView,
    UserAccountListView,
)

urlpatterns = [
    path('account-list', AccountListView.as_view(), name='account-list'),
    path('account/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('user/<str:username>', UserAccountListView.as_view(), name='user-accounts'),
]
