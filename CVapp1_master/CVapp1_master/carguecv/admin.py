from django.contrib import admin
from .models import Departamento, Municipio, Exp_Profesional, Formacion, Area, carga_cv, Tipo_Identificacion, Cargo

# Register your models here.
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Exp_Profesional)
admin.site.register(Formacion)
admin.site.register(Area)
admin.site.register(carga_cv)
admin.site.register(Cargo)
