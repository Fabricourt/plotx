from django.contrib import admin

# Register your models here.

from .models import Plot_size, Plot_type, Payment_plan, Road, Population, Development, Neighbor, Realtor, Company, Plot, PlotInstance
from towns.models import Town
from locations.models import Location


admin.site.register(Plot_size)
admin.site.register(Plot_type)
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
            'fields': ('company_name', 'contact_person', 'logo', 'about_company', 'about_pic')
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

class PlotAdmin(admin.ModelAdmin):
    """Administration object for Plot models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of plot instances in plot view (inlines)
    """
    list_display = ('title', 'realtor', 'company', 'town','location')

admin.site.register(Plot, PlotAdmin)


@admin.register(PlotInstance)
class PlotnstanceAdmin(admin.ModelAdmin):
    """Administration object for PlotInstance models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('plot', 'status', 'buyer','next_payment_due_when', 'id')
    list_filter = ('status', 'next_payment_due_when')
    
    fieldsets = (
        (None, {
            'fields': ('Plot','Plot_number', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'next_payment_due_when','buyer')
        }),
    )