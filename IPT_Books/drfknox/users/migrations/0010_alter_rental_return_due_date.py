# Generated by Django 3.2 on 2023-05-14 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_rental_return_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='return_due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 21, 19, 30, 31, 799418)),
        ),
    ]