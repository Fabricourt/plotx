from django.shortcuts import render
from django.views import generic
import datetime
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contactus, Plot_size, Plot_type, Payment_plan, Road, Population, Development, Neighbor, Realtor, Company, Plot, PlotInstance
from towns.models import Town
from locations.models import Location
from .forms import PlotForm





class TownListView(generic.ListView):
    """Generic class-based view for a list of plots."""
    model = Town
    paginate_by = 100


class TownDetailView(generic.DetailView):
    """Generic class-based detail view for a plot."""
    model = Town

class LocationListView(generic.ListView):
    """Generic class-based view for a list of plots."""
    model = Location
    paginate_by = 100
    
class LocationDetailView(generic.DetailView):
    """Generic class-based detail view for a plot."""
    model = Location

class PlotListView(generic.ListView):
    """Generic class-based view for a list of plots."""
    model = Plot
    paginate_by = 12
    
class PlotDetailView(generic.DetailView):
    """Generic class-based detail view for a plot."""
    model = Plot

# Classes created for the forms challenge
class PlotCreateView(LoginRequiredMixin, CreateView):
    model = Plot
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class PlotUpdateView(PermissionRequiredMixin, UpdateView):
    model = Plot
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == plot.created_by:
            return True
        return False

class PlotDeleteView(PermissionRequiredMixin, DeleteView):
    model = Plot
    success_url = reverse_lazy('plots')
    permission_required = 'catalog.can_mark_paid'

    def test_func(self):
        post = self.get_object()
        if self.request.user == plot.created_by:
            return True
        return False

class CompanyPlotDetailView(generic.DetailView):
    """Generic class-based detail view for a plot."""
    model = Plot

class RealtorListView(generic.ListView):
    """Generic class-based list view for a list of realtors."""
    model = Realtor
    paginate_by = 12 


class RealtorDetailView(generic.DetailView):
    """Generic class-based detail view for an realtor."""
    model = Realtor

class CompanyListView(generic.ListView):
    """Generic class-based list view for a list of companys."""
    model = Company
    paginate_by = 12 


class CompanyDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Company



  

class LoanedPlotsByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = PlotInstance
    template_name ='catalog/plotinstance_list_loaned_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return PlotInstance.objects.filter(buyer=self.request.user).filter(status__exact='o').order_by('next_payment_due_when')
        
class LoanedPlotsAllListView(PermissionRequiredMixin,generic.ListView):
    """Generic class-based view listing all plots on loan. Only visible to users with can_mark_paid permission."""
    model = PlotInstance
    permission_required = 'catalog.can_mark_paid'
    template_name ='catalog/plotinstance_list_loaned_all.html'
    paginate_by = 10
    
    def get_queryset(self):
        return PlotInstance.objects.filter(status__exact='o').order_by('next_payment_due_when')  


class RealtorCreate(PermissionRequiredMixin, CreateView):
    model = Realtor
    fields = '__all__'
    initial = {'created_on':'05/01/2020',}
    permission_required = 'catalog.can_mark_paid'

class RealtorUpdate(PermissionRequiredMixin, UpdateView):
    model = Realtor
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

class RealtorDelete(PermissionRequiredMixin, DeleteView):
    model = Realtor
    success_url = reverse_lazy('realtors')
    permission_required = 'catalog.can_mark_paid'


class CompanyCreate(PermissionRequiredMixin, CreateView):
    model = Company
    fields = '__all__'
    initial = {'created_on':'05/01/2020',}
    permission_required = 'catalog.can_mark_paid'

class CompanyUpdate(PermissionRequiredMixin, UpdateView):
    model = Company
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

class CompanyDelete(PermissionRequiredMixin, DeleteView):
    model = Company
    success_url = reverse_lazy('companys')
    permission_required = 'catalog.can_mark_paid'



# Classes created for the forms challenge
class TownCreate(PermissionRequiredMixin, CreateView):
    model = Town
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

class TownUpdate(PermissionRequiredMixin, UpdateView):
    model = Town
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

class TownDelete(PermissionRequiredMixin, DeleteView):
    model = Town
    success_url = reverse_lazy('plots')
    permission_required = 'catalog.can_mark_paid'

# Classes created for the forms challenge
class LocationCreate(PermissionRequiredMixin, CreateView):
    model = Location
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

class LocationUpdate(PermissionRequiredMixin, UpdateView):
    model = Location
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

class LocationDelete(PermissionRequiredMixin, DeleteView):
    model = Location
    success_url = reverse_lazy('plots')
    permission_required = 'catalog.can_mark_paid'




