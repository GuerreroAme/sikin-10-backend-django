# Generated by Django 4.2.14 on 2024-07-16 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=120, verbose_name='Nombre Usuario')),
                ('titulo', models.CharField(max_length=120, verbose_name='Título')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('area', models.CharField(max_length=120, verbose_name='Área')),
                ('descripcion', models.TextField(max_length=255, verbose_name='Descripción')),
                ('imagen', models.ImageField(upload_to='imagenes/logros', verbose_name='Imagen')),
            ],
            options={
                'db_table': 'logros',
            },
        ),
    ]
