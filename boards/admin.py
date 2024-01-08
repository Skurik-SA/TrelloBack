from django.contrib import admin

from boards.models import Dashboard, DashboardArchive


# Register your models here.

class DashboardArchiveInline(admin.StackedInline):
    model = DashboardArchive
    can_delete = False


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    inlines = (DashboardArchiveInline,)
    list_display = ('id', 'title', 'owner', 'is_private', 'is_favourite')
    list_filter = ('owner', 'is_private', 'is_favourite')
    search_fields = ('title', 'description')


@admin.register(DashboardArchive)
class DashboardArchiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'cards_archived_id', 'parent_dashboard')
    list_filter = ['id']
    search_fields = ['id']