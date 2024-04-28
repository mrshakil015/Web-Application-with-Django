# Generated by Django 5.0.4 on 2024-04-28 04:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrecipemodel',
            name='Create_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='addrecipemodel',
            name='CookingTime',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addrecipemodel',
            name='DifficultyLevel',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addrecipemodel',
            name='Ingredients',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='addrecipemodel',
            name='Instructions',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='addrecipemodel',
            name='NutritionalInformation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addrecipemodel',
            name='PreparationTime',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addrecipemodel',
            name='RecipeCategory',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addrecipemodel',
            name='RecipeTitle',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addrecipemodel',
            name='SampleImage',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
        migrations.AlterField(
            model_name='addrecipemodel',
            name='Tags',
            field=models.CharField(choices=[('Vegetrian', 'Vegetrian'), ('Non-Vegetrian', 'Non-Vegetrian')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addrecipemodel',
            name='TotalCalorie',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addrecipemodel',
            name='TotalTime',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
