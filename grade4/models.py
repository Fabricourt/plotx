from django.db import models
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from PIL import Image
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
# Create your models here.

"""class Classroom(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    slug = models.SlugField(max_length=250, blank=False, null=True, unique_for_date='date_posted', help_text='You must re enter the class name using dashes e.g class 7 west = class-7-west on the slug field')
    class_teacher =  models.ForeignKey(User, on_delete=models.DO_NOTHING,  blank=True, null=True, related_name='class_teacher')
    class_monitor =  models.ForeignKey(User, on_delete=models.DO_NOTHING,  blank=True, null=True, related_name='class_monitor')
    class_prefect =  models.ForeignKey(User, on_delete=models.DO_NOTHING,  blank=True, null=True, related_name='class_prefect')
    about_class = RichTextField(blank=False, null=True)
    #students = models.ManyToManyField(User,related_name='class_joined',blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)



    def get_absolute_url(self):
        return reverse('classroom-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.class_name


class Learning_area(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    teacher = models.ForeignKey(User, related_name='strands_created', on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Strand(models.Model):
    learning_a = models.ForeignKey(Learning_area, related_name='strands', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title




class Sub_strand(models.Model):
    strand = models.ForeignKey(Strand, related_name='sub_strand', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = OrderField(blank=True, for_fields=['strand'])

    def __str__(self):
        return f'{self.order}. {self.title}'

    class Meta:
        ordering = ['order']
        
class Content(models.Model):
    Sub_strand = models.ForeignKey(Sub_strand, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'model__in':(
                                     'text',
                                     'video',
                                     'image',
                                     'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['sub_strand'])

    class Meta:
        ordering = ['order']



class ItemBase(models.Model):
    teacher = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string(
        f'strands/content/{self._meta.model_name}.html',
        {'item': self})

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
       file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()

"""