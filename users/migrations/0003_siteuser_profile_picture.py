# Generated by Django 2.1.2 on 2018-10-30 22:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_siteuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='profile_picture',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profile_pictures/'),
            preserve_default=False,
        ),
    ]
