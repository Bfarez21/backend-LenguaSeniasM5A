# Generated by Django 5.1.4 on 2025-01-13 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo_usu', models.CharField(max_length=100)),
                ('contrasenia_usu', models.CharField(max_length=100)),
            ],
        ),
    ]
