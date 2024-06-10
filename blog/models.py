from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.DateField()
    imagem = models.ImageField(upload_to='blog/', default='blog/default.jpg', null=True)

    def __str__(self):
        return f'{self.nome} - {self.idade} idade'

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao =  models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    resumo = models.TextField(null = True )

    def __str__(self):
        return f'{self.autor} - {self.titulo} - {self.conteudo} -{self.data_publicacao} datadecriaçao '


class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    data_comentario =  models.DateField()
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.autor} - {self.artigo} - {self.texto} -{self.data_comentario} data de comentario '





class Avaliacao(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    pontuacao = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
         return f'Avaliação de {self.artigo.titulo} por {self.autor}: Pontuação {self.pontuacao}'



