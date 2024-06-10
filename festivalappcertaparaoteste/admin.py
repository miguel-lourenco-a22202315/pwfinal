from django.contrib import admin
from .models import band, festivaiss,Localizacao

admin.site.register(band)
class banAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'ano_criacao')

admin.site.register(Localizacao)
class LocalizAdmin(admin.ModelAdmin):
    list_display = ('localizacao', 'nome')

admin.site.register(festivaiss)
class FestiAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_criacao ')





