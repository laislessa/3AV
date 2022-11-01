from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from produtos.models import Produto


class ProdutoListView(ListView):
    model = Produto
    context_object_name = 'produtos'