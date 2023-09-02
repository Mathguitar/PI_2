from django.db import models
# Create your models here.

class AnimalPerdido(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='foto_encontrados/', blank=True, null=True)
    data_perdido = models.DateField()
    local_perdido = models.CharField(max_length=100)
    nome_perdeu = models.CharField(max_length=100, default='Desconhecido')
    tel_perdeu = models.CharField(max_length=100, default='00')
    
    def __str__(self):
        return self.nome

class AnimalEncontrado(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100, blank=True, null=True)
    cor = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='foto_encontrados/', blank=True, null=True)
    data_encontrado = models.DateField()
    local_encontrado = models.CharField(max_length=100)
    nome_encontrou = models.CharField(max_length=100, default='Desconhecido')
    tel_encontrou = models.CharField(max_length=100, default='00')

    def __str__(self):
        return self.nome
