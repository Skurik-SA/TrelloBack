from django.contrib import admin

from boards.models import Dashboard, DashboardArchive, Column, Card, Task, SubTasks, Marks, Mark


# Register your models here.

class DashboardArchiveInline(admin.StackedInline):
    model = DashboardArchive
    can_delete = False


class ColumnsInline(admin.TabularInline):
    model = Column
    can_delete = True


class MarksInline(admin.StackedInline):
    model = Marks
    can_delete = False


class MarkInline(admin.StackedInline):
    model = Mark
    can_delete = True


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    inlines = (DashboardArchiveInline, ColumnsInline, MarksInline)
    list_display = ('id', 'title', 'owner', 'is_private', 'is_favourite')
    list_filter = ('owner', 'is_private', 'is_favourite')
    search_fields = ('title', 'description')


@admin.register(DashboardArchive)
class DashboardArchiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'cards_archived_id', 'parent_dashboard')
    list_filter = ['id']
    search_fields = ['id']


@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    inlines = (MarkInline, )
    list_display = ('id',)
    list_filter = ['id']
    search_fields = ['id']


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'font_color', 'color', 'mark_text')
    list_filter = ['id']
    search_fields = ['id']


class CardsInline(admin.TabularInline):
    model = Card
    can_delete = True


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    inlines = (CardsInline,)
    list_display = ('id', 'title', 'position')
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'column', 'position', 'info', 'description', 'status', 'priority', 'card_marks', 'deadline',
                    'is_notifications', 'is_archived', 'color')
    list_filter = ['info']
    search_fields = ['info']


class SubTasksInline(admin.TabularInline):
    model = SubTasks
    can_delete = True


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = (SubTasksInline,)
    list_display = ('id', 'card', 'title', 'success_amount', 'total_amount')
    list_filter = ['title']
    search_fields = ['title']


@admin.register(SubTasks)
class SubTasks(admin.ModelAdmin):
    list_display = ('id', 'task', 'status', 'deadline')
    list_filter = ['task']
    search_fields = ['task']