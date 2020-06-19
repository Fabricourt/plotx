from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

"""

class ClassroomAdmin(admin.ModelAdmin):
  list_display = ('name', 'class_teacher', 'class_prefect', 'class_monitor',  'is_published', )
  list_display_links = ('name','class_prefect', 'class_monitor')
  list_filter = ('name',)
  list_editable = ('is_published',)
  search_fields = ('name', 'class_teacher', 'class_monitor', 'class_prefect', )
  prepopulated_fields = {"slug": ('name',)}
  list_per_page = 25

admin.site.register(Classroom, ClassroomAdmin)

@admin.register(Learning_area)
class Learning_areaAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class Sub_strandInline(admin.StackedInline):
    model = Sub_strand



@admin.register(Strand)
class StrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'learning_a', 'created']
    list_filter = ['created', 'learning_a']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [Sub_strandInline]
    
"""