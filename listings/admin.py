from django.contrib import admin

# Register your models here.
from .models import Listing, Bg_color, Color, Text_color, Border_color, Hover_color, Footer_color, Hover_border_color, Hover_text_color, Plot_size, Plot_status, Plot_type, Payment_plan, Road, Population, Development, Neighbor


admin.site.register(Listing)
admin.site.register(Bg_color)
admin.site.register(Hover_color)
admin.site.register(Border_color)
admin.site.register(Color)
admin.site.register(Text_color)
admin.site.register(Hover_border_color)
admin.site.register(Hover_text_color)
admin.site.register(Footer_color)
admin.site.register(Plot_size)
admin.site.register(Plot_type)
admin.site.register(Plot_status)
admin.site.register(Payment_plan)
admin.site.register(Road)
admin.site.register(Population)
admin.site.register(Development)
admin.site.register(Neighbor)