# implementacion de vistas para interactuar con nuestros modelos
#sirve para craer endpoint automaticamente

from rest_framework import viewsets
from backendSenias.models import Usuario,Configuracion,Perfil,Feedback,Idioma,Traduccion,Archivo,Logs  #importo todos los models/clases
from backendSenias.api.serializer import UsuarioSerializer,ConfiguracionSerializer,PerfilSerializer,FeedbackSerializer,IdiomaSerializer,TraduccionSerializer,ArchivoSerializer,LogsSerializer

class UsuarioViewSet(viewsets.ModelViewSet):   # MOdelViewSet permitira crear nuestro crud
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

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