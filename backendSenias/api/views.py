# implementacion de vistas para interactuar con nuestros modelos
# sirve para craer endpoint automaticamente

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from backendSenias.models import Usuario, Configuracion, Perfil, Feedback, Idioma, Traduccion, Modelo, Archivo, Logs, Juego, Partida, Nivel, Puntaje,Categoria, \
    Gif  # importo todos los models/clases
from backendSenias.api.serializer import UsuarioSerializer, ConfiguracionSerializer, PerfilSerializer, \
    FeedbackSerializer, IdiomaSerializer, TraduccionSerializer, ArchivoSerializer, LogsSerializer, CategoriaSerializer,ModeloSerializer, JuegoSerializer, NivelSerializer, PartidaSerializer, PuntajeSerializer, \
    GifSerializer
from rest_framework.parsers import MultiPartParser, FormParser  # Para manejar subidas de archivos
from rest_framework.response import Response  # Para enviar respuestas personalizadas
from backendSenias.models import Gif  # Tu modelo Gif
from backendSenias.api.serializer import GifSerializer  # Serializador para Gif
from backendSenias.models import Gif, Categoria
from rest_framework import generics
from django.utils.timezone import now


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

# ViewSet para el modelo Juego
class JuegoViewSet(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

    @action(detail=False, methods=['post'], url_path='guardar-progreso')
    def guardar_progreso(self, request):
        try:
            print("📥 Datos recibidos en API:", request.data)

            user_id = request.data.get("FK_id_usuario")
            juego_id = request.data.get("FK_id_juego")
            nivel_id = request.data.get("FK_id_nivel")
            resultado = request.data.get("resultado")

            if not user_id or not juego_id or not nivel_id:
                print("❌ Falta algún dato en la solicitud")
                return Response({"error": "Datos incompletos"}, status=status.HTTP_400_BAD_REQUEST)

            # Verificar si el usuario existe
            try:
                usuario = Usuario.objects.get(id=user_id)
            except Usuario.DoesNotExist:
                print(f"❌ Usuario con ID {user_id} no encontrado.")
                return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

            # Verificar si el juego existe
            try:
                juego = Juego.objects.get(id=juego_id)
            except Juego.DoesNotExist:
                print(f"❌ Juego con ID {juego_id} no encontrado.")
                return Response({"error": "Juego no encontrado"}, status=status.HTTP_404_NOT_FOUND)

            # Verificar si el nivel existe
            try:
                nivel = Nivel.objects.get(id=nivel_id)
            except Nivel.DoesNotExist:
                print(f"❌ Nivel con ID {nivel_id} no encontrado.")
                return Response({"error": "Nivel no encontrado"}, status=status.HTTP_404_NOT_FOUND)

            print(f"✅ Guardando partida: Usuario {user_id}, Juego {juego_id}, Nivel {nivel_id}, Resultado {resultado}")

            # Guardar la partida
            partida = Partida.objects.create(
                FK_id_usuario=usuario,
                FK_id_juego=juego,
                FK_id_nivel=nivel,  # 🔹 Se añade el nivel a la partida
                fecha_inicio=now(),
                fecha_fin=now(),
                resultado=resultado
            )

            # Guardar el puntaje
            puntaje = Puntaje.objects.create(
                FK_id_usuario=usuario,
                FK_id_nivel=nivel,
                puntaje_obtenido=resultado,
                fecha_ob_puntaje=now()
            )

            # Guardar en logs
            log = Logs.objects.create(
                fk_id_usu=usuario,
                mensaje_log=f"Partida guardada: Juego {juego.nombre_juego}, Nivel {nivel.dificultad_nivel}, Puntaje {resultado}",
                fecha_log=now(),
                leido_log=False
            )
            print(f"✅ Partida guardada correctamente. ID Partida: {partida.id}")
            return Response({
                "mensaje": "Progreso guardado exitosamente",
                "partida": PartidaSerializer(partida).data,
                "puntaje": PuntajeSerializer(puntaje).data,
                "log": LogsSerializer(log).data
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(f"❌ Error al guardar progreso: {str(e)}")
            return Response({"error": f"Error al guardar el progreso: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


# ViewSet para el modelo Nivel
class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

# ViewSet para el modelo Partida
class PartidaViewSet(viewsets.ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer

# ViewSet para el modelo Puntaje
class PuntajeViewSet(viewsets.ModelViewSet):
    queryset = Puntaje.objects.all()
    serializer_class = PuntajeSerializer


# para guardar y obtener GIF de la categoría "saludos"
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


# endpoint para obtener gifs categoria letras
    @action(detail=False, methods=['get'], url_path='letras')
    def letras(self, request):
        try:
            categoria_letras = Categoria.objects.get(nombre='letras')
            gifs = Gif.objects.filter(categoria=categoria_letras)
            serializer = self.get_serializer(gifs, many=True)
            return Response(serializer.data)
        except Categoria.DoesNotExist:
            return Response({"error": "Categoría 'letras' no encontrada"}, status=404)

# endpoint para obtener las estadisticas del juego en el usuario
@api_view(['GET'])
def obtener_estadisticas_usuario(request, google_id):
    try:
        usuario = Usuario.objects.get(google_id=google_id)
        puntajes = Puntaje.objects.filter(FK_id_usuario=usuario)

        # Organizar los datos por nivel
        niveles_dict = {}
        for puntaje in puntajes:
            nivel = puntaje.FK_id_nivel
            if nivel.id not in niveles_dict:
                niveles_dict[nivel.id] = {
                    "nombre": nivel.dificultad_nivel,
                    "puntos": 0
                }
            niveles_dict[nivel.id]["puntos"] += puntaje.puntaje_obtenido

        data = {
            "usuario": usuario.google_id,
            "total_puntos": sum([p.puntaje_obtenido for p in puntajes]),
            "niveles": list(niveles_dict.values()),  # Convertimos en lista para el frontend
        }

        print("📊 Datos enviados al frontend:", data)  # Depuración

        return Response(data, status=200)
    except Usuario.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=404)
