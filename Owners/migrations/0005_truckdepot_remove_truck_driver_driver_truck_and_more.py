# Generated by Django 4.1 on 2022-09-05 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Owners', '0004_container_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='TruckDepot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=300)),
                ('long', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='truck',
            name='driver',
        ),
        migrations.AddField(
            model_name='driver',
            name='truck',
            field=models.ManyToManyField(to='Owners.truck'),
        ),
        migrations.AddField(
            model_name='driver',
            name='station',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Owners.truckdepot'),
        ),
    ]