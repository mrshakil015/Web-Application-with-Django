from django.db import models

# Create your models here.
class infoModel(models.Model):
    Name=models.CharField(max_length=50)
    About=models.TextField()
    Address=models.CharField(max_length=250)
    Email=models.CharField(max_length=250)
    Mobile=models.CharField(max_length=250)
    Picture=models.ImageField(upload_to='media/images/')
    Summary=models.CharField(max_length=250)
    Degree=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)
    University=models.CharField(max_length=50)
    Session=models.CharField(max_length=50)
    WorkPlace=models.CharField(max_length=50)
    Designation=models.CharField(max_length=50)
    Duration=models.CharField(max_length=50)
    ProgrammingSkill=models.CharField(max_length=50)
    Other=models.CharField(max_length=50)
