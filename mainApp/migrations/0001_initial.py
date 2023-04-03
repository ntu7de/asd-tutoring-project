# Generated by Django 4.1.6 on 2023-04-03 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('subject', models.CharField(default='', max_length=100)),
                ('catalognumber', models.CharField(default='', max_length=100)),
                ('classsection', models.CharField(default='', max_length=100)),
                ('classnumber', models.CharField(default='', max_length=100, primary_key=True, serialize=False, unique=True)),
                ('classname', models.CharField(default='', max_length=100)),
                ('instructor', models.CharField(default='', max_length=200)),
                ('body', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='tutorClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.classes')),
                ('tutor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourly_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('monday_start', models.CharField(blank=True, choices=[('Select Time', 'Select Time'), ('9:00 AM', '9:00 AM'), ('9:30 AM', '9:30 AM'), ('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'), ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'), ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('1:00 PM', '1:00 PM'), ('1:30 PM', '1:30 PM'), ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'), ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'), ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM'), ('5:00 PM', '5:00 PM'), ('5:30 PM', '5:30 PM'), ('6:00 PM', '6:00 PM'), ('6:30 PM', '6:30 PM'), ('7:00 PM', '7:00 PM'), ('7:30 PM', '7:30 PM'), ('8:00 PM', '8:00 PM')], max_length=100, null=True)),
                ('monday_end', models.CharField(blank=True, choices=[('Select Time', 'Select Time'), ('9:00 AM', '9:00 AM'), ('9:30 AM', '9:30 AM'), ('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'), ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'), ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('1:00 PM', '1:00 PM'), ('1:30 PM', '1:30 PM'), ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'), ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'), ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM'), ('5:00 PM', '5:00 PM'), ('5:30 PM', '5:30 PM'), ('6:00 PM', '6:00 PM'), ('6:30 PM', '6:30 PM'), ('7:00 PM', '7:00 PM'), ('7:30 PM', '7:30 PM'), ('8:00 PM', '8:00 PM')], max_length=100, null=True)),
                ('tuesday_start', models.CharField(blank=True, choices=[('Select Time', 'Select Time'), ('9:00 AM', '9:00 AM'), ('9:30 AM', '9:30 AM'), ('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'), ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'), ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('1:00 PM', '1:00 PM'), ('1:30 PM', '1:30 PM'), ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'), ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'), ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM'), ('5:00 PM', '5:00 PM'), ('5:30 PM', '5:30 PM'), ('6:00 PM', '6:00 PM'), ('6:30 PM', '6:30 PM'), ('7:00 PM', '7:00 PM'), ('7:30 PM', '7:30 PM'), ('8:00 PM', '8:00 PM')], max_length=100, null=True)),
                ('tuesday_end', models.CharField(blank=True, choices=[('Select Time', 'Select Time'), ('9:00 AM', '9:00 AM'), ('9:30 AM', '9:30 AM'), ('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'), ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'), ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('1:00 PM', '1:00 PM'), ('1:30 PM', '1:30 PM'), ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'), ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'), ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM'), ('5:00 PM', '5:00 PM'), ('5:30 PM', '5:30 PM'), ('6:00 PM', '6:00 PM'), ('6:30 PM', '6:30 PM'), ('7:00 PM', '7:00 PM'), ('7:30 PM', '7:30 PM'), ('8:00 PM', '8:00 PM')], max_length=100, null=True)),
                ('wednesday_start', models.CharField(blank=True, choices=[('Select Time', 'Select Time'), ('9:00 AM', '9:00 AM'), ('9:30 AM', '9:30 AM'), ('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'), ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'), ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('1:00 PM', '1:00 PM'), ('1:30 PM', '1:30 PM'), ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'), ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'), ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM'), ('5:00 PM', '5:00 PM'), ('5:30 PM', '5:30 PM'), ('6:00 PM', '6:00 PM'), ('6:30 PM', '6:30 PM'), ('7:00 PM', '7:00 PM'), ('7:30 PM', '7:30 PM'), ('8:00 PM', '8:00 PM')], max_length=100, null=True)),
                ('wednesday_end', models.CharField(blank=True, choices=[('Select Time', 'Select Time'), ('9:00 AM', '9:00 AM'), ('9:30 AM', '9:30 AM'), ('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'), ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'), ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('1:00 PM', '1:00 PM'), ('1:30 PM', '1:30 PM'), ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'), ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'), ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM'), ('5:00 PM', '5:00 PM'), ('5:30 PM', '5:30 PM'), ('6:00 PM', '6:00 PM'), ('6:30 PM', '6:30 PM'), ('7:00 PM', '7:00 PM'), ('7:30 PM', '7:30 PM'), ('8:00 PM', '8:00 PM')], max_length=100, null=True)),
                ('thursday_start', models.CharField(blank=True, choices=[('Select Time', 'Select Time'), ('9:00 AM', '9:00 AM'), ('9:30 AM', '9:30 AM'), ('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'), ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'), ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('1:00 PM', '1:00 PM'), ('1:30 PM', '1:30 PM'), ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'), ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'), ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM'), ('5:00 PM', '5:00 PM'), ('5:30 PM', '5:30 PM'), ('6:00 PM', '6:00 PM'), ('6:30 PM', '6:30 PM'), ('7:00 PM', '7:00 PM'), ('7:30 PM', '7:30 PM'), ('8:00 PM', '8:00 PM')], max_length=100, null=True)),
                ('thursday_end', models.CharField(blank=True, choices=[('Select Time', 'Select Time'), ('9:00 AM', '9:00 AM'), ('9:30 AM', '9:30 AM'), ('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'), ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'), ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('1:00 PM', '1:00 PM'), ('1:30 PM', '1:30 PM'), ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'), ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'), ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM'), ('5:00 PM', '5:00 PM'), ('5:30 PM', '5:30 PM'), ('6:00 PM', '6:00 PM'), ('6:30 PM', '6:30 PM'), ('7:00 PM', '7:00 PM'), ('7:30 PM', '7:30 PM'), ('8:00 PM', '8:00 PM')], max_length=100, null=True)),
                ('friday_start', models.CharField(blank=True, choices=[('Select Time', 'Select Time'), ('9:00 AM', '9:00 AM'), ('9:30 AM', '9:30 AM'), ('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'), ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'), ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('1:00 PM', '1:00 PM'), ('1:30 PM', '1:30 PM'), ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'), ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'), ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM'), ('5:00 PM', '5:00 PM'), ('5:30 PM', '5:30 PM'), ('6:00 PM', '6:00 PM'), ('6:30 PM', '6:30 PM'), ('7:00 PM', '7:00 PM'), ('7:30 PM', '7:30 PM'), ('8:00 PM', '8:00 PM')], max_length=100, null=True)),
                ('friday_end', models.CharField(blank=True, choices=[('Select Time', 'Select Time'), ('9:00 AM', '9:00 AM'), ('9:30 AM', '9:30 AM'), ('10:00 AM', '10:00 AM'), ('10:30 AM', '10:30 AM'), ('11:00 AM', '11:00 AM'), ('11:30 AM', '11:30 AM'), ('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('1:00 PM', '1:00 PM'), ('1:30 PM', '1:30 PM'), ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'), ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'), ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM'), ('5:00 PM', '5:00 PM'), ('5:30 PM', '5:30 PM'), ('6:00 PM', '6:00 PM'), ('6:30 PM', '6:30 PM'), ('7:00 PM', '7:00 PM'), ('7:30 PM', '7:30 PM'), ('8:00 PM', '8:00 PM')], max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('pronouns', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=100)),
                ('tutor_or_student', models.CharField(default='tutor', max_length=100)),
                ('fun_fact', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
