# Generated by Django 5.1.1 on 2024-10-06 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_descrition_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='descrition',
            new_name='description',
        ),
    ]
