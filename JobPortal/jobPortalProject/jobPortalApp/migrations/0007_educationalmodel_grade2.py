# Generated by Django 5.0.4 on 2024-05-06 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobPortalApp', '0006_educationalmodel_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationalmodel',
            name='Grade2',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
    ]
