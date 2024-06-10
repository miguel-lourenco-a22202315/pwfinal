from django import forms    # formulários Django
from .models import Disciplina,Projeto,Curso

class AutorForm(forms.ModelForm):
  class Meta:
    model = Curso      # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.


class AlbumForm(forms.ModelForm):
  class Meta:
    model = Disciplina      # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.


class MusicaForm(forms.ModelForm):
  class Meta:
    model = Projeto      # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.