from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User



class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('id_number', 'email', 'phone')
    list_filter = ('user',)

admin.site.register(Profile, ProfileAdmin)