from django.db import models
from django.urls import reverse
from locations.models import Location

# Create your models here.
class Town(models.Model):
    name = models.CharField(max_length=100)
    location = models.ManyToManyField(Location, blank=True,  help_text="Select The  Locations found in this Town")
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        """Returns the url to access a particular town instance."""
        return reverse('town-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

