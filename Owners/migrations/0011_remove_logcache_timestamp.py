# Generated by Django 4.1 on 2022-09-24 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Owners', '0010_remove_owner_date_joined_remove_owner_lat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logcache',
            name='timestamp',
        ),
    ]
