# Generated by Django 3.2 on 2023-05-14 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20230514_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='return_due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 21, 18, 53, 42, 647147)),
        ),
    ]