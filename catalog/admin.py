from django.contrib import admin

# Register your models here.

from .models import Bg_color, Color, Text_color, Hover_color, Border_color, Plot_size, Plot_status, Plot_type, Payment_plan, Road, Population, Development, Neighbor, Realtor, Contactus, Company, Plot, PlotInstance
from towns.models import Town
from locations.models import Location

admin.site.register(Bg_color)
admin.site.register(Hover_color)
admin.site.register(Border_color)
admin.site.register(Color)
admin.site.register(Text_color)
admin.site.register(Plot_size)
admin.site.register(Plot_type)
admin.site.register(Plot_status)
admin.site.register(Payment_plan)
admin.site.register(Town)
admin.site.register(Location)
admin.site.register(Road)
admin.site.register(Population)
admin.site.register(Development)
admin.site.register(Neighbor)


class PlotsInline(admin.TabularInline):
    """Defines format of inline plot insertion (used in Realtor & Company Admin)"""
    model = Plot


@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    """Administration object for Realtor models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of plots in Realtor view (inlines)
    """
    list_display = ('last_name', 'first_name', 'phone', 'created_on')
 
@admin.register(Contactus)
class ContactusAdmin(admin.ModelAdmin):
    list_display = ('name', 'header', 'message', 'company', 'created_on', 'approved_contactus')
    list_filter = ('approved_contactus', 'created_on')
    search_fields = ('name', 'email', 'message')
    approved_contactus = ['approve_messages']

    def approve_messages(self, request, queryset):
        queryset.update(active=True)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Administration object for Company models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of plots in company view (inlines)
    """
    list_display = ('company_name', 'contact_person', 'phone_1', 'created_on')
    fieldsets = (
        ('Standard info', {
            'fields': ('company_name', 'company_slogan', 'company_created_on', 'contact_person', 'logo', 'company_pic', 'about_company', 'about_pic', )
        }),
        ('Colors info', {
            'fields': ('bg_color','hover_color', 'border_color', 'color','text_color','footer_color' )
        }),
        ('Realtors info', {
            'fields': ('realtor',)
        }),
        ('Services info', {
            'fields': ('services', 'service_pic')
        }),
        ('Location info', {
            'fields': ('location', 'town')
        }),
        ('Contact info', {
            'fields': ('website', 
                ('email_1', 'email_2'),
                ('phone_1', 'phone_2')
                )
        }),
        ('Social info', {
            'fields': ('facebook', 'twitter', 'Instagram')
        }),
    )




class PlotsInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion (used in BookAdmin)"""
    model = PlotInstance

@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    """Administration object for Plot models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of plot instances in plot view (inlines)
    """
    list_display = ('title', 'realtor', 'company', 'town','location')
    fieldsets = (
    ('standard info', {
            'fields': ('title', 'realtor', 'company', 'town','location' )
        }),
    ('Colors info', {
            'fields': ('bg_color','hover_color', 'border_color', 'color','text_color', )
        }),
    )




