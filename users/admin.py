from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import CustomUser, ArtistProfile, OrganizerProfile


@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ['email', 'user_type']
    
@admin.register(ArtistProfile)    
class ArtistAdmin(ModelAdmin):
    list_display = ['user', 'stage_name', 'genre']

@admin.register(OrganizerProfile)
class OrganizerAdmin(ModelAdmin):
    list_display = ['company_name', 'user', 'description']
