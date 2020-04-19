from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

# Create your models here.
class Thumbnail(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True)
    image = models.ImageField(
    upload_to="listing-thumbnails", null=True
    )

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)