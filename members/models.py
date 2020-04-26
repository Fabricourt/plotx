from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from locations.models import Location
from towns.models import Town
from ckeditor.fields import RichTextField

# Create your models here.
class Member(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)


    def get_absolute_url(self):
        """Returns the url to access a particular town instance."""
        return reverse('member-detail', args=[str(self.id)])

    def __str__(self):
        return self.member.username

