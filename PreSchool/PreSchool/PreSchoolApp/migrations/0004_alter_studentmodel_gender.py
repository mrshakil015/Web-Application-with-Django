# Generated by Django 5.0.6 on 2024-05-26 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PreSchoolApp', '0003_remove_studentmodel_admissionnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='Gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100),
        ),
    ]
