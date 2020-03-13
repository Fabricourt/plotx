from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'company', 'header', 'email', 'timestamp')
  list_display_links = ('id', 'name', 'company')
  search_fields = ('name', 'email', 'company')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)