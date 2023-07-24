from django.db import models



class Modelo(models.Model):
    nome = models.CharField(max_length=20, unique= True)
    idade = models.IntegerField()
    altura = models.FloatField()

    class Meta: 
        ordering = ['nome']

    def __str__(self):
        return self.nome