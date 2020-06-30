from django.contrib import admin
from .models import *



class VideoAdmin(admin.ModelAdmin):
  list_display = ('video_name', 'created_by', 'is_published' )
  list_display_links = ('video_name',)
  list_filter = ('created_by', 'is_published',)
  list_editable = ('is_published', )
  search_fields = ('video_name', 'created_by', )
  prepopulated_fields = {"slug": ('video_name',)}
  list_per_page = 25


admin.site.register(Video, VideoAdmin)