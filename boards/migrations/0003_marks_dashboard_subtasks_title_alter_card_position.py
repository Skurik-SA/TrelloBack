# Generated by Django 5.0 on 2024-01-25 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='dashboard',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_marks', to='boards.dashboard'),
        ),
        migrations.AddField(
            model_name='subtasks',
            name='title',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='position',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
