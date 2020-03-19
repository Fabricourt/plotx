from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from towns.models import Town
from locations.models import Location

class Bg_color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class Color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class Hover_color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class Hover_border_color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class Hover_text_color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class Border_color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color



class Text_color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class Footer_color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

# Create your models here.
class Business(models.Model):
    business_name = models.CharField(max_length=100, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=False, null=True)
    business_slogan = models.CharField(max_length=200, blank=True, null=True)
    town = models.ForeignKey(Town, on_delete=models.DO_NOTHING, blank=True, null=True,  help_text="Select The exact towns this company is located.")
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True, help_text="Select The exact locations where this Company  is found in the choosen Town")
    business_pic =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    logo = models.ImageField(default='logo.png', upload_to='logos/%Y/%m/%d/', blank=True, null=True)
    about_pic = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True )
    service_pic = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True )
    about_business = RichTextField(max_length=1500, blank=False, null=True, help_text="Max 200 words")
    services = RichTextField(max_length=1500, blank=False, null=True, help_text="Max 200 words")
    bg_color = models.ForeignKey(Bg_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    hover_color = models.ForeignKey(Hover_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    border_color = models.ForeignKey(Border_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    text_color = models.ForeignKey(Text_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    footer_color = models.ForeignKey(Footer_color, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    email_1 = models.CharField(max_length=100, blank=True, null=True)
    email_2 = models.CharField(max_length=100, blank=True, null=True)
    phone_1 = models.CharField(max_length=100, blank=True, null=True)
    phone_2 = models.CharField(max_length=100, blank=True, null=True)
    phone_2 = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    Instagram = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        """Returns the url to access a particular Broker instance."""
        return reverse('business-detail', args=[str(self.id)])

    def __str__(self):
        return self.business_name