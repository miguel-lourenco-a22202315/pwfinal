from django.db import models

class Bandas(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100, default='')
    ano_criacao = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to='bandas/', default='bandas/default.jpg', null=True)
    biografia = models.TextField(default='', null=True, blank=True)
    descricaocompleta = models.TextField(default='', null=True, blank=True)
    imagemintegrantes = models.ImageField(upload_to='bandas/', default='bandas/default.jpg', null=True)





class Albuns(models.Model):
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField(default=0)
    banda = models.ForeignKey(Bandas, on_delete=models.CASCADE, default=1)
    link =models.URLField( null=True)
    imagem = models.ImageField(upload_to='bandas/', default='bandas/default.jpg', null=True)



class Musicas(models.Model):
    titulo = models.CharField(max_length=100)
    duracao = models.CharField(max_length=10, default='')
    album = models.ForeignKey(Albuns, on_delete=models.CASCADE)
    letra = models.TextField(default='', null=True, blank=True)
    link =models.URLField( null=True)
    imagem = models.ImageField(upload_to='bandas/', default='bandas/default.jpg', null=True)

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    banda = models.ForeignKey(Bandas, on_delete=models.CASCADE ,default=1)

