# Generated by Django 2.2.5 on 2019-10-31 02:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_auto_20191030_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='book',
            name='incident_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='cart',
            name='incident_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='news',
            name='incident_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='news',
            name='purchase_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
