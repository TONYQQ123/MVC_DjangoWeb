# Generated by Django 5.0 on 2023-12-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserve', '0004_remove_rserve_gender_remove_rserve_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rserve',
            name='date',
            field=models.DateField(default='2023-1-1', null=True),
        ),
    ]