import uuid

from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser


# Create your models here.

class Dashboard(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_dashboards')
    participants = models.ManyToManyField(CustomUser, related_name='participant_dashboards', blank=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    marks = models.OneToOneField('Marks', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='marks')

    is_private = models.BooleanField(default=True, blank=True, null=True)
    is_favourite = models.BooleanField(default=False, blank=True, null=True)
    users_can_edit = ArrayField(models.IntegerField(blank=True, null=True), blank=True, null=True)
    users_can_view = ArrayField(models.IntegerField(blank=True, null=True), blank=True, null=True)
    users_can_comment = ArrayField(models.IntegerField(blank=True, null=True), blank=True, null=True)


class DashboardArchive(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    cards_archived_id = ArrayField(models.IntegerField(blank=True, null=True), blank=True, null=True)
    parent_dashboard = models.OneToOneField('Dashboard', null=True, blank=True, on_delete=models.CASCADE,
                                            related_name='archive')


@receiver(post_save, sender=Dashboard)
def create_dashboard_archive(sender, instance, created, **kwargs):
    if created:
        created_archive = DashboardArchive.objects.create(parent_dashboard=instance)
        sender.dashboard_archive = created_archive


@receiver(post_save, sender=Dashboard)
def create_marks(sender, instance, created, **kwargs):
    if created:
        created_marks = Marks.objects.create(dashboard=instance)
        sender.marks = created_marks


class Column(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='columns')
    title = models.TextField(blank=True, null=True)
    position = models.IntegerField(unique=True, blank=True, null=True)


class Marks(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    dashboard = models.OneToOneField(Dashboard, null=True, blank=True, on_delete=models.CASCADE,
                                     related_name='dashboard_marks')


class Mark(models.Model):
    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False)
    font_color = models.CharField(default="#000000")
    color = models.CharField(blank=True, null=True)
    mark_text = models.CharField(max_length=255, blank=True, null=True)
    parent_marks = models.ForeignKey(Marks, related_name='my_marks', on_delete=models.CASCADE)


class Card(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='cards')
    position = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    priority = models.CharField(blank=True, null=True)
    card_marks = ArrayField(models.CharField(blank=True, null=True), blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_notifications = models.BooleanField(default=False, blank=True, null=True)
    is_archived = models.BooleanField(default=False, blank=True, null=True)
    color = models.CharField(blank=True, null=True)


class Task(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='tasks')
    title = models.TextField(default="", blank=True, null=True)
    success_amount = models.IntegerField(default=0, blank=True, null=True)
    total_amount = models.IntegerField(default=0, blank=True, null=True)


class SubTasks(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='sub_tasks')
    title = models.TextField(default="", blank=True, null=True)
    status = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True, null=True)
