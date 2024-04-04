# Generated by Django 5.0.4 on 2024-04-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('MEN', 'men'), ('WOMEN', 'women'), ('OTHER', 'other')], default=True, max_length=10)),
                ('salary', models.FloatField()),
                ('join_date', models.DateField(default=True)),
                ('address', models.CharField(max_length=20)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
