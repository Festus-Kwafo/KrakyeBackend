# Generated by Django 3.1 on 2022-05-31 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220531_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='profile_picture',
            field=models.ImageField(blank=True, default='/userprofile/profile_default.png', upload_to='userprofile'),
        ),
    ]