# Generated by Django 2.2.2 on 2019-07-02 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.CharField(max_length=500)),
                ('item_name', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]
