# Generated by Django 4.0.4 on 2022-05-17 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_manager', '0003_alter_todomodel_time_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='time_field',
        ),
    ]
