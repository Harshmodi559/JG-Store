# Generated by Django 4.0.4 on 2022-10-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_customer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
