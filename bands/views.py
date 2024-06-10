from django.shortcuts import render
from .models import Bandas, Musicas, Albuns
from .forms import AutorForm,MusicaForm,AlbumForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


def bandas_view(request):
    context = {
        'bandas': Bandas.objects.all().order_by('nome'),
    }
    return render(request, "bands/bandas.html", context)


def album_view(request, banda_nome):

    banda = Bandas.objects.get(nome=banda_nome)

    albuns_da_banda = Albuns.objects.filter(banda=banda)

    context = {
        'banda': banda,
        'albuns': albuns_da_banda
    }
    return render(request, "bands/album.html", context)

def banda_view(request, nome):
    context = {
        'banda': Bandas.objects.get(nome=nome)
    }
    return render(request, "bands/banda.html", context)


def musicas_view(request, album_nome):
    album = Albuns.objects.get(titulo=album_nome)
    musicas_do_album = Musicas.objects.filter(album=album)
    context = {
        'musicas': musicas_do_album,
        'album': album
    }
    return render(request, "bands/musicas.html", context)



@login_required
def nova_banda_view(request):

    form = AutorForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('https://a22202315.pythonanywhere.com/Bandas/bandas/')


    context = {'form': form}
    return render(request, 'bands/nova_banda.html', context)
@login_required
def edita_banda_view(request, nome):
    banda = Bandas.objects.get(nome=nome)

    if request.POST:
        form = AutorForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('https://a22202315.pythonanywhere.com/Bandas/banda/{}/'.format(banda.nome))
    else:
        form = AutorForm(instance=banda)  # cria formulário com dados da instância autor

    context = {'form': form, 'banda':banda}
    return render(request, 'bands/edita_banda.html', context)
@login_required
def apaga_banda_view(request, nome):
    banda = Bandas.objects.get(nome=nome)
    banda.delete()
    return redirect('https://a22202315.pythonanywhere.com/Bandas/bandas/')



@login_required
def apaga_album_view(request, nome,nomebanda):
    banda = Bandas.objects.get(nome=nomebanda)
    album  =  Albuns.objects.get(titulo=nome)
    album.delete()

    return redirect('https://a22202315.pythonanywhere.com/Bandas/album/{}/'.format(banda.nome))


@login_required
def nova_album_view(request, nomebanda):
    banda = Bandas.objects.get(nome=nomebanda)
    form = AlbumForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('https://a22202315.pythonanywhere.com/Bandas/album/{}/'.format(banda.nome))


    context = {'form': form,'banda':banda}
    return render(request, 'bands/nova_album.html', context)

@login_required
def nova_musica_view(request,titulo):
    album= Albuns.objects.get(titulo=titulo)

    form = MusicaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('https://a22202315.pythonanywhere.com/Bandas/musica/{}/'.format(album.titulo))


    context = {'form': form,'album':album}
    return render(request, 'bands/nova_musica.html', context)


@login_required
def edita_album_view(request, nome, nomebanda):
    banda = Bandas.objects.get(nome=nomebanda)
    album = Albuns.objects.get(titulo=nome)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('https://a22202315.pythonanywhere.com/Bandas/album/{}/'.format(banda.nome))
    else:
        form = AlbumForm(instance=album)  # cria formulário com dados da instância autor rever aqui

    context = {'form': form, 'album':album,'banda':banda}
    return render(request, 'bands/edita_album.html', context)

@login_required
def edita_musica_view(request,nome,nomealbum):
    album = Musicas.objects.get(titulo=nome)
    album2=Albuns.objects.get(titulo=nomealbum)
    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('https://a22202315.pythonanywhere.com/Bandas/musica/{}/'.format(album2.titulo))
    else:
        form =MusicaForm(instance=album)  # cria formulário com dados da instância autor

    context = {'form': form, 'album':album,'album2':album2}
    return render(request, 'bands/edita_musica.html', context)
@login_required
def apaga_musica_view(request, nome,nomealbum):
    album  =  Musicas.objects.get(titulo=nome)
    album.delete()
    album2=Albuns.objects.get(titulo=nomealbum)
    return redirect('https://a22202315.pythonanywhere.com/Bandas/musica/{}/'.format(album2.titulo))

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

    return render(request, 'bands/registo.html')



def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return render(request, 'bands/user.html')
        else:
            render(request, 'bands/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'bands/login.html')

def logout_view(request):
    logout(request)
    return redirect('https://a22202315.pythonanywhere.com/Bandas/bandas/')
