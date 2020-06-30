from django.contrib import admin
from .models import *
from django.contrib.auth.models import User



class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('id_number', 'email', 'phone')
    list_filter = ('user',)

admin.site.register(Profile, ProfileAdmin)




class AccountAdmin(admin.ModelAdmin):
  list_display = ('accountname', 'fullname', 'user_class',  'is_published', )
  list_display_links = ('accountname',)
  list_filter = ('accountname', 'fullname',)
  list_editable = ('is_published', )
  search_fields = ('accountname', 'middle_name', )
  prepopulated_fields = {"slug": ('fullname',)}
  list_per_page = 25


admin.site.register(Account, AccountAdmin)
