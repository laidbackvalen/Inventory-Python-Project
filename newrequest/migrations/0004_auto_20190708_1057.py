# Generated by Django 2.2.2 on 2019-07-08 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newrequest', '0003_auto_20190708_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newrequest',
            name='emp_id',
            field=models.CharField(max_length=500),
        ),
    ]
