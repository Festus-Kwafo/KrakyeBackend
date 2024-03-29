# Generated by Django 3.2 on 2022-07-26 23:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20220721_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='ceremonial_event',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='regular_outfit',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='urban_outfit',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
