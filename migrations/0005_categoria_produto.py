from django.db import migrations, models
import django.db.models.deletion

def add_initial_categories(apps, schema_editor):
    Categoria = apps.get_model('salon', 'Categoria')
    categorias_iniciais = [
        "Finalizadores",
        "Colorações",
        "Tratamentos",
        "Descoloração",
        "Alisamentos",
        "Produtos para barba",
        "EPIs"
    ]
    for nome in categorias_iniciais:
        Categoria.objects.get_or_create(nome=nome)

class Migration(migrations.Migration):

    dependencies = [
        ("salon", "0004_agendamento_concluido"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("quantidade", models.IntegerField(default=0)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="salon.Categoria",
                    ),
                ),
            ],
        ),
        migrations.RunPython(add_initial_categories),
    ]
