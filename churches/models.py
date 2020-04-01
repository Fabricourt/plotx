from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from towns.models import Town
from locations.models import Location
from datetime import datetime

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

class Church_denomination(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



 

# Create your models here.
class Church(models.Model):
    church_name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    church_denomination = models.ForeignKey(Church_denomination, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    contact_person = models.CharField(max_length=100, blank=False, null=True)
    church_slogan = models.CharField(max_length=200, blank=True, null=True)
    town = models.ForeignKey(Town, on_delete=models.DO_NOTHING, blank=True, null=True,  help_text="Select The exact towns where this church is located")
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True, help_text="Select The exact locations where this Church  is found in the choosen Town")
    church_pic =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    logo = models.ImageField(default='logo.png', upload_to='logos/%Y/%m/%d/', blank=True, null=True)
    about_pic = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True )
    service_pic = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True )
    about_church = RichTextField(max_length=1500, blank=False, null=True, help_text="Max 200 words")
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
    youtube = models.CharField(max_length=100, blank=True, null=True)
    Instagram = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_thika = models.BooleanField(default=False)
    is_ruiru = models.BooleanField(default=False)
    is_maimahiu = models.BooleanField(default=False)
    is_kiambu = models.BooleanField(default=False)
    is_gatundu = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('church-detail', args=[str(self.id)])

    def __str__(self):
        return self.church_name




STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Photo(models.Model):
    name= models.CharField(max_length=500)
    description = RichTextField(blank=False, null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False, null=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    church = models.ForeignKey(Church, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    def __str__(self):
        return self.name

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    description = RichTextField(blank=False, null=True)
    church = models.ForeignKey(Church, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class Weekly_theme(models.Model):
    church = models.ForeignKey(Church, on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=200, blank=False, null=True)
    text = RichTextField(max_length=4000, blank=True, null=True)
    #status = models.IntegerField(choices=STATUS, default=0)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    pub_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Theme_of_the_year(models.Model):
    text = models.CharField(max_length=1000)
    church = models.ForeignKey(Church, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.church.church_name  

class Daily_word(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True)
    church = models.ForeignKey(Church, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.church.church_name  
   
    
class Schedule(models.Model):
    church = models.ForeignKey(Church, on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=200, blank=False, null=True)
    orderofservice = RichTextField(blank=True, null=True)
    praiseandworship = models.CharField(max_length=100, blank=True,null=True)
    ministering_choir = models.CharField(max_length=100, blank=True, null=True)
    first_service_leader = models.CharField(max_length=200, blank=True, null=True)
    second_service_leader = models.CharField(max_length=200, blank=True, null=True)
    todays_speaker_1 = models.CharField(max_length=200, blank=True, null=True)
    todays_speaker_2 = models.CharField(max_length=200, blank=True, null=True)
    Service_date = models.DateTimeField(default=datetime.now, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    pub_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Announcement(models.Model):
    church = models.ForeignKey(Church, on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=200, blank=False, null=True)
    announcement = RichTextField(null=True, blank=True)
    announcement_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title



class Home_cell(models.Model):
    church = models.ForeignKey(Church, on_delete=models.DO_NOTHING, blank=True, null=True)
    cell_location = models.CharField(max_length=200, blank=False, null=True)
    cell_day = models.CharField(max_length=200, blank=False, null=True)
    cell_leader = models.CharField(max_length=200, blank=False, null=True)
    leader_contact = models.CharField(max_length=200, blank=False, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.cell_location 

class Church_group(models.Model):
    name = models.CharField(max_length=100)
    church = models.ForeignKey(Church, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    def __str__(self):
        return self.name

class Church_member(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    town = models.ForeignKey(Town, on_delete=models.DO_NOTHING, blank=True, null=True,  help_text="Select the towns where this realtor is found")
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True, help_text="Select The  Locations where this realtor  is found in the choosen Town")
    church = models.ForeignKey(Church, on_delete=models.DO_NOTHING, blank=True, null=True, help_text="Select The Company this realtor belongs to")
    church_group =  models.ForeignKey(Church_group, on_delete=models.DO_NOTHING, blank=True, null=True, help_text="Select The Company this realtor belongs to")
    home_cell_group =  models.ForeignKey(Home_cell, on_delete=models.DO_NOTHING, blank=True, null=True, help_text="Select The Company this realtor belongs to")
    profile = models.ImageField(default='avatar.jpg', upload_to='profiles/%Y/%m/%d/', blank=True)
    about_member = models.TextField(max_length=1000, blank=True, null=True, help_text="Enter a brief description of the Realtor.")
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name
    

class Church_choir(models.Model):
    choir_name = models.CharField(max_length=200, blank=False, null=True)
    church = models.ForeignKey(Church, on_delete=models.DO_NOTHING, blank=True, null=True)
    choir_leader = models.ForeignKey(Church_member, on_delete=models.DO_NOTHING, blank=True, null=True)
    leader_contact = models.CharField(max_length=200, blank=False, null=True)
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.choir_name



class Hymn(models.Model):
    hymn_title = models.CharField(max_length=100)
    hymn = RichTextField(max_length=1500, blank=False, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.hymn_title


class Hymn_of_the_week(models.Model):
    hymn_title = models.CharField(max_length=100)
    church = models.ForeignKey(Church, on_delete=models.DO_NOTHING, blank=True, null=True)
    hymn = models.ForeignKey(Hymn, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.hymn_title




class Sermon(models.Model):
    title = models.CharField(max_length=100)
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    sermon = RichTextField(blank=False, null=True)
    def __str__(self):
        return self.name


