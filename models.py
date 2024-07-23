from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('pix', 'PIX'),
        ('debito', 'Débito'),
        ('credito', 'Crédito'),
        ('dinheiro', 'Dinheiro'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    concluido = models.BooleanField(default=False)
    forma_pagamento = models.CharField(max_length=10, choices=FORMA_PAGAMENTO_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.servico.nome} - {self.data} - {self.hora}"
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
