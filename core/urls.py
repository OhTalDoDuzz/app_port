from django.urls import path
from . import views

urlpatterns = [

    #! Autenticação
    path('', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),

    #! Home    
    path('home/', views.index, name='index'),

    #! Escala
    path('escalacao/', views.escalacao, name='escalacao'), 
    path('update_escala/<int:pk>', views.update, name='update_escala'),
    path('delete_escala/<int:pk>', views.delete, name='delete_escala'),

    #! Evento
    path('cadastrar_evento/', views.cadastro_evento, name='cadastrar_evento'),
    path('delete_evento/<int:pk>', views.delete_evento, name='delete_evento'),
    path('update_evento/<int:pk>', views.update_evento, name='update_evento'), 

    #! Quantitativo
    path('quantitativo/', views.quantitativo, name='quantitativo'),
    path('delete_quantitativo/<int:pk>', views.delete_quantitativo, name='delete_quantitativo'),

    #! Colaborador
    path('colaborador/', views.colaborador, name='colaborador'),
    path('cadastrar_colaborador/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('delete_colaborador/<int:pk>', views.delete_colaborador, name='delete_colaborador'), 
    path('update_colaborador/<int:pk>', views.update_colaborador, name='update_colaborador'), 

    #! Fornecedor
    path('fornecedor/', views.fornecedor, name='fornecedor'),
    path('cadastrar_fornecedor/', views.cadastro_fornecedor, name='cadastrar_fornecedor'),
    path('delete_fornecedor/<int:pk>/', views.delete_fornecedor, name='delete_fornecedor'),
    path('update_fornecedor/<int:pk>', views.update_fornecedor, name='update_fornecedor'),

    #! Consulta Escala
    path('consulta_escala/', views.consultar_escala, name='consultar_escala'),
    path('deletar_consulta_escala/<int:pk>', views.deletar_consulta_escala, name='deletar_consulta_escala'),

    #! Consulta Escala_colaborador
    path('consulta_escala_col/', views.visualizar_escala_col, name='consulta_escala_col'),

    #! Compra Passagem
    path('compra_passagem/', views.compra_passagem, name='compra_passagem'),
    path('update_passagem/<int:pk>', views.update_passagem, name='update_passagem'),

    #! Pagamento beneficios
    path('beneficios/', views.beneficios, name='beneficios'),
    path('update_beneficios/<int:pk>', views.update_beneficios, name='update_beneficios'), 

    #! Realizado
    path('realizado/', views.realizado, name='realizado'),
    path('update_realizado/<int:pk>', views.update_realizado, name='update_realizado'), 
]


