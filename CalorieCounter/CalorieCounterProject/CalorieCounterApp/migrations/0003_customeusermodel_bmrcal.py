# Generated by Django 5.0.6 on 2024-06-08 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalorieCounterApp', '0002_caloriesmodel_itemcalories'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeusermodel',
            name='BMRCal',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
