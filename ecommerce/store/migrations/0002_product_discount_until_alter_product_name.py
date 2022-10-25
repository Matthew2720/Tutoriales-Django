# Generated by Django 4.1.2 on 2022-10-25 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="discount_until",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=20),
        ),
    ]
