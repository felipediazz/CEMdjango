from django.urls import path
from django.contrib import admin
from .views import index ,regprogramas, listado_programa, modificar_programa, eliminar_programa, listado_notas, regcalificaciones, listado_postu, postular

urlpatterns = [
    path('', index, name="index"),
    path('regprogramas/', regprogramas, name="regprogramas"),
    path('listado-prgramas/', listado_programa, name="listado_progra"),
    path('modificar-programa/<id>/', modificar_programa, name="modificar_programa"),
    path('eliminar-programa/<id>/', eliminar_programa, name="eliminar_programa"),
    path('listado-calificaciones/', listado_notas, name="listado_notas" ),
    path('registro-calificaciones/', regcalificaciones, name="regcalificaciones"),
    path('listado_postular/', listado_postu, name="listado_postu"),
    path('postulacion/<id>/', postular, name="postular")
]