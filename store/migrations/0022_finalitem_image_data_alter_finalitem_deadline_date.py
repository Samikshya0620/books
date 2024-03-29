# Generated by Django 4.1.6 on 2023-03-09 18:37

import datetime
from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_remove_finalitem_image_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalitem',
            name='image_data',
            field=models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path),
        ),
        migrations.AlterField(
            model_name='finalitem',
            name='deadline_date',
            field=models.DateField(default=datetime.date(2023, 4, 9)),
        ),
    ]
