# Generated by Django 5.1 on 2024-09-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_bid_delete_bids_alter_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(max_length=800),
        ),
    ]
