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

#from .forms import RenewBookForm
from catalog.forms import TruckloanPlotForm

# Create your views here.
from .models import Plot_size, Plot_type, Payment_plan, Road, Population, Development, Neighbor, Realtor, Company, Plot, PlotInstance
from towns.models import Town
from locations.models import Location

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_plots = Plot.objects.all().count()
    num_towns = Town.objects.all().count()
    num_locations = Location.objects.all().count()
    num_instances = PlotInstance.objects.all().count()
    # Available copies of plots
    num_instances_available = PlotInstance.objects.filter(status__exact='a').count()
    num_realtors = Realtor.objects.count()  # The 'all()' is implied by default.
    num_companys = Company.objects.count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1


    
    towns = Town.objects.order_by('name').filter(is_published=True)

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={
            'num_plots':num_plots,
            'num_towns':num_towns,
            'num_locations':num_locations,
            'num_instances':num_instances,'num_instances_available':num_instances_available,
            'num_companys':num_companys,
            'num_realtors':num_realtors,
            'num_visits':num_visits,
            'towns':towns,
           
            },
    )



class TownListView(generic.ListView):
    """Generic class-based view for a list of plots."""
    model = Town
    paginate_by = 10


class TownDetailView(generic.DetailView):
    """Generic class-based detail view for a plot."""
    model = Town

class LocationListView(generic.ListView):
    """Generic class-based view for a list of plots."""
    model = Location
    paginate_by = 10
    
class LocationDetailView(generic.DetailView):
    """Generic class-based detail view for a plot."""
    model = Location

class PlotListView(generic.ListView):
    """Generic class-based view for a list of plots."""
    model = Plot
    paginate_by = 10
    
class PlotDetailView(generic.DetailView):
    """Generic class-based detail view for a plot."""
    model = Plot

class RealtorListView(generic.ListView):
    """Generic class-based list view for a list of realtors."""
    model = Realtor
    paginate_by = 10 


class RealtorDetailView(generic.DetailView):
    """Generic class-based detail view for an realtor."""
    model = Realtor

class CompanyListView(generic.ListView):
    """Generic class-based list view for a list of companys."""
    model = Company
    paginate_by = 10 


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


@permission_required('catalog.can_mark_paid')
def renew_loaninstallment_secretary(request, pk):
    """View function for renewing  a specific PlotInstance by secretary."""
    plot_instance = get_object_or_404(PlotInstance, pk = pk)

    # If this is a town request then process the Form data
    if request.method == 'town':

        # Create a form instance and populate it with data from the request (binding):
        form = TruckloanPlotForm(request.town)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            plot_instance.due_back = form.cleaned_data['renewpayment_date']
            plot_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-loaned') )

    # If this is a GET (or any other method) create the default form
    else:
        proposed_renewpayment_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = TruckloanPlotForm(initial={'renewpayment_date': proposed_renewpayment_date,})

    context = {
        'form': form,
        'plot_instance': plot_instance,
    }

    return render(request, 'catalog/plot_renewpayment_date_secretary.html', context)

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
class PlotCreate(PermissionRequiredMixin, CreateView):
    model = Plot
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

class PlotUpdate(PermissionRequiredMixin, UpdateView):
    model = Plot
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

class PlotDelete(PermissionRequiredMixin, DeleteView):
    model = Plot
    success_url = reverse_lazy('plots')
    permission_required = 'catalog.can_mark_paid'

# Classes created for the forms challenge
class TownCreate(PermissionRequiredMixin, CreateView):
    model = Plot
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

class TownUpdate(PermissionRequiredMixin, UpdateView):
    model = Plot
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

class TownDelete(PermissionRequiredMixin, DeleteView):
    model = Plot
    success_url = reverse_lazy('plots')
    permission_required = 'catalog.can_mark_paid'

# Classes created for the forms challenge
class LocationCreate(PermissionRequiredMixin, CreateView):
    model = Plot
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

class LocationUpdate(PermissionRequiredMixin, UpdateView):
    model = Plot
    fields = '__all__'
    permission_required = 'catalog.can_mark_paid'

class LocationDelete(PermissionRequiredMixin, DeleteView):
    model = Plot
    success_url = reverse_lazy('plots')
    permission_required = 'catalog.can_mark_paid'