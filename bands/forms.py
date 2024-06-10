from django import forms
from .models import Bandas, Albuns, Musicas

class AutorForm(forms.ModelForm):
    class Meta:
        model = Bandas
        fields = '__all__'

        help_texts = {
            'nome': 'Insira o nome da banda.',
            'nacionalidade': 'Insira a nacionalidade da banda.',
            'ano_criacao': 'Insira o ano de criação da banda.',
            'imagem': 'Faça upload de uma imagem representativa da banda.',
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Albuns
        fields = '__all__'

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musicas
        fields = '__all__'
