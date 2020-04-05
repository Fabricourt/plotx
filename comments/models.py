from django.db import models
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from towns.models import Town
from companys.models import Business
from locations.models import Location
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

"""
class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    business = models.ForeignKey(Business, on_delete=models.DO_NOTHING, blank=False, null=True)
    pub_date = models.DateTimeField('date published')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
    is_published = models.BooleanField(default=True)

    
    def __str__(self):
        return self.business.busines_name"""