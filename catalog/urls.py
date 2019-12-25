from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('plots/', views.PlotListView.as_view(), name='plots'),
    path('plot/<int:pk>', views.PlotDetailView.as_view(), name='plot-detail'),
    path('plot/<uuid:pk>/renew/', views.renew_loaninstallment_secretary, name='renew_loaninstallment_secretary'),
    path('plot/create/', views.PlotCreate.as_view(), name='plot_create'),
    path('plot/<int:pk>/update/', views.PlotUpdate.as_view(), name='plot_update'),
    path('plot/<int:pk>/delete/', views.PlotDelete.as_view(), name='plot_delete'),

    path('realtors/', views.RealtorListView.as_view(), name='realtors'),
    path('/create/', views.RealtorCreate.as_view(), name='realtor_create'),
    path('realtor/<int:pk>/update/', views.RealtorUpdate.as_view(), name='realtor_update'),
    path('realtor/<int:pk>/delete/', views.RealtorDelete.as_view(), name='realtor_delete'),
    path('realtor/<int:pk>', views.RealtorDetailView.as_view(), name='realtor-detail'),
   
    path('companys/', views.CompanyListView.as_view(), name='companys'),
    path('company/<int:pk>', views.CompanyDetailView.as_view(), name='company-detail'),
    path('company/create/', views.CompanyCreate.as_view(), name='company_create'),
    path('company/<int:pk>/update/', views.CompanyUpdate.as_view(), name='company_update'),
    path('company/<int:pk>/delete/', views.CompanyDelete.as_view(), name='company_delete'),
    
    path('myplots/', views.LoanedPlotsByUserListView.as_view(), name='my-loan'),
    path(r'loaned/', views.LoanedPlotsAllListView.as_view(), name='all-loaned'), # Added for challenge
]

