# Generated by Django 5.1.6 on 2025-02-24 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='imagen',
            field=models.ImageField(upload_to='media/denuncias-imgs', verbose_name='Imagen'),
        ),
    ]
