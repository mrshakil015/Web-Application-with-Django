# Generated by Django 5.0.3 on 2024-03-19 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_studentskill'),
    ]

    operations = [
        migrations.CreateModel(
            name='studenthobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbyname', models.CharField(max_length=100)),
                ('hobbyid', models.CharField(max_length=100)),
            ],
        ),
    ]
