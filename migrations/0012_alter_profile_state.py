# Generated by Django 5.0.2 on 2024-04-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wnApp', '0011_alter_profile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, choices=[('GUJ', 'Gujarat'), ('M', 'Madhya Pradesh'), ('AS', 'Assam')], max_length=100),
        ),
    ]
