from django.db import models

# Create your models here.
class approval(models.Model):
    item_no = models.CharField(max_length=1000)
    date = models.DateField(null= True)
    request_id = models.CharField(max_length=500)
    emp_id = models.CharField(max_length=500)
    class Meta:
        db_table = 'approval'