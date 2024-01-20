from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'email', 'phone', 'city',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'phone', 'is_active', 'avatar')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
