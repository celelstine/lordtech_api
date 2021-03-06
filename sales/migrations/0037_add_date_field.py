# Generated by Django 3.0.5 on 2020-05-07 10:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0036_trade_rates_optional'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashreceived',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='datasales',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='trade',
            name='sales_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tradesummary',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
