# Generated by Django 4.1 on 2022-09-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0007_transactionlog_amount_ghs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='address',
            field=models.CharField(default='***', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance_BTC',
            field=models.FloatField(default=10),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='private_key',
            field=models.CharField(default='***', max_length=300),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='public_key',
            field=models.CharField(default='***', max_length=300),
        ),
    ]
