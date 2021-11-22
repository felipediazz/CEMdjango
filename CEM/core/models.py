from django.db import models

# Create your models here.
programa_estado = [
    ('Disponible', 'Disponible'),
    ('No disponible', 'No disponible')
]
sexo = [
    ('Femenino', 'Femenino'),
    ('Masculino', 'Masculino')
]

estado_civil = [
    ('Soltero','Soltero'),
    ('Casado','Casado'),
    ('Separado','Separado'),
    ('Viudo','Viudo'),
    ('Otro','Otro')
]

class Programas(models.Model):
    idPrograma = models.IntegerField(primary_key=True, verbose_name='Id de programa')
    nombre = models.CharField(max_length=200, verbose_name='Nombre del programa')
    duracion = models.CharField(max_length=70, verbose_name='duracion del programa')
    fechaInicio = models.DateField(verbose_name='Fecha inicio del programa')
    fechaFin = models.DateField(verbose_name='Fecha termino del programa')
    asignatura = models.CharField(max_length=50, verbose_name='Nombre de la asignatura')
    estado = models.CharField(max_length=50, verbose_name='Indicar estado disponible o no disponible',null=False,blank=False,
                                choices=programa_estado, default='Disponible')
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

class Postulante(models.Model):
    rut = models.CharField(primary_key=True,max_length=12, verbose_name='Rut postulante')
    postulante = models.CharField(max_length=200, verbose_name='Nombre del postulante')
    fechaNaci = models.DateField(verbose_name='Fecha de nacimiento')
    nacionalidad = models.CharField(max_length=50, verbose_name='Nacionalidad')
    estadoCivil = models.CharField(max_length=50, verbose_name='Estado civil',null=False,blank=False,choices=estado_civil, default='Soltero')
    sexo = models.CharField(max_length=50, verbose_name='Indicar sexo',null=False,blank=False,
                            choices=sexo, default='Masculino')
    telefono = models.IntegerField(verbose_name='Numero de celular')
    correo = models.CharField(max_length=200, verbose_name='Correo del postulante')
    procAcademica = models.CharField(max_length=200, verbose_name='Procedencia academica')
    programa = models.ForeignKey(Programas, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.postulante