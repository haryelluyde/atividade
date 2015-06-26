from django.contrib import admin
from .models import Autor, Receita, Ingrediente

class IngredienteInline(admin.TabularInline):
    model = Ingrediente
    extra = 3

class ReceitaAdmin(admin.ModelAdmin):
    inlines = [IngredienteInline]
    list_display = ('nome', 'tempo_preparo', 'rendimento', 'autor')
    list_filter = ('tempo_preparo', 'rendimento')
    search_fields = ['nome']

admin.site.register(Autor)
admin.site.register(Receita, ReceitaAdmin)