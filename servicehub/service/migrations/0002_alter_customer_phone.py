# Generated by Django 5.1.1 on 2024-10-16 08:45

import service.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=100, validators=[service.models.validate_phone_number]),
        ),
    ]
