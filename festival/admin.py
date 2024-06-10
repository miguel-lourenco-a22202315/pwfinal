from django.contrib import admin
from .models import Bandas, Localizacao,Festivais

admin.site.register(Bandas)
class BandasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'ano_criacao')

admin.site.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('localizacao', 'nome')

admin.site.register(Festivais)
class FestivaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_criacao ')





