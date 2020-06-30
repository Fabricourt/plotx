from django.contrib import admin
from .models import *
from blog.models import *

#class PostInline(admin.TabularInline):
  #model = Post
  



class ClassAdmin(admin.ModelAdmin):
  list_display = ('class_name', 'class_teacher', 'class_prefect', 'class_monitor',  'is_published', )
  list_display_links = ('class_name','class_prefect', 'class_monitor')
  list_filter = ('class_name',)
  list_editable = ('is_published',)
  search_fields = ('class_name', 'class_teacher', 'class_monitor', 'class_prefect', )
  prepopulated_fields = {"slug": ('class_name',)}
  list_per_page = 25
  #inlines = [PostInline]

admin.site.register(Class, ClassAdmin)