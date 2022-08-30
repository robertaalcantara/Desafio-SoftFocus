from django import forms
from .models import Comunicacao

class ComunicacaoForm(forms.ModelForm):
    class Meta:
        model = Comunicacao
        fields = '__all__'
