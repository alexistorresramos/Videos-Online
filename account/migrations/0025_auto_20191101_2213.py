# Generated by Django 2.2.5 on 2019-11-02 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_auto_20191030_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='created_at',
            new_name='purchase_date',
        ),
    ]
