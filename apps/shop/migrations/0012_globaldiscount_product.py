# Generated by Django 5.0.3 on 2024-04-02 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_gender_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]