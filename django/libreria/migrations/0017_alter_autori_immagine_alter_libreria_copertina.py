# Generated by Django 5.1.7 on 2025-05-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0016_remove_autori_libri_scritti_alter_libreria_autore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autori',
            name='immagine',
            field=models.ImageField(blank=True, null=True, upload_to='autori/'),
        ),
        migrations.AlterField(
            model_name='libreria',
            name='copertina',
            field=models.ImageField(blank=True, null=True, upload_to='copertine/'),
        ),
    ]
