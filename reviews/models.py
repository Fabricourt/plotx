from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from towns.models import Town
from companys.models import Business
from locations.models import Location
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Businessreview(models.Model):
    heading = models.CharField(max_length=200, blank=False, null=True)
    business = models.ForeignKey(Business, on_delete=models.DO_NOTHING, blank=True, null=False)
    review = models.TextField(blank=False,null=True, help_text="simple is better than complex")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.business.business_name