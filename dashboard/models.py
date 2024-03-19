from django.db import models

# Create your models here.
class quer(models.Model):
    item_no = models.CharField(max_length=500)
    class Meta:
        db_table = 'quer'

class quer1(models.Model):
    name2 =  models.CharField(max_length= 1000)
    id2 = models.CharField(max_length=1000)
    bond2 = models.CharField(max_length=1000)
    type2 =  models.CharField(max_length=1000)
    class Meta:
        db_table = 'quer1'