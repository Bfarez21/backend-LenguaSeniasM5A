from django.contrib.postgres import serializers
#nos servirá para convertir objeto modelo django a tipos de datos que se
# puede representar en formato JSON:
from django.conf import settings
from rest_framework import serializers
from backendSenias.models import Usuario,Configuracion,Perfil,Feedback,Idioma,Traduccion,Modelo,Archivo,Logs,Categoria,Gif, Partida, Juego, Nivel, Puntaje #importo todos los models/clases

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  #interviene todos los campos

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = '__all__'

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'

class TraduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traduccion
        fields = '__all__'


class ModeloSerializer(serializers.ModelSerializer):
    model_url = serializers.SerializerMethodField()
    metadata_url = serializers.SerializerMethodField()
    weights_url = serializers.SerializerMethodField()

    class Meta:
        model = Modelo
        fields = ['id', 'nombre', 'descripcion', 'fecha_ingreso',
                  'model_file', 'metadata_file', 'weights_file',
                  'model_url', 'metadata_url', 'weights_url']

    def get_model_url(self, obj):
        if obj.model_file:
            return f"{settings.MEDIA_URL}{obj.model_file.name}"
        return None

    def get_metadata_url(self, obj):
        if obj.metadata_file:
            return f"{settings.MEDIA_URL}{obj.metadata_file.name}"
        return None

    def get_weights_url(self, obj):
        if obj.weights_file:
            return f"{settings.MEDIA_URL}{obj.weights_file.name}"
        return None

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields = '__all__'

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class GifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gif
        fields = ['id', 'nombre', 'archivo', 'categoria']

# Serializer para el modelo Juego
class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['id', 'nombre_juego', 'descripcion_jue']

# Serializer para el modelo Nivel
class NivelSerializer(serializers.ModelSerializer):
    FK_id_juego = serializers.PrimaryKeyRelatedField(queryset=Juego.objects.all())

    class Meta:
        model = Nivel
        fields = ['id', 'dificultad_nivel', 'descripcion_nivel', 'FK_id_juego']

# Serializer para el modelo Partida
class PartidaSerializer(serializers.ModelSerializer):
    FK_id_usuario = serializers.StringRelatedField()  # Esto muestra el nombre de usuario
    FK_id_juego = JuegoSerializer()  # Relacionamos con el modelo Juego

    class Meta:
        model = Partida
        fields = ['id', 'fecha_inicio', 'fecha_fin', 'resultado', 'FK_id_usuario', 'FK_id_juego']

# Serializer para el modelo Puntaje
class PuntajeSerializer(serializers.ModelSerializer):
    FK_id_usuario = serializers.StringRelatedField()  # Muestra el nombre del usuario
    FK_id_nivel = NivelSerializer()  # Relacionamos con el modelo Nivel

    class Meta:
        model = Puntaje
        fields = ['id', 'puntaje_obtenido', 'fecha_ob_puntaje', 'FK_id_usuario', 'FK_id_nivel']