# Generated by Django 5.1.1 on 2024-10-06 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_category_product_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descrition',
            new_name='description',
        ),
    ]
