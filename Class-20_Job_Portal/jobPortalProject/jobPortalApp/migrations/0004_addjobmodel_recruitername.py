# Generated by Django 5.0.4 on 2024-04-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobPortalApp', '0003_alter_addjobmodel_companyname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addjobmodel',
            name='RecruiterName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]