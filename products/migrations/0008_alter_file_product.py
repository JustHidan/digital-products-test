# Generated by Django 5.1.1 on 2024-10-07 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_descrition_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='products.product', verbose_name='product'),
        ),
    ]
