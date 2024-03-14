from django.contrib import admin
from .models import CustomUser, UserProfile
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    UserAdmin.fieldsets +=  (
        ("User Type", {
            'fields': (
                'role',
            ),
        }),
    )

    list_display=(
        'username', 'email', 'is_active', 'is_staff',
    )
    list_editable=(
        'is_active',
    )

admin.site.register(UserProfile)