# Generated by Django 3.0.3 on 2020-04-17 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_auto_20200417_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='brand',
            new_name='brand_name',
        ),
    ]
