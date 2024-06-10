from django.shortcuts import render
from .models import Curso, Disciplina, Projeto
from .forms import AutorForm,MusicaForm,AlbumForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

def curso_page(request, curso_nome):
    curso = Curso.objects.get( nome=curso_nome)
    context = {
        'curso': curso,
    }
    return render(request, 'LEI/curso.html', context)


def disciplina_page(request, disciplina_id):
    disciplina = Disciplina.objects.get(nome=disciplina_id)
    context = {
        'disciplina': disciplina,
    }
    return render(request, 'LEI/disciplina.html', context)

def projeto_page(request, projeto_nome,nome):
    projeto = Projeto.objects.get( nome=projeto_nome)
    disciplina = Disciplina.objects.get(nome=nome)

    context = {
        'projeto': projeto,
        'disciplina': disciplina,
    }
    return render(request, 'LEI/projeto.html', context)

def projetos(request, disciplina_nome):
    disciplina = Disciplina.objects.get(nome=disciplina_nome)

    context = {
        'disciplina': disciplina,
    }
    return render(request, 'LEI/projetos.html', context)
@login_required
def nova_banda_view(request):

    form = AutorForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('https://a22202315.pythonanywhere.com/Lusofona/curso/Engenharia%20Inform%C3%A1tica/')


    context = {'form': form}
    return render(request, 'LEI/nova_banda.html', context)
@login_required
def edita_banda_view(request, nome):
    banda = Curso.objects.get(nome=nome)

    if request.POST:
        form = AutorForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('https://a22202315.pythonanywhere.com/Lusofona/curso/Engenharia%20Inform%C3%A1tica/')
    else:
        form = AutorForm(instance=banda)

    context = {'form': form, 'banda':banda}
    return render(request, 'LEI/edita_banda.html', context)
@login_required
def apaga_banda_view(request, nome):
    banda = Curso.objects.get(nome=nome)
    banda.delete()
    return redirect('https://a22202315.pythonanywhere.com/Lusofona/curso/Engenharia%20Inform%C3%A1tica/')
@login_required
def nova_album_view(request):

    form = AlbumForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('https://a22202315.pythonanywhere.com/Lusofona/curso/Engenharia%20Inform%C3%A1tica/')


    context = {'form': form}
    return render(request, 'LEI/nova_album.html', context)
@login_required
def edita_album_view(request, nome):
    album =Disciplina.objects.get(nome=nome)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('https://a22202315.pythonanywhere.com/Lusofona/disciplina/{}/'.format(album.nome))
    else:
        form = AlbumForm(instance=album)

    context = {'form': form, 'album':album}
    return render(request, 'LEI/edita_album.html', context)
@login_required
def apaga_album_view(request, nome):
    album  =  Disciplina.objects.get(nome=nome)
    album.delete()
    return redirect('https://a22202315.pythonanywhere.com/Lusofona/curso/Engenharia%20Inform%C3%A1tica/')
@login_required
def nova_musica_view(request,nome):
    album  =  Disciplina.objects.get(nome=nome)
    form = MusicaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('https://a22202315.pythonanywhere.com/Lusofona/disciplina/{}/'.format(album.nome))


    context = {'form': form}
    return render(request, 'LEI/nova_musica.html', context)
@login_required
def edita_musica_view(request,nome,nome2):
    album = Projeto.objects.get(nome=nome)
    disciplina = Disciplina.objects.get(nome=nome2)


    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('https://a22202315.pythonanywhere.com/Lusofona/projeto/{}/{}/'.format(album.nome, disciplina.nome))
    else:
        form =MusicaForm(instance=album)

    context = {'form': form,
    'projeto': album,
        'disciplina': disciplina,
                     }
    return render(request, 'LEI/edita_musica.html', context)
@login_required
def apaga_musica_view(request, nome,nome2):
    album  =  Projeto.objects.get(nome=nome)
    album.delete()
    disciplina=Disciplina.objects.get(nome=nome)

    return redirect('https://a22202315.pythonanywhere.com/Lusofona/disciplina/{}/'.format(disciplina.nome))






from django.contrib.auth import models


def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('https://a22202315.pythonanywhere.com/LEI/login/')

    return render(request, 'LEI/registo.html')



def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return render(request, 'LEI/user.html')
        else:
            render(request, 'LEI/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'LEI/login.html')

def logout_view(request):
    logout(request)
    return redirect('https://a22202315.pythonanywhere.com/Lusofona/curso/Engenharia%20Inform%C3%A1tica/')