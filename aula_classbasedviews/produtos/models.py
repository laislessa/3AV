from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()

class Categoria(models.Model):
    categoria = models.CharField(max_length=255)