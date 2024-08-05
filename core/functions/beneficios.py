from datetime import datetime
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import *

@login_required
def visualizar_beneficios(request):
    escalas = Escala.objects.all()
    form = None 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('compra_passagem')
    return render(request, 'beneficios/beneficios.html', {'escalas': escalas, 'form': form})


def atualizar_beneficios(request, pk):
    escala = get_object_or_404(Escala, pk=pk)

    if request.method == 'POST':
        #Salvar alimentacao_semana_un
        alimentacao_semana_un = request.POST.get('alimentacao_valor_semana')
        if alimentacao_semana_un:
            alimentacao_semana_un = str(alimentacao_semana_un)
            alimentacao_semana_un = alimentacao_semana_un.replace(',','.')
            escala.alimentacao_semana_un = alimentacao_semana_un
        
        #Salvar alimentacao_semana_qtd
        alimentacao_semana_qtd = request.POST.get('alimentacao_qtd_semana')
        if alimentacao_semana_qtd:
            alimentacao_semana_qtd = str(alimentacao_semana_qtd)
            alimentacao_semana_qtd = alimentacao_semana_qtd.replace(',','.')
            escala.alimentacao_semana_qtd = alimentacao_semana_qtd
        
        #Salvar alimentacao_fds_un
        alimentacao_fds_un = request.POST.get('alimentacao_valor_fds')
        if alimentacao_fds_un:
            alimentacao_fds_un = str(alimentacao_fds_un)
            alimentacao_fds_un = alimentacao_fds_un.replace(',','.')
            escala.alimentacao_fds_un = alimentacao_fds_un
        
        #Salvar alimentacao_fds_qtd
        alimentacao_fds_qtd = request.POST.get('alimentacao_qtd_fds')       
        if alimentacao_fds_qtd:
            alimentacao_fds_qtd = str(alimentacao_fds_qtd)
            alimentacao_fds_qtd = alimentacao_fds_qtd.replace(',','.')
            escala.alimentacao_fds_qtd = alimentacao_fds_qtd

        #Salvar mobilidade
        valor_mobilidade = request.POST.get('valor_mobilidade')       
        if valor_mobilidade:
            valor_mobilidade = str(valor_mobilidade)
            valor_mobilidade = valor_mobilidade.replace(',','.')
            escala.valor_mobilidade = valor_mobilidade
        
        #Salvar saida e retorno
        if escala.contrato == "FREELA":
            escala.saida = request.POST.get('saida')
            escala.retorno = request.POST.get('retorno')

        #Salvar deslocamento
        if escala.contrato == "FREELA":
            escala.valor_deslocamento = request.POST.get('deslocamento')
        else:
            escala.valor_deslocamento = "0"

        #Salvar status
        escala.status_fase3 = request.POST.get('status3')

        escala.save()

        #replicar em Realizado
        if escala.status_fase3 == "CONCLUÍDO":
            evento = get_object_or_404(Evento, id=escala.id_evento)

            realizado = Realizado.objects.create(
                escala=escala,
                id_evento=evento,
                nome_evento=escala.nome_evento,
                data_evento=escala.data_evento,
                id_colaborador=escala.id_colaborador,
                colaborador_name=escala.colaborador_name,
                nome_area=escala.nome_area,
                id_cargo=escala.id_cargo,
                nome_cargo=escala.nome_cargo,
                id_contrato=escala.id_contrato,
                contrato=escala.contrato,
                id_origem=escala.id_origem,
                origem=escala.origem,
                data_inicio=escala.data_inicio,
                data_final=escala.data_final,
                qtd_diaria=escala.qtd_diaria,
                r_qtd_diaria=escala.qtd_diaria, #realizado
                qtd_dias_pgto=escala.qtd_dias_pgto,
                r_qtd_dias_pgto=escala.qtd_dias_pgto,#realizado
                unidade_diaria=escala.unidade_diaria,
                r_unidade_diaria=escala.unidade_diaria,#realizado
                total_diaria=escala.total_diaria,
                r_total_diaria=escala.total_diaria, #realizado
                passagem=escala.passagem,
                valor_passagem=escala.valor_passagem,
                r_valor_passagem=escala.valor_passagem, #realizado
                hora_ida=escala.hora_ida,
                # r_hora_ida=escala.hora_ida, #realizado
                hora_volta=escala.hora_volta,
                # r_hora_volta=escala.hora_volta, #realizado
                meio_transporte=escala.meio_transporte,
                r_meio_transporte=escala.meio_transporte, #realizado
                companhia_aerea=escala.companhia_aerea,
                r_companhia_aerea=escala.companhia_aerea, #realizado
                loc_voo=escala.loc_voo,
                alimentacao_semana_un=escala.alimentacao_semana_un,
                r_alimentacao_semana_un=escala.alimentacao_semana_un, #realizado
                alimentacao_semana_qtd=escala.alimentacao_semana_qtd,
                r_alimentacao_semana_qtd=escala.alimentacao_semana_qtd, #realizado
                alimentacao_fds_un=escala.alimentacao_fds_un,
                r_alimentacao_fds_un=escala.alimentacao_fds_un, #realizado
                alimentacao_fds_qtd=escala.alimentacao_fds_qtd,
                r_alimentacao_fds_qtd=escala.alimentacao_fds_qtd, #realizado
                alimentacao_total=escala.alimentacao_total,
                r_alimentacao_total=escala.alimentacao_total, #realizado
                valor_mobilidade=escala.valor_mobilidade,
                r_valor_mobilidade=escala.valor_mobilidade, #realizado
                saida=escala.saida,
                retorno=escala.retorno,
                valor_deslocamento=escala.valor_deslocamento,
                r_valor_deslocamento=escala.valor_deslocamento,
                valor_hotel=escala.valor_hotel,
                r_valor_hotel=escala.valor_hotel,
                status_fase1=escala.status_fase1,
                status_fase2=escala.status_fase2,
                status_fase3=escala.status_fase3,
            )
            print(f"Criada nova escala: {realizado}")


        return redirect('beneficios')
    return render(request, 'beneficios/update_beneficios.html', {'escala': escala})