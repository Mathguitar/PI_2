from django import forms
from .models import AnimalPerdido, AnimalEncontrado
from django.forms import ImageField

class AnimalPerdidoForm(forms.ModelForm):
    foto = ImageField(required=False)
    
    class Meta:
        model = AnimalPerdido
        fields = ('nome', 'especie', 'raca', 'cor', 'descricao', 'foto', 'data_perdido', 'local_perdido', 'nome_perdeu', 'tel_perdeu')

class AnimalEncontradoForm(forms.ModelForm):
    foto = ImageField(required=False)
     
    class Meta:
        model = AnimalEncontrado
        fields = ('nome', 'especie', 'raca', 'cor', 'descricao', 'foto', 'data_encontrado', 'local_encontrado', 'nome_encontrou', 'tel_encontrou')
        widgets = {
            'nome': forms.TextInput(attrs={'required': False}),
            'raca': forms.TextInput(attrs={'required': False}),
        }
