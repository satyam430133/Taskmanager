# Generated by Django 5.0.4 on 2024-04-11 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagerApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskDetail',
        ),
        migrations.AddField(
            model_name='user',
            name='taskDetail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='TaskManagerApp.task'),
        ),
    ]
