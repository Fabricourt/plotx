from django.urls import path
from .views import (
    UserBrokerListView,
    BrokerListView,
    BrokerDetailView,
    BrokerCreateView,
    BrokerUpdateView,
    BrokerDeleteView
)
from . import views


urlpatterns = [
    path('brokers/', BrokerListView.as_view(), name='brokers'),
    path('user/<str:username>', UserBrokerListView.as_view(), name='user-brokers'),
    path('broker/<int:pk>/', BrokerDetailView.as_view(), name='broker-detail'),
    path('broker/new/', BrokerCreateView.as_view(), name='broker-create'),
    path('broker/<int:pk>/update/', BrokerUpdateView.as_view(), name='broker-update'),
    path('broker/<int:pk>/delete/', BrokerDeleteView.as_view(), name='broker-delete'),
]
