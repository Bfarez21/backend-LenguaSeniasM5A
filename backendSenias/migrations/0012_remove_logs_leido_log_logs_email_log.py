# Generated by Django 5.1.5 on 2025-02-17 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendSenias', '0011_partida_fk_id_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='leido_log',
        ),
        migrations.AddField(
            model_name='logs',
            name='email_log',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
