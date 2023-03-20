# Generated by Django 3.2.18 on 2023-03-17 18:00

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
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourly_rate', models.IntegerField()),
                ('monday_hours', models.CharField(max_length=200)),
                ('tuesday_hours', models.CharField(max_length=200)),
                ('wednesday_hours', models.CharField(max_length=200)),
                ('thursday_hours', models.CharField(max_length=200)),
                ('friday_hours', models.CharField(max_length=200)),
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
                ('year', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('pronouns', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=100)),
                ('is_tutor', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('fun_fact', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('subject', models.CharField(default='', max_length=100)),
                ('catalognumber', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('classsection', models.CharField(default='', max_length=100)),
                ('classnumber', models.CharField(default='', max_length=100)),
                ('classname', models.CharField(default='', max_length=100)),
                ('instructor', models.CharField(default='', max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]