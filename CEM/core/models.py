from django.db import models

# Create your models here.


class Programas(models.Model):
    idPrograma = models.IntegerField(primary_key=True, verbose_name='Id de programa')
    nombre = models.CharField(max_length=200, verbose_name='Nombre del programa')
    duracion = models.CharField(max_length=70, verbose_name='duracion del programa')
    fechaInicio = models.DateField(verbose_name='Fecha inicio del programa')
    fechaFin = models.DateField(verbose_name='Fecha termino del programa')
    asignatura = models.CharField(max_length=50, verbose_name='Nombre de la asignatura')
    estado = models.CharField(max_length=50, verbose_name='Indicar estado disponible o no disponible')
    institucion = models.CharField(max_length=200, verbose_name='Nombre de la institucion')
    pais = models.CharField(max_length=200, verbose_name='Pais de la institucion')

    def __str__(self):
        return self.nombre

class Calificaciones(models.Model):
    idCalificacion = models.IntegerField(primary_key=True, verbose_name='Id de calificacion')
    alumno = models.CharField(max_length=200, verbose_name='Nombre del alumno')
    asignatura = models.CharField(max_length=50, verbose_name='Nombre de la asignatura')
    nota1 = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Nota 1')
    nota2 = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Nota 2')
    nota3 = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Nota 3')
    nota4 = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Nota 4')
    nota5 = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Nota 5')
    nota6 = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Nota 6')
    profesor = models.CharField(max_length=300, verbose_name='Nombre Apellido del profesor encargado')
    institucion = models.CharField(max_length=200, verbose_name='Nombre de la institucion')

    def __str__(self):
        return self.alumno