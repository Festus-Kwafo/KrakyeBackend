# Generated by Django 3.1 on 2022-05-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=15)),
                ('time_slot', models.CharField(max_length=100)),
            ],
        ),
    ]