from django.shortcuts import render, redirect
from .models import Calificaciones, Programas, Postulante
from .forms import CalificacionesForm, ProgramasForm, PostulanteForm
from django.views.generic import CreateView
# Create your views here.


#pagina principal
def index(request):
   return render(request, 'core/index.html')



def regprogramas(request):
    data = {
        'form':ProgramasForm()
    }

    if request.method == 'POST':
        formulario = ProgramasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Programa registrado Correctamente"

    return render(request, 'core/regprogramas.html',data)

def listado_programa(request):
    programas = Programas.objects.all()
    data = {
        'programas':programas
    }
    return render(request, 'core/listado_progra.html', data)

def listado_postu (request):
    programas_filtrados = Programas.objects.filter(estado='Disponible')
    data = {
        'programas_filtrados':programas_filtrados
    }
    return render(request, 'core/listado_postu.html', data)

def modificar_programa(request, id):
    programa = Programas.objects.get(idPrograma=id)
    data = {
        'form': ProgramasForm(instance=programa)
    }

    if request.method == 'POST':
        formulario = ProgramasForm(data=request.POST, instance=programa)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correcatamente"
            data['form'] = formulario        

    return render(request, 'core/modificar_progra.html', data)

def eliminar_programa(request, id):
    programa = Programas.objects.get(idPrograma=id)
    programa.delete()

    return redirect(to="listado_progra")

# POSTULACION

def postular (request, id):
    programa = Programas.objects.get(idPrograma=id)
    data = {
        'form':PostulanteForm(),
        
    }
    if request.method == 'POST':
        formulario = PostulanteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Postulacion registrada Correctamente"
   
    return render(request, 'core/postular.html',data)

# PORTAL DE NOTAS

def listado_notas(request):
    notas = Calificaciones.objects.all()
    data = {
        'notas':notas
    }
    return render(request, 'core/portal_notas.html', data)


def regcalificaciones(request):
    data = {
        'form':CalificacionesForm()
    }

    if request.method == 'POST':
        formulario = CalificacionesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Calificaciones registradas Correctamente"

    return render(request, 'core/regcalificacion.html',data)