# Generated by Django 3.2.18 on 2023-03-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_tutordb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutordb',
            name='rate',
            field=models.CharField(max_length=200),
        ),
    ]
