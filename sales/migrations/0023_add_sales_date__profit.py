# Generated by Django 2.2.7 on 2019-12-14 20:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0022_rename_profit__product'),
    ]

    operations = [
        migrations.AddField(
            model_name='profit',
            name='sales_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
