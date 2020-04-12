from django.contrib import admin
from .models import  Bg_color, Color, Text_color, Border_color, Hover_color, Hover_text_color, Hover_border_color, Footer_color

# Register your models here.
admin.site.register(Bg_color)
admin.site.register(Hover_color)
admin.site.register(Hover_text_color)
admin.site.register(Hover_border_color)
admin.site.register(Footer_color)
admin.site.register(Border_color)
admin.site.register(Color)
admin.site.register(Text_color)