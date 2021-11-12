from django.urls import path
from django.contrib import admin
from .views import regprogramas, listado_programa, modificar_programa, eliminar_programa, listado_notas, regcalificaciones

urlpatterns = [
    path('', regprogramas, name="regprogramas"),
    path('listado-prgramas/', listado_programa, name="listado_progra"),
    path('modificar-programa/<id>/', modificar_programa, name="modificar_programa"),
    path('eliminar-programa/<id>/', eliminar_programa, name="eliminar_programa"),
    path('listado-calificaciones/', listado_notas, name="listado_notas" ),
    path('registro-calificaciones/', regcalificaciones, name="regcalificaciones"),
]