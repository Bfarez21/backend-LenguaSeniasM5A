# implementacion de vistas para interactuar con nuestros modelos
# sirve para craer endpoint automaticamente

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from backendSenias.models import Usuario, Configuracion, Perfil, Feedback, Idioma, Traduccion, Archivo, \
    Logs  # importo todos los models/clases
from backendSenias.api.serializer import UsuarioSerializer, ConfiguracionSerializer, PerfilSerializer, \
    FeedbackSerializer, IdiomaSerializer, TraduccionSerializer, ArchivoSerializer, LogsSerializer


class UsuarioViewSet(viewsets.ModelViewSet):  # MOdelViewSet permitira crear nuestro crud
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    # Agregar una acción para obtener usuario por google_id
    @action(detail=False, methods=['get'], url_path='buscar/(?P<google_id>[^/.]+)')
    def buscar_por_google_id(self, request, google_id=None):
        try:
            usuario = Usuario.objects.get(google_id=google_id)
            serializer = self.get_serializer(usuario)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class IdiomaViewSet(viewsets.ModelViewSet):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer


class TraduccionViewSet(viewsets.ModelViewSet):
    queryset = Traduccion.objects.all()
    serializer_class = TraduccionSerializer


class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer


class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
