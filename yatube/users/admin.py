from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'phone_number',
        'location',
        'birth_date',
        'is_staff'
    )
    search_fields = ('username',)
    list_filter = ('groups',)
    empty_value_display = '-пусто-'
