# Generated by Django 5.0.2 on 2024-04-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wnApp', '0015_alter_profile_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('', 'Select Gender #new default option functionality :)'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
    ]
