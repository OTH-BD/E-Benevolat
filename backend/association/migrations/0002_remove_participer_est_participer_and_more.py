# Generated by Django 4.1 on 2022-08-29 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participer',
            name='est_participer',
        ),
        migrations.AddField(
            model_name='participer',
            name='participer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='association.mission'),
        ),
    ]