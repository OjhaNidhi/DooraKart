# Generated by Django 3.0.3 on 2020-04-15 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(db_column='category_id', primary_key=True, serialize=False)),
                ('category_name', models.CharField(db_column='category_name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ItemSubCategory',
            fields=[
                ('id', models.AutoField(db_column='sub_category_id', primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(max_length=100)),
                ('image_path', models.FileField(upload_to='images/')),
                ('category_id', models.ForeignKey(db_column='category_id', default=None, on_delete=django.db.models.deletion.CASCADE, to='Admin.ItemCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_upc', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('item_name', models.CharField(max_length=100)),
                ('brand', models.CharField(default=None, max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('price_per_unit', models.FloatField()),
                ('market_price', models.FloatField(default=0.0)),
                ('available_qty', models.IntegerField()),
                ('image_path', models.FileField(upload_to='images/')),
                ('item_description', models.TextField(default=None)),
                ('category_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Admin.ItemCategory')),
                ('sub_category_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Admin.ItemSubCategory')),
            ],
        ),
    ]
