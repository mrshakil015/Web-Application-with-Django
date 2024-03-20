# Generated by Django 5.0.3 on 2024-03-19 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='badUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baduniversityname', models.CharField(max_length=100)),
                ('baduniversityid', models.CharField(max_length=100)),
                ('baduniversityaddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='goodUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gooduniversityname', models.CharField(max_length=100)),
                ('gooduniversityid', models.CharField(max_length=100)),
                ('gooduniversityaddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='internationalUniversiy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internationaluniversityname', models.CharField(max_length=100)),
                ('internationaluniversityid', models.CharField(max_length=100)),
                ('internationaluniversityaddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='universitylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universityname', models.CharField(max_length=100)),
                ('universityid', models.CharField(max_length=100)),
                ('universityaddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='universityStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universitystudentname', models.CharField(max_length=100)),
                ('universitystudentid', models.CharField(max_length=100)),
                ('universitystudentaddress', models.CharField(max_length=100)),
            ],
        ),
    ]