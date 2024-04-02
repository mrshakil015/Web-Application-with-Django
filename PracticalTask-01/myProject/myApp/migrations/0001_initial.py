# Generated by Django 5.0.3 on 2024-03-30 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('linkedin_profile', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('languages', models.CharField(max_length=50)),
                ('years_of_experience', models.CharField(max_length=50)),
            ],
        ),
    ]