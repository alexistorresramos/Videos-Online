# Generated by Django 2.2.5 on 2019-10-24 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_buyer_video_stored'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='video_stored',
        ),
    ]
