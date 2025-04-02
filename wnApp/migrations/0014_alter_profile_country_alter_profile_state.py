# Generated by Django 5.0.2 on 2024-04-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wnApp', '0013_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, choices=[('', 'Select Country'), ('IND', 'India'), ('US', 'United States'), ('AUS', 'Australia')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, choices=[('', 'Select State'), ('GUJ', 'Gujarat'), ('M', 'Madhya Pradesh'), ('AS', 'Assam')], max_length=100),
        ),
    ]
