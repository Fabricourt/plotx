from django.contrib import admin
from .models import *



class StudentAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'middle_name', 'last_name',  'age', 'classname', 'title', 'address', 'phone', 'is_published', )
  list_display_links = ('last_name',)
  list_filter = ('title', 'classname',)
  list_editable = ('is_published', )
  search_fields = ('first_name', 'middle_name', 'last_name', 'address', )
  prepopulated_fields = {"slug": ('first_name','middle_name', 'last_name',)}
  list_per_page = 25


admin.site.register(Student, StudentAdmin)
