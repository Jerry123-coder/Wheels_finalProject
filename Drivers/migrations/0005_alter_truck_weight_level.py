# Generated by Django 4.1 on 2022-09-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drivers', '0004_truck_weight_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='weight_level',
            field=models.IntegerField(default=1),
        ),
    ]