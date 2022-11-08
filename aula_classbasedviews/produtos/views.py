from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView
from produtos.models import Produto,Categoria
# from django.urls import reverse_lazy


class ProdutoListView(ListView):
    model = Produto
    model = Categoria
    context_object_name = 'produtos'
    context_object_name = 'categorias'

class ProdutoCreateView(CreateView):
    model = Produto
    model = Categoria
    fields = ['nome','preco',' categorias'],
    # sucess_url = reverse_lazy('list_produtos')
