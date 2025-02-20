from django.apps import AppConfig


class BackendseniasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backendSenias'
#Creacion de un juego con niveles por defecto al iniciar la API
    def ready(self):
        from .models import Juego, Nivel
        if not Juego.objects.filter(nombre_juego='Adivina la seña').exists():
            # Crear el juego
            nuevo_juego, created = Juego.objects.get_or_create(
                id=1,
                nombre_juego='Adivina la seña',
                defaults={'descripcion_jue': 'Adivina la seña mediante gifs con múltiples opciones'}
            )

            if created:
                niveles = [
                    {'id': 1, 'dificultad_nivel': 'Fácil', 'descripcion_nivel': 'Señas con números y letras'},
                    {'id': 2, 'dificultad_nivel': 'Medio', 'descripcion_nivel': 'Señas de colores y familia'},
                    {'id': 3, 'dificultad_nivel': 'Difícil', 'descripcion_nivel': 'Aprende imitando las señas'},
                ]

                for nivel in niveles:
                    Nivel.objects.create(
                        id=nivel['id'],
                        dificultad_nivel=nivel['dificultad_nivel'],
                        descripcion_nivel=nivel['descripcion_nivel'],
                        FK_id_juego=nuevo_juego
                    )