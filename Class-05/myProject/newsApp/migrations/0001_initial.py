# Generated by Django 5.0.3 on 2024-03-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='badNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badnewsname', models.CharField(max_length=100)),
                ('badnewsid', models.CharField(max_length=100)),
                ('badnewsaddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='blogNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blognewstitle', models.CharField(max_length=100)),
                ('blognewsid', models.CharField(max_length=100)),
                ('blognewsdetails', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='goodNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodnewsname', models.CharField(max_length=100)),
                ('goodnewsid', models.CharField(max_length=100)),
                ('goodnewsaddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='internationalNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internationalnewsname', models.CharField(max_length=100)),
                ('internationalnewsid', models.CharField(max_length=100)),
                ('internationalnewsaddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='newslist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsname', models.CharField(max_length=100)),
                ('newsid', models.CharField(max_length=100)),
                ('newsaddress', models.CharField(max_length=100)),
            ],
        ),
    ]
