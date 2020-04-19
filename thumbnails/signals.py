from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Thumbnail


@receiver(post_save, sender=User)
def create_thumbnail(sender, instance, created, **kwargs):
    if created:
        Thumbnail.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_thumbnail(sender, instance, **kwargs):
    instance.thumbnail.save()