from django.shortcuts import render, redirect
from .models import Calificaciones, Programas
from .forms import CalificacionesForm, ProgramasForm
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