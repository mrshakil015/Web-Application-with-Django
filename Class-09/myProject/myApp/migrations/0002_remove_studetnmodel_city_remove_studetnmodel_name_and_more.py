# Generated by Django 5.0.3 on 2024-03-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studetnmodel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='studetnmodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='studetnmodel',
            name='rollno',
        ),
        migrations.AddField(
            model_name='studetnmodel',
            name='Department',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='studetnmodel',
            name='FirstName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='studetnmodel',
            name='LastName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='studetnmodel',
            name='City',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
