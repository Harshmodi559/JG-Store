# Generated by Django 4.0.4 on 2022-10-18 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_customer_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='d',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 14, 30, 22, 311375)),
        ),
    ]
