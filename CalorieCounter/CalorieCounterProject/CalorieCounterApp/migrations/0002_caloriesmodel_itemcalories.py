# Generated by Django 5.0.6 on 2024-06-08 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalorieCounterApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='caloriesmodel',
            name='ItemCalories',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
