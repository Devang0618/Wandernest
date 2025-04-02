# Generated by Django 5.0.2 on 2024-04-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wnApp', '0010_alter_profile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, choices=[('IND', 'India'), ('US', 'United States'), ('AUS', 'Australia')], max_length=100),
        ),
    ]
