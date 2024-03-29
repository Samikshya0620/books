# Generated by Django 4.1.4 on 2023-02-07 14:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_customer_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.", regex='^\\+?977?\\d{10}$')])),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
