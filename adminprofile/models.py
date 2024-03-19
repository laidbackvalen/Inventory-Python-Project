from django.db import models

# Create your models here.
class returnmodel(models.Model):
    item_no = models.CharField(primary_key=True, max_length=1000)
    Condition = models.CharField(max_length=1000, blank=True)
    class Meta:
        db_table = "returnmodel"

class useradmin(models.Model):
    emailaddress = models.EmailField()
    password = models.CharField(max_length=500)
    Employee_Id = models.CharField(primary_key=True, max_length=500)
    name = models.CharField(max_length=500)
    class Meta:
        db_table = "useradmin"

class items(models.Model):
    Name = models.CharField(max_length= 10000,null=True)
    Description = models.TextField(blank=True,null=True)
    Type = models.CharField(max_length=1000, null=True)
    id = models.CharField(primary_key= True,max_length=1000)
    Bond_Id = models.CharField(max_length=1000,null=True)
    Date_Of_Order = models.DateField(null=True)
    Vendor = models.CharField(max_length=1000,blank=True, null=True)
    Purchase_Price_Per_Item = models.IntegerField(blank=True, null=True)
    Delivered_Date = models.DateField(null=True)
    Condition = models.CharField(max_length=1000,blank=True, null=True)
    Quantity = models.IntegerField(blank=True, null=True)
    Asset_Value = models.IntegerField(blank=True, null=True)
    Model = models.CharField(max_length=1000,blank=True,null=True)
    Vendor_No = models.CharField(max_length=1000,blank=True,null=True)
    Remarks = models.TextField(blank=True,null=True)
    Photograph = models.ImageField(blank=True,null=True)
    Date_Of_Upgrade = models.DateField(blank=True,null=True)
    In_use = models.BooleanField(blank=True,default=False,null=True)
    Replacement_Required = models.BooleanField(blank=True,default=False, null=True)
    Location = models.CharField(max_length=1000, blank=True,null=True)
    To_be_Discarded = models.BooleanField(blank=True,default=False, null=True)
    Loaned = models.BooleanField(blank=True,default=False, null=True)
    class Meta:
        db_table = "items"