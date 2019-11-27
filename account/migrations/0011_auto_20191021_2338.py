# Generated by Django 2.2.5 on 2019-10-22 03:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20191021_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videos_sold',
            old_name='videos_sold',
            new_name='videos_to_sell',
        ),
        migrations.AlterField(
            model_name='videos_sold',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
