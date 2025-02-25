
from django.db import models
from django.core.validators import FileExtensionValidator
# Crear las clases o models correspondientes aqui
class Configuracion(models.Model):
    idioma_con = models.CharField(max_length=50)
    configuracionAudio_con = models.CharField(max_length=50)
    configuracionTexto_con = models.CharField(max_length=50)

    class Meta:
        db_table = 'configuracion'

class Usuario(models.Model):
    google_id = models.CharField(max_length=255, unique=True, null=False)
    fk_id_con = models.OneToOneField(Configuracion, on_delete=models.CASCADE, null=True)  #relacion uno a uno

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

class Modelo(models.Model):
    nombre = models.CharField(max_length=100, default="modelos")
    descripcion = models.TextField(blank=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    model_file = models.FileField(upload_to='modelos', default='model_file.json')
    weights_file = models.FileField(upload_to='modelos', default='weights_file.bin')
    metadata_file = models.FileField(upload_to='modelos', default='default_metadata_file.json')  # Valor por defecto

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"

    def __str__(self):
        return self.nombre


class Traduccion(models.Model):
    texto_tra = models.TextField()
    fecha_tra = models.DateTimeField()
    fk_id_usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fk_id_idi = models.ManyToManyField(Idioma)
    # Relación con el modelo Modelo a través de una clave foránea
    fk_id_modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, default=1)

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
    email_log = models.CharField(max_length=150, null=True)
    fk_id_usu = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'logs'

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre


class Gif(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='gifs/')  # FileField to store the uploaded file
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='gifs')

    class Meta:
        db_table = 'gif'

    def __str__(self):
        return self.nombre


class Juego(models.Model):
    nombre_juego = models.CharField(max_length=255)
    descripcion_jue = models.TextField()

    def __str__(self):
        return self.nombre_juego

class Nivel(models.Model):
    dificultad_nivel = models.CharField(max_length=50)
    descripcion_nivel = models.TextField()
    FK_id_juego = models.ForeignKey(Juego, related_name='niveles', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dificultad_nivel} - {self.FK_id_juego.nombre_juego}"

class Partida(models.Model):
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(auto_now=True)  # Fecha de fin se actualiza automáticamente en cada guardado
    resultado = models.IntegerField()
    FK_id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    FK_id_juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    FK_id_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, null=True, default=1)


    def __str__(self):
        return f"Partida {self.id} - {self.FK_id_usuario.google_id}"

class Puntaje(models.Model):
    puntaje_obtenido = models.IntegerField()
    fecha_ob_puntaje = models.DateTimeField(auto_now_add=True)
    FK_id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    FK_id_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Puntaje de {self.FK_id_usuario.google_id} - {self.puntaje_obtenido} puntos"

class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='historial')  # Relación con Usuario
    gif = models.ForeignKey(Gif, on_delete=models.CASCADE, related_name='historial_gif')       # Relación con Gif
    fecha_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'historial'
        ordering = ['-fecha_hora']