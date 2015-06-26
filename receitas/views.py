from django.views import generic

from .models import Autor, Receita, Ingrediente

class ReceitaDetalheView(generic.DetailView):
    model = Receita
    template_name = 'receitas/receita_detalhe.html'