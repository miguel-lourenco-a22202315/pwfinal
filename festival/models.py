from django.db import models

class Bandas(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100, default='')
    ano_criacao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Localizacao(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100, null=True )


    def __str__(self):
        return self.nome


class Festivais(models.Model):
    nome = models.CharField(max_length=100)
    ano_criacao = models.IntegerField(default=0)
    bandas =  models.ManyToManyField(Bandas)
    localizacao = models.OneToOneField(Localizacao, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='festivais', null=True  )

    def __str__(self):
        return self.nome


