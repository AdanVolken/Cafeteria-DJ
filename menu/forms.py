from django import forms
from .models import Bebida,Comida

class FormularioBebidas(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ['nombre', 'ingredientes','precio','imagen','alcohol','disponible' ]
        widgets = {
            'imagen': forms.FileInput(attrs={'accept': 'image/*'}),
        }


class FormularioComida(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ['nombre', 'ingredientes','precio','imagen','disponible' ]
        widgets = {
            'imagen': forms.FileInput(attrs={'accept': 'image/*'}),
        }