# Generated by Django 5.0.4 on 2024-05-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECommerceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecommerceuser',
            name='UserType',
            field=models.CharField(choices=[('Customer', 'Customer'), ('Seller', 'Seller')], max_length=100),
        ),
    ]
