from django import forms
from .models import Servico
from django import forms
from .models import Agendamento
from .models import Produto
from django.contrib.auth import logout
from django.shortcuts import render, redirect





class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'valor']

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['servico', 'data', 'hora', 'valor']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'quantidade']

class AtualizarQuantidadeForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['quantidade']        

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)