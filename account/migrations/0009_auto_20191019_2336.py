# Generated by Django 2.2.5 on 2019-10-20 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20191019_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to='account.Category', verbose_name='Category'),
        ),
    ]
