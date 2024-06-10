from django.db import models

class band(models.Model):
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


class festivaiss(models.Model):
    nome = models.CharField(max_length=100)
    ano_criacao = models.IntegerField(default=0)
    bandas =  models.ManyToManyField(band)
    localizacao = models.OneToOneField(Localizacao, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='festivais', null=True  )

    def __str__(self):
        return self.nome

