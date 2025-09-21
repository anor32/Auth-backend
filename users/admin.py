from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from users.models import Role

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    list_editable = ('role',)