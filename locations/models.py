from django.db import models
from django.urls import reverse

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    location_pic = models.ImageField(upload_to='photos/%Y/%m/%d/',null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        """Returns the url to access a particular realtor instance."""
        return reverse('location-detail', args=[str(self.id)])

    def __str__(self):
        return self.name