from datetime import datetime
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import *
from datetime import time

@login_required
def visualizar_passagem(request):
    escalas = Escala.objects.all()
    form = None 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('compra_passagem')
    return render(request,'passagem/passagem.html', {'escalas': escalas, 'form': form})


@login_required
def atualizar_passagem(request, pk):
    escala = get_object_or_404(Escala, pk=pk)
    colaborador = get_object_or_404(Colaborador, pk=escala.id_colaborador)

    if request.method == 'POST':
        #Salvar passagem:
        escala.passagem = request.POST.get('passagem')

        #Salvar valor passagem
        valor_passagem = request.POST.get('valor_passagem')
        if valor_passagem:
            valor_passagem = str(valor_passagem)
            valor_passagem = valor_passagem.replace(',','.')
            escala.valor_passagem = valor_passagem


        #Salvar Hora ida e hora volta:
        ida = request.POST.get('hora_ida')
        volta = request.POST.get('hora_volta')

        escala.hora_ida = ida if ida else None
        escala.hora_volta = volta if volta  else None

        #Salvar Meio de Transpote
        escala.meio_transporte = request.POST.get('transporte')

        #Salvar TIPO DE QUARTO
        escala.tipo_quarto = request.POST.get('quarto')

        #Salvar Companhia Aérea
        companhia = request.POST.get('companhia')
        if companhia:
            companhia = str(companhia)
            companhia = companhia.upper()
            escala.companhia_aerea = companhia

        #Salvar Loc
        loc = request.POST.get('loc')
        if loc:
            loc = str(loc)
            loc = loc.upper()
            escala.loc_voo = loc

        #Salvar mobilidade
        hora_ida_voo_partindo_inicio = time(23, 30)  # 23:30
        hora_ida_voo_partindo_fim = time(9, 30)  # 09:30

        hora_retorno_voo_chegando_inicio = time(20, 0)  # 20:00
        hora_retorno_voo_chegando_fim = time(5, 0)  # 05:00

        valor_mobilidade_ida = 25
        valor_mobilidade_retorno = 25

        if escala.hora_ida:
            hora_ida = time.fromisoformat(escala.hora_ida)
            if (hora_ida >= hora_ida_voo_partindo_inicio or hora_ida <= hora_ida_voo_partindo_fim):
                valor_mobilidade_ida = 50

        if escala.hora_volta:
            hora_retorno = time.fromisoformat(escala.hora_volta)
            if (hora_retorno >= hora_retorno_voo_chegando_inicio or hora_retorno <= hora_retorno_voo_chegando_fim):
                valor_mobilidade_retorno = 50

        escala.valor_mobilidade = valor_mobilidade_ida + valor_mobilidade_retorno

        #Salvar valor hotel
        valor_hotel = request.POST.get('valor_hotel')
        if valor_hotel:
            valor_hotel = str(valor_hotel)
            valor_hotel = valor_hotel.replace(',','.')
            escala.valor_hotel = valor_hotel

        #Salvar Status
        escala.status_fase2 = request.POST.get('status2')

        #Voltar Fase
        voltar_fase = request.POST.get('voltar_fase')
        if voltar_fase == "true":
            escala.status_fase1 = "PENDENTE"

        #Salvar Nome Hotel
        nome_hotel = request.POST.get('nome_hotel')
        if nome_hotel:
            nome_hotel = str(nome_hotel)
            escala.nome_hotel = nome_hotel

        escala.save()
        return redirect('compra_passagem')
    return render(request, 'passagem/update_passagem.html', {'escala': escala, 'colaborador':colaborador})

