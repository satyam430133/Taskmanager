# Generated by Django 5.0.4 on 2024-04-11 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagerApp', '0008_remove_task_tasktype_user_tasktype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='tasktype',
            new_name='taskss',
        ),
    ]
