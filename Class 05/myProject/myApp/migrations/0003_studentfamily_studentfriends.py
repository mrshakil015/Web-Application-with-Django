# Generated by Django 5.0.3 on 2024-03-19 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_classmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentfamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentaddress', models.CharField(max_length=100)),
                ('studentid', models.CharField(max_length=100)),
                ('studentfather', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='studentfriends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendsname', models.CharField(max_length=100)),
                ('friendid', models.CharField(max_length=100)),
                ('friendaddress', models.CharField(max_length=100)),
            ],
        ),
    ]