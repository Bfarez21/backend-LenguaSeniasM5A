
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma_con', models.CharField(max_length=50)),
                ('configuracionAudio_con', models.CharField(max_length=50)),
                ('configuracionTexto_con', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'configuracion',
            },
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_idi', models.CharField(max_length=50)),
                ('codigo_idi', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'idioma',
            },
        ),
        migrations.CreateModel(
            name='Traduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_tra', models.TextField()),
                ('fecha_tra', models.DateTimeField()),
                ('fk_id_idi', models.ManyToManyField(to='backendSenias.idioma')),
            ],
            options={
                'db_table': 'traduccion',
            },
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_arc', models.CharField(max_length=50)),
                ('tipo_arc', models.CharField(max_length=50)),
                ('ruta_arc', models.CharField(max_length=100)),
                ('fk_id_tra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendSenias.traduccion')),
            ],
            options={
                'db_table': 'archivo',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo_usu', models.CharField(max_length=100)),
                ('contrasenia_usu', models.CharField(max_length=100)),
                ('fk_id_con', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backendSenias.configuracion')),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.AddField(
            model_name='traduccion',
            name='fk_id_usu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendSenias.usuario'),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_per', models.CharField(max_length=100)),
                ('descripcion_per', models.CharField(max_length=250)),
                ('fk_id_usu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backendSenias.usuario')),
            ],
            options={
                'db_table': 'perfil',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje_log', models.TextField()),
                ('fecha_log', models.DateTimeField()),
                ('leido_log', models.BooleanField()),
                ('fk_id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendSenias.usuario')),
            ],
            options={
                'db_table': 'logs',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario_fee', models.CharField(max_length=250)),
                ('calificacion_fee', models.IntegerField()),
                ('fecha_fee', models.DateTimeField()),
                ('fk_id_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendSenias.usuario')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]
