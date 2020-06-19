from django.contrib import admin
from .models import *

  
class LessonInline(admin.StackedInline):
  model = Lesson
  
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
  list_display = ('subject', 'teacher', 'title', )
  list_display_links = ('title',)
  list_filter = ('subject', 'title', 'teacher',)
  search_fields = ('subject', 'teacher', 'title',)
  prepopulated_fields = {"slug": ('title',)}
  list_per_page = 25
  inlines = [LessonInline]




