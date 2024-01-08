from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from boards.models import Dashboard
from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import CustomUser, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class DashboardsInline(admin.TabularInline):
    model = Dashboard
    can_delete = True


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, DashboardsInline)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active", "id")
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

