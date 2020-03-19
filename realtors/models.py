from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from towns.models import Town
from locations.models import Location
from companys.models import Business


# Create your models here.
class Broker(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    town = models.ForeignKey(Town, on_delete=models.DO_NOTHING, blank=True, null=True,  help_text="Select the towns where this realtor is found")
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True, help_text="Select The  Locations where this realtor  is found in the choosen Town")
    business = models.ForeignKey(Business, on_delete=models.DO_NOTHING, blank=True, null=True, help_text="Select The Company this realtor belongs to")
    profile = models.ImageField(default='avatar.jpg', upload_to='profiles/%Y/%m/%d/', blank=True)
    about_realtor = models.TextField(max_length=1000, blank=True, null=True, help_text="Enter a brief description of the Realtor.")
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    

    def get_absolute_url(self):
        """Returns the url to access a particular Listing instance."""
        return reverse('broker-detail', args=[str(self.id)])

    def __str__(self):
        return self.first_name