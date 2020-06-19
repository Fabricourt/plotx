from django.contrib import admin
from .models import *

class AnswerInline(admin.StackedInline):
  model = Answer
  
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
  list_display = ('title', 'classname', 'subject', 'topic', 'teacher', 'is_published' )
  list_display_links = ('title',)
  list_filter = ('classname', 'subject', 'topic',  'teacher',)
  list_editable = ('is_published', )
  #search_fields = ('classname', 'subject', 'topic', 'lesson', 'teacher', 'title',)
  prepopulated_fields = {"slug": ('title',)}
  list_per_page = 25
  inlines = [AnswerInline]



