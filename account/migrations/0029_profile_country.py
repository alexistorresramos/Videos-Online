# Generated by Django 2.2.5 on 2019-11-08 14:24

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0028_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(default='US', max_length=2),
        ),
    ]
