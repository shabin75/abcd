from django.db import models


class EmployeeData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()



ob1=EmployeeData()
ob1.name='shabin'
ob1.age=27