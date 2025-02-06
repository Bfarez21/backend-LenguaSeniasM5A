

# especificamos las rutas usando viewSet
from rest_framework.routers import DefaultRouter
from backendSenias.api.views import UsuarioViewSet,ConfiguracionViewSet,PerfilViewSet,FeedbackViewSet,IdiomaViewSet,TraduccionViewSet,ArchivoViewSet,LogsViewSet,ModeloViewSet,CategoriaViewSet,GifViewSet
from . import views
router = DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='usuario')
router.register('config', ConfiguracionViewSet, basename='configuracion')
router.register('perfil', PerfilViewSet, basename='perfil')
router.register('feedback', FeedbackViewSet, basename='feedback')
router.register('idioma', IdiomaViewSet, basename='idioma')
router.register('traduccion', TraduccionViewSet, basename='traduccion')

router.register('modelo', ModeloViewSet, basename='modelo')

router.register('modelo-activo', ModeloViewSet, basename='modelo-activo')
router.register('archivo', ArchivoViewSet, basename='archivo')
router.register('logs', LogsViewSet, basename='logs')
router.register('categoria', views.CategoriaViewSet, basename='categoria')

router.register('partida', views.PartidaViewSet, basename='partida')
router.register('puntaje', views.PuntajeViewSet, basename='puntaje')
router.register('juego', views.JuegoViewSet, basename='juego')
router.register('nivel', views.NivelViewSet, basename='nivel')
router.register('gifs', GifViewSet, basename='gifs')
urlpatterns = router.urls
