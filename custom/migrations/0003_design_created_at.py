# Generated by Django 5.0.7 on 2024-08-03 17:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0002_remove_design_tshirt_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
