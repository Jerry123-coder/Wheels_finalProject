# Generated by Django 4.1 on 2022-09-10 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Drivers', '0009_delete_agent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='truck',
        ),
    ]