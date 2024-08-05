from .functions.index import home
from .functions.autentication import *
from .functions.escala import *
from .functions.evento import *
from .functions.quantitativo import *
from .functions.colaborador import *
from .functions.fornecedor import *
from .functions.consultar_escala import *
from .functions.consulta_colaborador import *
from .functions.passagem import *
from .functions.beneficios import *
from.functions.realizado import *

#! HOME  
def index(request):
    return home(request)


#! AUTENTICAÇÃO  
def cadastro(request):
    return cadastrar_usuario(request)

def login(request):
    return login_usuario(request)


#! ESCALA   
def update(request, pk):
    return atualizar_escala(request, pk)

def delete(request, pk):
    return deletar_escala(request, pk)

def escalacao(request):
    return visualizar_escalacao(request)


#! EVENTO   
def delete_evento(request, pk):
    return deletar_evento(request, pk)

def cadastro_evento(request):
    return cadastrar_evento(request)

def update_evento(request, pk):
    return atualizar_evento(request,pk)


#! QUANTITATIVO   
def quantitativo(request):
    return criar_quantitativo(request)

def delete_quantitativo(request, pk):
    return deletar_quantitativo(request, pk)


#! CADASTRO COLABORADOR  
def colaborador(request):
    return visualizar_colaborador(request)

def cadastrar_colaborador(request):
    return c_colaborador(request)

def delete_colaborador(request, pk):
    return deletar_colaborador(request, pk)

def update_colaborador(request, pk):
    return atualizar_colaborador(request, pk)

#! CADASTRO FORNECEDOR  
def  fornecedor(request):
    return visualizar_fornecedor(request)

def cadastro_fornecedor(request):
    return cadastrar_fornecedor(request)

def delete_fornecedor(request, pk):
    return deletar_fornecedor(request, pk)

def update_fornecedor(request, pk):
    return atualizar_fornecedor(request, pk)


#!CONSULTAR ESCALA
def consultar_escala(request):
    return visualizar_escala(request)

def delete_escala(request, pk):
    return deletar_consulta_escala(request, pk)

#!CONSULTAR ESCALA COLABORADOR
def consultar_escala_col(request):
    return visualizar_escala_col(request)

#!COMPRA PASSAGEM
def compra_passagem(request):
    return visualizar_passagem(request)

def update_passagem(request, pk):
    return atualizar_passagem(request, pk)




#! Benefícios
def beneficios(request):
    return visualizar_beneficios(request)

def update_beneficios(request, pk):
    return atualizar_beneficios(request, pk)


#! Realizado
def realizado(request):
    return visualizar_realizado(request)

def update_realizado(request, pk):
    return atualizar_realizado(request,pk)