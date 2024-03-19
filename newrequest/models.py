from django.db import models
from signup.models import Employee
from adminprofile.models import items
from django.utils import timezone
# Create your models here.
class NewRequest(models.Model):
    qty = models.IntegerField(default=1)
    emp_id = models.CharField(max_length=500)
    item_name = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    request_id = models.CharField(primary_key=True, max_length=500)
    class Meta:
        db_table = "NewRequest"