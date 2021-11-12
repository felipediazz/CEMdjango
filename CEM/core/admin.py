from django.contrib import admin
from .models import Programas, Calificaciones
# Register your models here.

class ProgramaAdmin(admin.ModelAdmin):
    list_display = ['nombre','estado','institucion','pais']
    search_fields = ['nombre','estado','institucion','pais']
    list_filter = ['estado']

class CalificacionAdmin(admin.ModelAdmin):
    list_display = ['alumno','asignatura']
    search_fields = ['alumno','asignatura']
    list_filter = ['asignatura']

admin.site.register(Programas, ProgramaAdmin)
admin.site.register(Calificaciones, CalificacionAdmin)
