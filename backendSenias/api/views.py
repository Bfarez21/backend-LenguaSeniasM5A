# implementacion de vistas para interactuar con nuestros modelos

from rest_framework import viewsets
from backendSenias.models import Usuario
from backendSenias.api.serializer import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):   # MOdelViewSet permitira crear nuestro crud
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
