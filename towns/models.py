from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from locations.models import Location
from ckeditor.fields import RichTextField

# Create your models here.
class Town(models.Model):
    name = models.CharField(max_length=100,  blank=False, null=True)
    county = models.CharField(max_length=100, blank=False, null=True)
    population = models.IntegerField(blank=False, null=True)
    about_town = RichTextField(blank=False, null=True)
    town_pic = models.ImageField(upload_to='towns/%Y/%m/%d/',null=True, blank=False)
    town_pic1 = models.ImageField(upload_to='towns/%Y/%m/%d/',null=True, blank=False)
    town_pic2 = models.ImageField(upload_to='towns/%Y/%m/%d/',null=True, blank=False)
    county_flag_pic = models.ImageField(upload_to='countys_flags/%Y/%m/%d/',null=True, blank=False)
    tytube_video_link = models.CharField(max_length=1000, blank=True, null=True)
    town_video = models.FileField(upload_to='videos/', null=True, blank=True)
    location = models.ManyToManyField(Location, blank=True,  help_text="Select The  Locations found in this Town")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    is_published = models.BooleanField(default=True)


    def get_absolute_url(self):
        """Returns the url to access a particular town instance."""
        return reverse('town-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

