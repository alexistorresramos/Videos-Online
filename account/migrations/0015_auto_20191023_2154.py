# Generated by Django 2.2.5 on 2019-10-24 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20191022_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='buyers',
            field=models.ManyToManyField(related_name='video_buyers', to='account.Buyer'),
        ),
    ]
