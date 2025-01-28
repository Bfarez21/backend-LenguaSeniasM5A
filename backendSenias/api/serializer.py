from rest_framework import serializers
from backendSenias.models import (
    Usuario, Configuracion, Perfil, Feedback, Idioma, Traduccion, Archivo, Logs, Categoria, Gif
)  # Importo todos los modelos necesarios

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  # Incluye todos los campos del modelo

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

