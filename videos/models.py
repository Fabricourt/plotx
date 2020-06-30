from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    video_name= models.CharField(max_length=500, blank=False, null=True)
    slug = models.SlugField(max_length=250,unique_for_date='date_posted')
    videofile= models.FileField(upload_to='Lesson_videos/%Y/%m/%d', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail-photos/%Y/%m/%d/', blank=True, null=True)
    description = RichTextField(blank=False, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='usercreator', blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('video-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.video_name

