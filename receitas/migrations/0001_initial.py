# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'autor',
                'verbose_name_plural': 'autores',
            },
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'ingrediente',
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('tempo_preparo', models.CharField(max_length=45, verbose_name='Tempo de preparo')),
                ('modo_preparo', models.TextField(verbose_name='Modo de preparo')),
                ('rendimento', models.IntegerField(verbose_name='Rendimento')),
                ('autor', models.ForeignKey(to='receitas.Autor')),
            ],
            options={
                'verbose_name': 'receita',
                'verbose_name_plural': 'receitas',
            },
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='receita',
            field=models.ForeignKey(to='receitas.Receita'),
        ),
    ]
