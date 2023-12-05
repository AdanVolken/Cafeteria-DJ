from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from .views import(
    home,
    inicio_sesion,
    productos,
    agregar_comida,
    agregar_bebida,
    editar_bebida,
    editar_comida,
    eliminar_bebida,
    eliminar_comida,
    bebida,
    comida,
)

urlpatterns = [
    path('',home, name="home"),
    path('login/', inicio_sesion,  name=" inicio_sesion"),
    path('productos/', productos, name = "productos"),
    path('agregar_comida/', agregar_comida, name='agregar_comida'),
    path('agregar_bebida/', agregar_bebida, name='agregar_bebida'),
    path('editar_comida/<int:id_comida>/', editar_comida, name="editar_comida"),
    path('editar_bebida/<int:id_bebida>/', editar_bebida, name="editar_bebida"),
    path('eliminar_comida/<int:id_comida>/', eliminar_comida, name="eliminar_comida"),
    path('eliminar_bebida/<int:id_bebida>/', eliminar_bebida, name="eliminar_bebida"),
    path('bebidas/', bebida, name='bebida'),
    path('comida/', comida, name='comida'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)