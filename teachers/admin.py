from django.contrib import admin
from .models import *


admin.site.register(Skill)
admin.site.register(Language)

class TeacherAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'middle_name', 'last_name', 'title', 'address', 'phone', 'is_published', )
  list_display_links = ('last_name',)
  list_filter = ('last_name',)
  list_editable = ('is_published',)
  search_fields = ('first_name', 'middle_name', 'last_name', 'title', )
  prepopulated_fields = {"slug": ('first_name','middle_name', 'last_name',)}
  list_per_page = 25


admin.site.register(Teacher, TeacherAdmin)