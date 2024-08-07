# Generated by Django 4.2.13 on 2024-06-04 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("salon", "0005_categoria_produto"),
    ]

    operations = [
        migrations.AddField(
            model_name="agendamento",
            name="forma_pagamento",
            field=models.CharField(
                blank=True,
                choices=[
                    ("pix", "PIX"),
                    ("debito", "Débito"),
                    ("credito", "Crédito"),
                    ("dinheiro", "Dinheiro"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="agendamento",
            name="data",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="agendamento",
            name="hora",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
