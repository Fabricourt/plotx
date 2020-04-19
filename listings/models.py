from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from realtors.models import Broker
from towns.models import Town
from locations.models import Location
from companys.models import Business
from thumbnails.models import Thumbnail
from PIL import Image


class Bg_color(models.Model):
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.color

class Color(models.Model):
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.color

class Hover_color(models.Model):
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.color

class Hover_border_color(models.Model):
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.color

class Hover_text_color(models.Model):
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.color

class Border_color(models.Model):
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.color

class Text_color(models.Model):
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.color

class Footer_color(models.Model):
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.color

class Plot_size(models.Model):
    size = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.size

class Plot_status(models.Model):
    status = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.status

class Plot_type(models.Model):
    type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.type

class Payment_plan(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Road(models.Model):
    type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.type

class Population(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Development(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Neighbor(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name




# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True)
    plot_status =  models.ForeignKey(Plot_status, on_delete=models.DO_NOTHING,  blank=True, null=True)
    broker = models.ForeignKey(Broker, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    business = models.ForeignKey(Business, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    bg_color = models.ForeignKey(Bg_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    hover_color = models.ForeignKey(Hover_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    border_color = models.ForeignKey(Border_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    text_color = models.ForeignKey(Text_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    town = models.ForeignKey(Town, on_delete=models.DO_NOTHING,  blank=False, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING,  blank=False, null=True, help_text='add a location closet to the plot in the picked town' )
    description = RichTextField(blank=False, null=True)
    price = models.IntegerField( blank=False, null=True)
    payment_plan =  models.ForeignKey(Payment_plan, on_delete=models.DO_NOTHING,   blank=False, null=True, help_text='mode of payment required')
    water = models.CharField(max_length=100, blank=False, null=True, help_text='the distance from water pipe or source')
    roads = models.ForeignKey(Road, on_delete=models.DO_NOTHING,  blank=False, null=True)
    electricity = models.CharField(max_length=100,  blank=False, null=True, help_text='distance from the closest transformer') 
    population = models.ForeignKey(Population, on_delete=models.DO_NOTHING,  blank=False, null=True)
    development = models.ForeignKey(Development, on_delete=models.DO_NOTHING,  blank=False, null=True)
    neighbor =  models.ForeignKey(Neighbor, on_delete=models.DO_NOTHING,  blank=False, null=True)
    plot_type =  models.ForeignKey(Plot_type, on_delete=models.DO_NOTHING,  blank=False, null=True)
    plot_size =  models.ForeignKey(Plot_size, on_delete=models.DO_NOTHING,  blank=False, null=True)
    #thumbnail =  models.ForeignKey(Thumbnail, on_delete=models.DO_NOTHING,  blank=True, null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    pytube_video_link = models.CharField(max_length=1000, blank=True, null=True)
    plot_video = models.FileField(upload_to='videos/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        """Returns the url to access a particular Listing instance."""
        return reverse('listing-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Videolisting(models.Model):
    title = models.CharField(max_length=100)
    videofile= models.FileField(upload_to='videos/', blank=False, null=True, )
    Business = models.ForeignKey(Business, on_delete=models.DO_NOTHING, blank=False, null=True)
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING, blank=False, null=True)
    broker = models.ForeignKey(Broker, on_delete=models.DO_NOTHING, blank=False, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    description = RichTextField(blank=False, null=True)

    def __str__(self):
        return self.listing.title


