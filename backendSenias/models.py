
from django.db import models

# Crear las clases o models correspondientes aqui
class Configuracion(models.Model):
    idioma_con = models.CharField(max_length=50)
    configuracionAudio_con = models.CharField(max_length=50)
    configuracionTexto_con = models.CharField(max_length=50)

    class Meta:
        db_table = 'configuracion'

class Usuario(models.Model):
    correo_usu = models.CharField(max_length=100)
    contrasenia_usu = models.CharField(max_length=100)
    fk_id_con = models.OneToOneField(Configuracion, on_delete=models.CASCADE)  #relacion uno a uno

    class Meta:
        db_table = 'usuario'

class Perfil(models.Model):
    nombre_per = models.CharField(max_length=100)
    descripcion_per = models.CharField(max_length=250)
    fk_id_usu = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'perfil'

class Feedback(models.Model):
    comentario_fee = models.CharField(max_length=250)
    calificacion_fee = models.IntegerField()  # para numeros enteros
    fecha_fee = models.DateTimeField()  # fecha y hora
    fk_id_usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)  #unno a muchos

    class Meta:
        db_table = 'feedback'

class Idioma(models.Model):
    nombre_idi = models.CharField(max_length=50)
    codigo_idi = models.CharField(max_length=20)

    class Meta:
        db_table = 'idioma'

class Traduccion(models.Model):
    texto_tra = models.TextField()
    fecha_tra = models.DateTimeField()
    fk_id_usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fk_id_idi = models.ManyToManyField(Idioma)

    class Meta:
        db_table = 'traduccion'

class Archivo(models.Model):
    nombre_arc = models.CharField(max_length=50)
    tipo_arc = models.CharField(max_length=50)
    ruta_arc = models.CharField(max_length=100)
    fk_id_tra = models.ForeignKey(Traduccion, on_delete=models.CASCADE)

    class Meta:
        db_table = 'archivo'

class Logs(models.Model):
    mensaje_log = models.TextField()
    fecha_log = models.DateTimeField()
    leido_log = models.BooleanField()
    fk_id_usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'logs'
