# Generated by Django 3.2 on 2023-05-16 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20230516_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 20, 0, 10, 7, 540249)),
        ),
    ]