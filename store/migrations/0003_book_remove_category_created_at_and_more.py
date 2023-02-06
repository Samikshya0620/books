# Generated by Django 4.1.4 on 2023-02-05 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_payment_detail_booking_item_booking_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
                ('discount', models.DecimalField(decimal_places=5, max_digits=10)),
                ('review', models.TextField(blank=True, max_length=100, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='status',
        ),
        migrations.RemoveField(
            model_name='category',
            name='trending',
        ),
        migrations.AlterField(
            model_name='booking_detail',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='booking_detail',
            name='modified_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='booking_detail',
            name='payment_details_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET, to='store.payment_detail'),
        ),
        migrations.AlterField(
            model_name='booking_item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='booking_item',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='payment_detail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='payment_detail',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Book_Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.SET, to='store.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
        migrations.AlterField(
            model_name='booking_item',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.book'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
