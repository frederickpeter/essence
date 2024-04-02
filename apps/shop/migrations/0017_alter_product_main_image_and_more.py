# Generated by Django 5.0.3 on 2024-04-02 10:46

import apps.utils.upload
import functools
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_product_main_image_product_secondary_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(upload_to=functools.partial(apps.utils.upload.unique_file_name_generator, *(), **{'base_path': 'product-images'})),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondary_image',
            field=models.ImageField(blank=True, null=True, upload_to=functools.partial(apps.utils.upload.unique_file_name_generator, *(), **{'base_path': 'product-images'})),
        ),
    ]
