# Generated by Django 5.0 on 2023-12-18 17:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_ordersdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersdetails',
            name='orderDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]