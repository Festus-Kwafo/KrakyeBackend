# Generated by Django 4.0.3 on 2022-03-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
