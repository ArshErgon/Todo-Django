# Generated by Django 2.1.5 on 2019-02-11 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_todo_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TryModel',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]