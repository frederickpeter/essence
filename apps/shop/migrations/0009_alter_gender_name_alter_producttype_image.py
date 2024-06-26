# Generated by Django 5.0.3 on 2024-04-01 21:17

import apps.utils.upload
import functools
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_producttype_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.CharField(choices=[('Men', "Men's"), ('Women', "Women's"), ('Kid', "Kids's")], default='Men', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='image',
            field=models.ImageField(help_text='Background image of product type - ideal resolution of 800x533', upload_to=functools.partial(apps.utils.upload.unique_file_name_generator, *(), **{'base_path': 'product-types'})),
        ),
    ]
