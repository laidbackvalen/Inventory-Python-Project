# Generated by Django 2.2.2 on 2019-07-09 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'approval',
            },
        ),
    ]