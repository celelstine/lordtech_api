# Generated by Django 2.2.7 on 2019-12-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_create_sales_rep_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='category',
            field=models.CharField(choices=[('da', 'Data'), ('gc', 'GIFTCARD'), ('all', 'all')], default='all', max_length=3),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='key',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='salesrep',
            name='category',
            field=models.CharField(choices=[('da', 'Data'), ('gc', 'GIFTCARD'), ('all', 'all')], default='all', max_length=2),
        ),
        migrations.AlterField(
            model_name='salesrep',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='configuration',
            unique_together={('category', 'key')},
        ),
        migrations.AlterUniqueTogether(
            name='salesrep',
            unique_together={('category', 'name')},
        ),
    ]