# Generated by Django 2.2.2 on 2019-07-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminprofile', '0013_auto_20190705_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='In_use',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='items',
            name='Loaned',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='items',
            name='Replacement_Required',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='items',
            name='To_be_Discarded',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]