from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ['username', 'email', 'user_type']
