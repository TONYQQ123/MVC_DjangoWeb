# Generated by Django 5.0 on 2023-12-22 11:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reserve', '0002_coustomuser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoustomUser',
            new_name='CustomUser',
        ),
    ]
