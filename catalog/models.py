from django.db import models
import uuid  # Required for unique book instances
from datetime import date
from datetime import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.


class Plot_size(models.Model):
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.size

class Plot_type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Payment_plan(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Town(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Road(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Population(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Development(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Neighbor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Realtor(models.Model):
    """Model representing an Realtor."""
    town = models.ManyToManyField(Town, blank=True, help_text="Select the town where this realtor is found")
    location = models.ManyToManyField(Location, blank=True,  help_text="Select The exact Location where this Company  is found in the choosen Town")
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    about_realtor = models.TextField(max_length=1000, help_text="Enter a brief description of the Realtor.")
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    Instagram = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateField(null=True, blank=True)
    
      
    def display_town(self):
        """Creates a string for the Town. This is required to display town in Admin."""
        return ', '.join([town.name for town in self.town.all()[:5]])

    display_town.short_description = 'Town'

    def display_location(self):
        """Creates a string for the Location. This is required to display location in Admin."""
        return ', '.join([location.name for location in self.location.all()[:5]])

    display_location.short_description = 'Location'

    class Meta:
        ordering = ['last_name', 'first_name', 'phone']

    def get_absolute_url(self):
        """Returns the url to access a particular realtor instance."""
        return reverse('realtor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)

class Company(models.Model):
    """Model representing an Realtor."""
    company_name = models.CharField(max_length=100, blank=True, null=True)
    about_company = models.TextField(max_length=1000, help_text="Enter a brief description of the company.")
    contact_person = models.CharField(max_length=100, blank=False, null=True)
    town = models.ManyToManyField(Town, blank=True,  help_text="Select The exact Town this company is located.")
    location = models.ManyToManyField(Location, blank=True, help_text="Select The exact Location where this Company  is found in the choosen Town")
    email_1 = models.CharField(max_length=100, blank=True, null=True)
    email_2 = models.CharField(max_length=100, blank=True, null=True)
    phone_1 = models.CharField(max_length=100, blank=True, null=True)
    phone_2 = models.CharField(max_length=100, blank=True, null=True)
    phone_2 = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    Instagram = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateField(null=True, blank=True)
    
    
    def display_town(self):
        """Creates a string for the Town. This is required to display town in Admin."""
        return ', '.join([town.name for town in self.town.all()[:5]])

    display_town.short_description = 'Town'

    def display_location(self):
        """Creates a string for the Location. This is required to display location in Admin."""
        return ', '.join([location.name for location in self.location.all()[:5]])

    display_location.short_description = 'Location'

    class Meta:
        ordering = ['company_name', 'contact_person', 'phone_1']

    def get_absolute_url(self):
        """Returns the url to access a particular company instance."""
        return reverse('realtor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Plot(models.Model):
    """Model representing a plot (but not a specific plot)."""
    title = models.CharField(max_length=200, blank=False, null=True)
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    town = models.ForeignKey(Town, on_delete=models.DO_NOTHING,  blank=False, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING,  blank=False, null=True, help_text='add a location closet to the plot in the picked town' )
    description = RichTextField(blank=False, null=True)
    price = models.IntegerField()
    payment_plan =  models.ForeignKey(Payment_plan, on_delete=models.DO_NOTHING,   blank=False, null=True, help_text='mode of payment required')
    water = models.CharField(max_length=100, blank=False, null=True, help_text='the distance from water pipe or source')
    roads = models.ForeignKey(Road, on_delete=models.DO_NOTHING,  blank=False, null=True)
    electricity = models.CharField(max_length=100, help_text='distance from the closest transformer') 
    population = models.ForeignKey(Population, on_delete=models.DO_NOTHING,  blank=False, null=True)
    development = models.ForeignKey(Development, on_delete=models.DO_NOTHING,  blank=False, null=True)
    neighbor =  models.ForeignKey(Neighbor, on_delete=models.DO_NOTHING,  blank=False, null=True)
    plot_type =  models.ForeignKey(Plot_type, on_delete=models.DO_NOTHING,  blank=False, null=True)
    plot_size =  models.ForeignKey(Plot_size, on_delete=models.DO_NOTHING,  blank=False, null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(blank=True, null=True)
    

def get_absolute_url(self):
    """Returns the url to access a particular book instance."""
    return reverse('book-detail', args=[str(self.id)])

def __str__(self):
    """String for representing the Model object."""
    return self.title

class PlotInstance(models.Model):
    """Model representing a specific plot (i.e. that can be bought)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular plot in the system")
    plot = models.ForeignKey('Plot', on_delete=models.SET_NULL, null=True)
    plot_number = models.CharField(null=True, blank=True, max_length=200)
    next_payment_due_when = models.DateField(null=True, blank=True)
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.next_payment_due_when and date.today() > self.next_payment_due_when:
            return True
        return False

    LOAN_STATUS = (
        ('s', 'Sold'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
        ('m', 'Maintenance'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='plot availability')

    class Meta:
        ordering = ['next_payment_due_when']
        permissions = (("can_mark_paid", "Set plot as paid"),)

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.plot.title)


