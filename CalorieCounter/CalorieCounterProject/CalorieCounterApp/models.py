from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomeUserModel(AbstractUser):
    Name = models.CharField(max_length=100,null=True)
    Age = models.CharField(max_length=100,null=True)
    GENDER = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    Gender = models.CharField(choices=GENDER,max_length=100,null=True)
    Height = models.CharField(max_length=100,null=True)
    Weight = models.CharField(max_length=100,null=True)
    BMRCal = models.CharField(max_length=100,null=True)
    
class CaloriesModel(models.Model):
    CreateDate = models.DateField(null=True)
    ItemName = models.CharField(max_length=100,null=True)
    ItemCalories = models.CharField(max_length=100,null=True)
    CaloriesConsumed = models.CharField(max_length=100,null=True)
    MyUser = models.ForeignKey(CustomeUserModel, on_delete=models.CASCADE, null=True)
    
    
    
    
