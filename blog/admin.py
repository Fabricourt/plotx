from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display= ('title', 'author', 'date_posted', 'is_published')
    list_filter =( 'author', 'title',)
    list_editable = ('is_published',)
    list_per_page = 25
admin.site.register(Post, PostAdmin)