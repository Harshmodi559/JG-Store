# Generated by Django 4.0.4 on 2022-10-17 03:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_customer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 8, 51, 33, 670354)),
        ),
    ]
