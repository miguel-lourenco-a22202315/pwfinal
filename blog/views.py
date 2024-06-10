from django.shortcuts import render
from .models import Artigo, Autor, Comentario,Avaliacao
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout
from .forms import AutorForm,MusicaForm,ArtigoForm,ComForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "blog/layout.html")

def id(request, artigo_id):
    artigo = Artigo.objects.get( titulo=artigo_id)
    context = {'artigo': artigo}
    return render(request, "blog/artigos.html", context)

def todos_os_artigos(request):
    context = {'artigos': Artigo.objects.all().order_by('titulo')}
    return render(request, "blog/todos_os_artigos.html", context)

def avaliacoes_do_artigo(request, artigo_id):
    artigo = Artigo.objects.get( titulo=artigo_id)

    avaliacao = Avaliacao.objects.filter(artigo=artigo)
    context = {'artigo': artigo, 'avaliacao':avaliacao}

    return render(request, "blog/avaliacoes_do_artigo.html", context)

def artigos_do_autor(request, autor_id):
    autor = Autor.objects.get( nome=autor_id)
    artigos = Artigo.objects.filter(autor=autor).order_by('titulo')
    context = {'autor': autor, 'artigos': artigos}
    return render(request, "blog/artigos_do_autor.html", context)

def comentarios_do_artigo(request, artigo_id):
    artigo = Artigo.objects.get( titulo=artigo_id)
    comentarios = Comentario.objects.filter(artigo=artigo).order_by('data_comentario')
    context = {'artigo': artigo, 'comentarios': comentarios}
    return render(request, "blog/comentarios_do_artigo.html", context)

@login_required
def nova_banda_view(request):

    form = ArtigoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('https://a22202315.pythonanywhere.com/Blog/todos_os_artigos/')


    context = {'form': form}
    return render(request, 'blog/nova_banda.html', context)
@login_required
def edita_banda_view(request, nome):
    banda = Artigo.objects.get(titulo=nome)

    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('https://a22202315.pythonanywhere.com/Blog/todos_os_artigos/')
    else:
        form = ArtigoForm(instance=banda)  # cria formulário com dados da instância autor

    context = {'form': form, 'banda':banda}
    return render(request, 'blog/edita_banda.html', context)
@login_required
def apaga_banda_view(request, nome):
    banda = Artigo.objects.get(titulo=nome)
    banda.delete()
    return redirect('https://a22202315.pythonanywhere.com/Blog/todos_os_artigos/')
@login_required
def nova_album_view(request):

    form = ComForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('https://a22202315.pythonanywhere.com/Blog/todos_os_artigos/')


    context = {'form': form}
    return render(request, 'blog/nova_album.html', context)
@login_required
def edita_album_view(request, nome):
    album = Comentario.objects.get(autor=nome)

    if request.POST:
        form = ComForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('https://a22202315.pythonanywhere.com/Blog/todos_os_artigos/')
    else:
        form = ComForm(instance=album)  # cria formulário com dados da instância autor

    context = {'form': form, 'album':album}
    return render(request, 'blog/edita_album.html', context)
@login_required
def apaga_album_view(request, nome):
    album  =  Comentario.objects.get(autor=nome)
    album.delete()
    return redirect('https://a22202315.pythonanywhere.com/Blog/todos_os_artigos/')
@login_required
def nova_musica_view(request):

    form = MusicaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('https://a22202315.pythonanywhere.com/Blog/todos_os_artigos/')


    context = {'form': form}
    return render(request, 'blog/nova_musica.html', context)
@login_required
def edita_musica_view(request,nome):
    album = Avaliacao.objects.get(autor=nome)

    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('https://a22202315.pythonanywhere.com/Blog/todos_os_artigos/')
    else:
        form =MusicaForm(instance=album)  # cria formulário com dados da instância autor

    context = {'form': form, 'album':album}
    return render(request, 'blog/edita_musica.html', context)
@login_required
def apaga_musica_view(request, nome):
    album  =  Avaliacao.objects.get(autor=nome)
    album.delete()
    return redirect('https://a22202315.pythonanywhere.com/Blog/todos_os_artigos/')

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
        return redirect('https://a22202315.pythonanywhere.com/Bandas/login/')

    return render(request, 'blog/registo.html')



def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return render(request, 'blog/user.html')
        else:
            render(request, 'blog/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'blog/login.html')

def logout_view(request):
    logout(request)
    return redirect('https://a22202315.pythonanywhere.com/Blog/todos_os_artigos/')
