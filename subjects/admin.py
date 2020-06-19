from django.contrib import admin
from .models import *



class SubjectAdmin(admin.ModelAdmin):
  list_display = ('subject_name', 'created_by', 'is_published', )
  list_display_links = ('subject_name',)
  list_filter = ('subject_name', 'created_by',)  
  list_editable = ('is_published',)
  search_fields = ('subject_name', 'created_by',  )
  prepopulated_fields = {"slug": ('subject_name',)}
  list_per_page = 25


admin.site.register(Subject, SubjectAdmin)