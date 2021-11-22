from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Programas, Calificaciones, Postulante

class ProgramasForm(ModelForm):

    class Meta:
        model = Programas
        fields = ['nombre','duracion','fechaInicio','fechaFin','asignatura','estado','institucion','pais']

class CalificacionesForm(ModelForm):

    class Meta:
        model = Calificaciones
        fields = ['alumno','asignatura','nota1','nota2','nota3','nota4','nota5','nota6','profesor','institucion']

class PostulanteForm(ModelForm):

    class Meta:
        model = Postulante
        fields = ['rut','postulante','fechaNaci','nacionalidad','estadoCivil','sexo','telefono','correo','procAcademica','programa']