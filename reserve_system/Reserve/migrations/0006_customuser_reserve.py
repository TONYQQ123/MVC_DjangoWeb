# Generated by Django 5.0 on 2023-12-23 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserve', '0005_alter_rserve_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='reserve',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Reserve.rserve'),
        ),
    ]
