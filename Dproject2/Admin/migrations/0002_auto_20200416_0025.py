# Generated by Django 3.0.3 on 2020-04-15 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemsubcategory',
            old_name='category_id',
            new_name='category',
        ),
    ]