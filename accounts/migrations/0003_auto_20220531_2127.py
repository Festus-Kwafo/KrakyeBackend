# Generated by Django 3.1 on 2022-05-31 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220526_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='profile_picture',
            field=models.ImageField(blank=True, default='/static/images/profile.png', upload_to='userprofile'),
        ),
    ]