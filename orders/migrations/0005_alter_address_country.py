# Generated by Django 4.0.3 on 2022-04-10 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_id_alter_city_region_and_more'),
        ('orders', '0004_alter_address_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.country'),
        ),
    ]
