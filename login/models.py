from django.db import models

# Create your models here.

class Login(models.Model):
    emp_pas = models.CharField(max_length = 500)
    emp_id = models.CharField( primary_key=True, max_length=500)
    class Meta:
        db_table = "Login"