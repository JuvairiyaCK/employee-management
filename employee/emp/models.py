from django.db import models

# Create your models here.

class EmpData(models.Model):
    ename=models.CharField(max_length=100,verbose_name="employee name")
    age=models.IntegerField()
    salary=models.IntegerField()
    designation=models.CharField(max_length=100)
