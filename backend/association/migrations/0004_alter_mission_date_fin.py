# Generated by Django 4.1 on 2022-09-02 11:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0003_mission_date_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='date_fin',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]