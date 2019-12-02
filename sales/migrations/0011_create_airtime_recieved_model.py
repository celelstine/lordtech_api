# Generated by Django 2.2.7 on 2019-12-02 08:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0010_rename_isactive_to_isclosed__salesrepsub'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirtimeRecieved',
            fields=[
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField()),
                ('is_closed', models.BooleanField(default=False)),
                ('sales_rep', models.ForeignKey(limit_choices_to={'category': 'da'}, on_delete=django.db.models.deletion.CASCADE, to='sales.SalesRep')),
            ],
            options={
                'verbose_name': 'Airtime Recieved',
                'verbose_name_plural': 'Airtime Recieved',
            },
        ),
    ]
