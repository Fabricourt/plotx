from django.db import models
from django.urls import reverse
# Create your models here.


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