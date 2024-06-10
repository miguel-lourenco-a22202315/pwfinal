from django.contrib import admin
from .models import Bandas, Albuns, Musicas, Pessoa


class BandasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'ano_criacao')


admin.site.register(Bandas, BandasAdmin)


class AlbunsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano_lancamento', 'banda')


admin.site.register(Albuns, AlbunsAdmin)


class MusicasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'duracao', 'album')


admin.site.register(Musicas, MusicasAdmin)


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'banda')


admin.site.register(Pessoa, PessoaAdmin)
