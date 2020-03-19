from django.contrib import admin

# Register your models here.
from .models import Business, Bg_color, Color, Text_color, Border_color, Hover_color, Footer_color, Hover_border_color, Hover_text_color

admin.site.register(Business)
admin.site.register(Bg_color)
admin.site.register(Hover_color)
admin.site.register(Hover_text_color)
admin.site.register(Hover_border_color)
admin.site.register(Footer_color)
admin.site.register(Border_color)
admin.site.register(Color)
admin.site.register(Text_color)