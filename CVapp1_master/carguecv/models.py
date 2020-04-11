from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Departamento(models.Model):
    departamento = models.CharField(max_length=200)
    def __str__(self):
        return self.departamento

class Municipio(models.Model):
    municipio= models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.municipio

class Area(models.Model):
    Areas = models.CharField(max_length=50)

    def __str__(self):
        return self.Areas

class Tipo_Identificacion(models.Model):
    Tipo_identificacion = models.CharField(max_length=50)

    def __str__(self):
        return self.Tipo_identificacion

class Cargo(models.Model):
    descripcion = models.CharField(max_length=20)
    def __str__(self):
        return self.descripcion

class carga_cv(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_identificacion = models.ForeignKey(Tipo_Identificacion, null=False, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=15)
    estado_civil = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    municipio = models.ForeignKey(Municipio, null=False, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50)
    Centro_educativo = models.CharField(max_length=200)
    Nivel_educativo = models.CharField(max_length=200)
    Estado_estudio = models.CharField(max_length=100)
    Periodo_inicio = models.DateField()
    Periodo_fin = models.DateField()
    cargo = models.ForeignKey(Cargo, null=False, on_delete=models.CASCADE)
    Empresa = models.CharField(max_length=200)
    Periodo_inicio = models.DateField()
    Periodo_fin = models.DateField()
    Funciones = models.CharField(max_length=300)
    idioma = models.CharField(max_length=20)
    nivel = models.CharField(max_length=15)
    area = models.ForeignKey(Area, null=False, on_delete=models.CASCADE)
    salario = models.IntegerField()
    foto = models.FileField(null=False, upload_to="Foto/%Y/%m/%d")
    archivo_cv = models.FileField(null=False, upload_to="Cv/%Y/%m/%d")
