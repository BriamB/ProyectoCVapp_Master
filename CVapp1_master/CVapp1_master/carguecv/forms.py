from django import forms
from .models import carga_cv, Exp_Profesional

class MovimientoCV(forms.ModelForm):
    class Meta:
        model = carga_cv
        fields = '__all__'
class MovimientoExpPro(forms.ModelForm):
    class Meta:
        model = Exp_Profesional
        fields = '__all__'
