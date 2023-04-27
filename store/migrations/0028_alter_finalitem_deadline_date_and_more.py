# Generated by Django 4.1.4 on 2023-03-25 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalitem',
            name='deadline_date',
            field=models.DateField(default=datetime.date(2023, 4, 25)),
        ),
        migrations.AlterField(
            model_name='owner',
            name='contactnumber',
            field=models.CharField(max_length=14),
        ),
    ]
