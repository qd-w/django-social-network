# Generated by Django 2.1.2 on 2018-10-31 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181031_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='siteuser',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
