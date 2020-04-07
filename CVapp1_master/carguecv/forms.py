from django import forms
from .models import carga_cv

class MovimientoCV(forms.ModelForm):
    class Meta:
        model = carga_cv
        fields = '__all__'
