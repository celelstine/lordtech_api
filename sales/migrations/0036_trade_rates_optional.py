# Generated by Django 3.0.5 on 2020-05-06 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0035_auto_20200504_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='buying_rate',
            field=models.FloatField(blank=True, null=True, verbose_name='Buying rate (Naira)'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='selling_rate',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Selling rate (Yuan)'),
        ),
    ]
