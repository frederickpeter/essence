from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # the items to display in the table
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "is_active",
    )
    readonly_fields = ["last_login", "date_joined"]

    # fieldsets is the form for editing or viewing an entity
    # the first index of each tuple is the name of the section: ex. 'Personal Information', 'Role Status'
    fieldsets = (
        (
            "Peronal Information",
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "email", "password"),
            },
        ),
        (
            "Role Status",
            {
                "classes": ("wide",),
                "fields": ("is_staff", "is_superuser", "is_active"),
            },
        ),
        (
            "Permissions",
            {
                "classes": ("wide",),
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "Date Information",
            {
                "classes": ("wide",),
                "fields": ("last_login", "date_joined"),
            },
        ),
    )

    # add_fieldsets is the form for adding/creating a new entity
    # the first index of each tuple is the name of the section: ex. 'Personal Information', 'Role Status'
    add_fieldsets = (
        (
            "Peronal Information",
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Role Status",
            {
                "classes": ("wide",),
                "fields": ("is_staff", "is_superuser", "is_active"),
            },
        ),
        (
            "Permissions",
            {
                "classes": ("wide",),
                "fields": ("groups", "user_permissions"),
            },
        ),
    )

    # table should be ordered by first name
    ordering = ("first_name",)
    # search by email, firstname and lastname
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
