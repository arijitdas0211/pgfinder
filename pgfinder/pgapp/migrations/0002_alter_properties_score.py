# Generated by Django 4.1.10 on 2023-11-15 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pgapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='score',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pgapp.rating'),
        ),
    ]
