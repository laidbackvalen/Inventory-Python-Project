from django.db import models

# Create your models here.

class Employee(models.Model):
    emailaddress = models.EmailField()
    password = models.CharField(max_length = 500)
    Employee_Id = models.CharField( primary_key=True, max_length=500)
    name = models.CharField(max_length = 500)
    class Meta:
        db_table = "Employee"