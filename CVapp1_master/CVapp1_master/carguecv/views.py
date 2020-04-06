from django.shortcuts import render
from .models import Exp_Profesional, Formacion, Area, carga_cv
from django.http import HttpResponseRedirect
from .forms import MovimientoCV, MovimientoExpPro
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
def cargueexplav(request):
    return render(request, "cargueexplav.html")
def Detail(request):
    return render(request, "detail.html")

def home(request):
    return render (request,"home.html")

class BadgetView(LoginRequiredMixin, ListView):
    template_name = 'carguecv.html'
    model = carga_cv

class BadgetViewExp(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'users.listar'
    template_name = 'cargueexplav.html'
    model = Exp_Profesional

class CreateCV(CreateView):
    model = carga_cv
    fields =['nombre', 'apellido', 'tipo_identificacion', 'ceduala', 'fecha_nacimiento',
    'genero', 'estado_civil', 'telefono', 'Departamento', 'direccion', 'licencia', 'foto',
    'experiencia_profesional', 'formacion', 'idioma', 'nivel', 'estado_laboral', 'area', 'salario', 'archivo_cv', 'cargo' ]

    def get_success_url(self):
        return reverse('')

class BadgetUpdate(UpdateView):
    model = carga_cv
    fields =['nombre', 'apellido', 'tipo_identificacion', 'ceduala', 'fecha_nacimiento',
    'genero', 'estado_civil', 'telefono', 'Departamento', 'direccion', 'licencia', 'foto',
    'experiencia_profesional', 'formacion', 'idioma', 'nivel', 'estado_laboral', 'area', 'salario', 'archivo_cv', 'cargo' ]

    def get_success_url(self):
        return reverse('')

class BadgetDetail(DetailView):
    model = carga_cv
    template_name = 'carguecv/detail.html'

class CreateExplab(CreateView):
    model = Exp_Profesional
    fields = ['Empresa', 'Departamento', 'Periodo_inicio', 'Periodo_fin', 'Funciones']

    def get_success_url(self):
        return reverse('')

class BadgetUpdateExplab(UpdateView):
    model = Exp_Profesional
    fields = ['Empresa', 'Departamento', 'Periodo_inicio', 'Periodo_fin', 'Funciones']

    def get_success_url(self):
        return reverse('')

class BadgetDetailExplab(DetailView):
    template_name = 'detail.html'
    model = Exp_Profesional
