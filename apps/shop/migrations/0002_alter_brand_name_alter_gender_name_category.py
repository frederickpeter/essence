# Generated by Django 5.0.3 on 2024-03-29 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.CharField(choices=[("Men's", "Men's"), ("Women's", "Women's"), ("Kid's", "Kids's")], default="Men's", max_length=10, unique=True),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='shop.gender')),
            ],
        ),
    ]