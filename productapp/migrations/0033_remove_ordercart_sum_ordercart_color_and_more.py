# Generated by Django 5.0.7 on 2024-09-11 16:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0032_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordercart',
            name='sum',
        ),
        migrations.AddField(
            model_name='ordercart',
            name='color',
            field=models.CharField(default=django.utils.timezone.now, max_length=225),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordercart',
            name='product_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordercart',
            name='size',
            field=models.CharField(default=django.utils.timezone.now, max_length=225),
            preserve_default=False,
        ),
    ]