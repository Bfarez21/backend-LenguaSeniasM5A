# especificamos las rutas usando viewSet

from rest_framework.routers import DefaultRouter
from backendSenias.api.views import UsuarioViewSet

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='usuarios')
urlpatterns = router.urls
