# Generated by Django 3.2.4 on 2021-07-06 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('rut', models.CharField(max_length=9)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
                ('genero', models.CharField(max_length=10)),
                ('instrumento', models.CharField(max_length=10)),
                ('comuna', models.CharField(max_length=15)),
                ('comentarios', models.CharField(max_length=200)),
            ],
        ),
    ]
