
#nos servirá para convertir objeto modelo django a tipos de datos que se
# puede representar en formato JSON:

from rest_framework import serializers
from backendSenias.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  #interviene todos los campos