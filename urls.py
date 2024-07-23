from django.urls import path
from . import views
from .views import agendar_servico
from .views import agendamentos_concluidos, pesquisar_cliente
from .views import AgendamentosRelatorioView, exportar_agendamentos_excel
from .views import login_view
from .views import login_view, logout_view



urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', views.home, name='home'),  # Defina uma rota padrão
    path('index/', views.index, name='index'),  # Mudei o caminho para não conflitar
    path('dashboard/', views.dashboard, name='dashboard'),  # Adiciona esta linha se 'dashboard' for uma view existente
    path('novo_agendamento/', views.novo_agendamento, name='novo_agendamento'),
    path('editar_agendamento/<int:agendamento_id>/', views.editar_agendamento, name='editar_agendamento'),
    path('excluir_agendamento/<int:agendamento_id>/', views.excluir_agendamento, name='excluir_agendamento'),
    path('agendamentos_pendentes/', views.agendamentos_pendentes, name='agendamentos_pendentes'),
    path('concluir_agendamento/<int:agendamento_id>/', views.concluir_agendamento, name='concluir_agendamento'),
    path('agendamentos_concluidos/', views.agendamentos_concluidos, name='agendamentos_concluidos'),
    path('obter-valor-servico/', views.obter_valor_servico, name='obter_valor_servico'),
    path('lista_servicos/', views.lista_servicos, name='lista_servicos'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('lista_produtos/', views.lista_produtos, name='lista_produtos'),
    path('atualizar_quantidade/<int:produto_id>/', views.atualizar_quantidade, name='atualizar_quantidade'),
    path('filtrar_por_categoria/<int:categoria_id>/', views.filtrar_por_categoria, name='filtrar_por_categoria'),
    path('pesquisar-cliente/', pesquisar_cliente, name='pesquisar_cliente'),
    path('excluir_agendamento/<int:agendamento_id>/', views.excluir_agendamento, name='excluir_agendamento'),
    path('relatorio_agendamentos/', AgendamentosRelatorioView.as_view(), name='relatorio_agendamentos'),
    path('exportar_agendamentos_excel/', exportar_agendamentos_excel, name='exportar_agendamentos_excel'),
    path('agendamentos_graficos/', views.agendamentos_graficos, name='agendamentos_graficos'),
    


    

]
