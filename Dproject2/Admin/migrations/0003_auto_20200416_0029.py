# Generated by Django 3.0.3 on 2020-04-15 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_auto_20200416_0025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_id',
            new_name='ItemId',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='sub_category_id',
            new_name='sub_category',
        ),
    ]