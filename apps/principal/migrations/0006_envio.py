# Generated by Django 4.2.1 on 2023-06-26 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_delete_carritoitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
    ]
