# Generated by Django 5.0 on 2023-12-20 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_ordersdetails_orderdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitems',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
