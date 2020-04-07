from django.shortcuts import render
from .models import Area, carga_cv
from django.http import HttpResponseRedirect
from .forms import MovimientoCV
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

#Login requerido
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

def carguecv(request):
    return render(request, "carguecv.html")
def Detail(request):
    return render(request, "detail.html")

def home(request):
    return render (request,"home.html")

class BadgetView(LoginRequiredMixin, ListView):
    template_name = 'carguecv.html'
    model = carga_cv

class CreateCV(CreateView):
    model = carga_cv
    fields =['nombre', 'apellido', 'tipo_identificacion', 'cedula', 'fecha_nacimiento', 'genero', 'estado_civil', 'telefono',
    'municipio', 'direccion', 'Centro_educativo','Nivel_educativo','Estado_estudio', 'cargo','Empresa','Periodo_inicio',
    'Periodo_fin','Funciones', 'idioma', 'nivel','area', 'salario','foto', 'archivo_cv']

    def get_success_url(self):
        return reverse('')

class BadgetUpdate(UpdateView):
    model = carga_cv
    fields =['nombre', 'apellido', 'tipo_identificacion', 'cedula', 'fecha_nacimiento', 'genero', 'estado_civil', 'telefono',
    'municipio', 'direccion', 'Centro_educativo','Nivel_educativo','Estado_estudio', 'cargo','Empresa','Periodo_inicio',
    'Periodo_fin','Funciones', 'idioma', 'nivel','area', 'salario','foto', 'archivo_cv']

    def get_success_url(self):
        return reverse('')

class BadgetDetail(DetailView):
    model = carga_cv
    template_name = 'carguecv/detail.html'
