from django.contrib import admin

from .models import  Review
from companys.models import Business
"""
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('business', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
    
admin.site.register(Business)
admin.site.register(Review, ReviewAdmin)"""