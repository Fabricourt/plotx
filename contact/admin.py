from django.contrib import admin

from .models import Contactk, Contact

class ContactkAdmin(admin.ModelAdmin):
  list_display = ('id', 'name',  'email', 'timestamp')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email')
  list_per_page = 25

admin.site.register(Contactk, ContactkAdmin)

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'business', 'header', 'email', 'timestamp')
  list_display_links = ('id', 'name', 'business')
  search_fields = ('name', 'email', 'business')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)