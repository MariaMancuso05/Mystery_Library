# Generated by Django 5.1.7 on 2025-04-07 12:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0013_alter_cartafittizia_numero_della_carta'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='votazione',
            unique_together={('user', 'libro')},
        ),
    ]
