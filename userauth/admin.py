from django.contrib import admin
from .models import User, Profile


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['ip', 'last_ip']
    list_display = ['username', 'email', 'user_type', 'is_active', 'is_verify', 'last_ip']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'city', 'country']


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
