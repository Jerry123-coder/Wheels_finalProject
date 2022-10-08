# Generated by Django 4.1 on 2022-09-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0003_rename_shipping_address_transactionlog_pickup_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactionlog',
            old_name='amount',
            new_name='amount_BTC',
        ),
        migrations.RenameField(
            model_name='wallet',
            old_name='balance',
            new_name='balance_BTC',
        ),
        migrations.RemoveField(
            model_name='transactionlog',
            name='delivery_fee_ghc',
        ),
        migrations.AddField(
            model_name='transactionlog',
            name='delivery_fee_BTC',
            field=models.FloatField(default=1),
        ),
    ]