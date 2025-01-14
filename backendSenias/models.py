from django.db import models

# Crear las clases o models correspondientes aqui
class Usuario(models.Model):
    correo_usu = models.CharField(max_length=100)
    contrasenia_usu = models.CharField(max_length=100)
