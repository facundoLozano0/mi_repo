from atexit import register
from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('blogs', views.blogs, name='blogs'),
    path('blogs/crear', views.crear, name='crear'),
    path('blogs/editar', views.editar, name='editar'),
    path('borrar/<id>', views.borrar, name='borrar'),
    path('registrate', views.registro, name='registro' )
    #path('login', views.login, name='Ingresar')




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)