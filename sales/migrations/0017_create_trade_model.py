# Generated by Django 2.2.7 on 2019-12-10 21:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0016_add_data_balance_to_sales_rep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('group', models.CharField(blank=True, max_length=50, null=True)),
                ('selling_rate', models.PositiveIntegerField(verbose_name='Selling rate (Yuan)')),
                ('buying_rate', models.PositiveIntegerField(verbose_name='Buying rate (Naira)')),
                ('amount', models.PositiveIntegerField()),
                ('amount_paid', models.PositiveIntegerField()),
                ('is_closed', models.BooleanField(default=False)),
                ('card', models.ForeignKey(limit_choices_to={'category': 'gc'}, on_delete=django.db.models.deletion.CASCADE, related_name='trades', to='sales.Product')),
                ('sales_rep', models.ForeignKey(limit_choices_to={'category': 'gc'}, on_delete=django.db.models.deletion.CASCADE, related_name='trades', to='sales.SalesRep')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]