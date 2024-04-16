from django.urls import path
from . import views
# se importa para acceder a las medias creadas para ver las imagenes
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('we', views.nosotros, name='nosotros'),
    path('index', views.libros, name='index'),
    path('index/create', views.create, name='create'),
    path('index/update', views.update, name='update'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('index/update/<int:id>', views.update, name='update'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
