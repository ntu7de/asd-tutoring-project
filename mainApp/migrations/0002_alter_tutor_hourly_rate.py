# Generated by Django 4.1.6 on 2023-03-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='hourly_rate',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
