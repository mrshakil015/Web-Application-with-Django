# Generated by Django 5.0.4 on 2024-05-02 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobPortalApp', '0006_jobrecruiterprofile_jobseekerprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobrecruiterprofile',
            old_name='skills',
            new_name='company_address',
        ),
        migrations.RenameField(
            model_name='jobrecruiterprofile',
            old_name='work_experience',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='jobseekerprofile',
            old_name='company_address',
            new_name='skills',
        ),
        migrations.RenameField(
            model_name='jobseekerprofile',
            old_name='company_name',
            new_name='work_experience',
        ),
    ]
