# Generated by Django 5.0.2 on 2024-04-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wnApp', '0017_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, choices=[('', 'Select City'), ('AHM', 'AHM'), ('GN', 'Gandhinagar'), ('MEH', 'Mehsana')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, choices=[('', 'Select State'), ('GUJ', 'GUJ'), ('M', 'Madhya Pradesh'), ('AS', 'Assam')], max_length=100),
        ),
    ]
