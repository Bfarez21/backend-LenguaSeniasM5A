# implementacion de vistas para interactuar con nuestros modelos
# sirve para craer endpoint automaticamente

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from backendSenias.models import Usuario, Configuracion, Perfil, Feedback, Idioma, Traduccion, Modelo, Archivo, Logs, Categoria, \
    Gif  # importo todos los models/clases
from backendSenias.api.serializer import UsuarioSerializer, ConfiguracionSerializer, PerfilSerializer, \
    FeedbackSerializer, IdiomaSerializer, TraduccionSerializer, ArchivoSerializer, LogsSerializer, CategoriaSerializer,ModeloSerializer, \
    GifSerializer
from rest_framework.parsers import MultiPartParser, FormParser  # Para manejar subidas de archivos
from rest_framework.response import Response  # Para enviar respuestas personalizadas
from backendSenias.models import Gif  # Tu modelo Gif
from backendSenias.api.serializer import GifSerializer  # Serializador para Gif
from backendSenias.models import Gif, Categoria
from rest_framework import generics

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

# ViewSet para manejar los modelos
class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()  # Consulta todos los modelos
    serializer_class = ModeloSerializer

# Endpoint para obtener los modelos sin depender del campo "activo"
@api_view(['GET'])
def obtener_modelo(request):
    try:
        # Obtenemos todos los modelos, puedes modificar esto para obtener solo ciertos tipos
        modelos = Modelo.objects.all()
        serializer = ModeloSerializer(modelos, many=True)
        return Response({
            'success': True,
            'modelos': serializer.data
        })
    except Modelo.DoesNotExist:
        return Response({
            'success': False,
            'error': 'No se encontraron modelos'
        }, status=404)

class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer


class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer


class CategoriaViewSet(viewsets.ModelViewSet):  # ViewSet para manejar las categorías
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# para guardar y obtener GIFs de la categoría "saludos"
class GifViewSet(viewsets.ModelViewSet):
    queryset = Gif.objects.all()
    serializer_class = GifSerializer
    parser_classes = [MultiPartParser, FormParser]  # Permite manejar subidas de archivos

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['get'], url_path='saludos')
    def saludos(self, request):
        try:
            categoria_saludos = Categoria.objects.get(nombre='saludos')
            gifs = Gif.objects.filter(categoria=categoria_saludos)
            serializer = self.get_serializer(gifs, many=True)
            return Response(serializer.data)
        except Categoria.DoesNotExist:
            return Response([])

    @action(detail=False, methods=['get'])
    def por_categoria(self, request):
        categoria_id = request.query_params.get('id', None)
        categoria_nombre = request.query_params.get('nombre', None)

        if categoria_id:
            gifs = self.queryset.filter(categoria_id=categoria_id)
        elif categoria_nombre:
            try:
                categoria = Categoria.objects.get(nombre=categoria_nombre)
                gifs = self.queryset.filter(categoria=categoria)
            except Categoria.DoesNotExist:
                return Response({"error": "Categoría no encontrada"}, status=404)
        else:
            return Response({"error": "Falta un identificador de categoría"}, status=400)

        serializer = self.get_serializer(gifs, many=True)
        return Response({"success": True, "data": serializer.data})
