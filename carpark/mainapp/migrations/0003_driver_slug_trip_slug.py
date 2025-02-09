# Generated by Django 4.2.18 on 2025-01-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_car_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
