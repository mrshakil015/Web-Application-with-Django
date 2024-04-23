# Generated by Django 5.0.4 on 2024-04-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobPortalApp', '0003_custom_user_address_custom_user_blood_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='user_type',
            field=models.CharField(choices=[('recruiter', 'Recruiter'), ('seeker', 'JobSeekter')], max_length=100, null=True),
        ),
    ]
