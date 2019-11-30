from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    User,
    RefreshToken
)

admin.site.register(User, UserAdmin)


@admin.register(RefreshToken)
class RefreshTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'key', 'create_date', 'modify_date')
    readonly_fields = ('create_date', 'modify_date', 'key', 'user')
    search_fields = ['key', 'id']
