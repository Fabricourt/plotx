from django.contrib import admin

# Register your models here.
from .models import Business, Business_type, Bg_color, Color, Text_color, Border_color, Hover_color, Footer_color, Hover_border_color, Hover_text_color
from reviews.models import Businessreview



admin.site.register(Business_type)
admin.site.register(Bg_color)
admin.site.register(Hover_color)
admin.site.register(Hover_text_color)
admin.site.register(Hover_border_color)
admin.site.register(Footer_color)
admin.site.register(Border_color)
admin.site.register(Color)
admin.site.register(Text_color)

class ReviewInline(admin.TabularInline):
    model = Businessreview

class BusinessAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
list_display = ("business_name", "business_type", "email_1", "phone_1")
admin.site.register(Business, BusinessAdmin)
