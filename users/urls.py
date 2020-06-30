from django.urls import path
#from . import views
from users.views import (
    AccountListView,
    AccountDetailView,
    UserAccountListView,
)

urlpatterns = [
    #path('register/', views.AccountRegistrationView.as_view(), name='account-registration'),
    #path('enroll-classx/', views.AccountEnrollClassxView.as_view(), name='account_enroll_classx'),
    path('account-list', AccountListView.as_view(), name='account-list'),
    path('account/<slug:slug>/', AccountDetailView.as_view(), name='account-detail'),
    path('user/<str:username>', UserAccountListView.as_view(), name='user-accounts'),
]
