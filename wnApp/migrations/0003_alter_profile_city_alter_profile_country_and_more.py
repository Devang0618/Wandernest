# Generated by Django 5.0.2 on 2024-04-16 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wnApp', '0002_city_country_alter_profile_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
