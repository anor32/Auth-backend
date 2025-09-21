from django.contrib import admin

from users.models import Role,User

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ( 'email', 'role','first_name','is_active')
    list_editable = ('role',)
