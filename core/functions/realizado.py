from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from ..models import *
from ..forms import *
from django.contrib.auth.decorators import login_required

@login_required
def visualizar_realizado(request):
    realizado = Realizado.objects.all()
    return render(request, 'realizado/realizado.html', {'realizado': realizado})

def atualizar_realizado(request, pk):
    realizado = get_object_or_404(Realizado, pk=pk)

    if request.method == 'POST':
        realizado.r_qtd_diaria = request.POST.get('r_qtd_diaria')
        realizado.r_qtd_dias_pgto = request.POST.get('r_qtd_dias_pgto')
        realizado.r_unidade_diaria = request.POST.get('r_unidade_diaria')

        total_diaria = request.POST.get('r_total_diaria')
        if total_diaria:
            total_diaria = str(total_diaria)
            total_diaria = total_diaria.replace(',','.')
            realizado.r_total_diaria = total_diaria


        valor_passagem = request.POST.get('r_valor_passagem')
        if valor_passagem:
            valor_passagem = str(valor_passagem)
            valor_passagem = valor_passagem.replace(',','.')
            realizado.r_valor_passagem = valor_passagem

        realizado.r_meio_transporte = request.POST.get('r_meio_transporte')

        companhia = request.POST.get('r_companhia_aerea')
        if companhia:
            companhia = str(companhia)
            companhia = companhia.upper()
            realizado.r_companhia_aerea = companhia
        
        alimentacao_semana_un = request.POST.get('r_alimentacao_semana_un')
        if alimentacao_semana_un:
            alimentacao_semana_un = str(alimentacao_semana_un)
            alimentacao_semana_un = alimentacao_semana_un.replace(',', '.')
            realizado.r_alimentacao_semana_un = alimentacao_semana_un


        r_alimentacao_semana_qtd = request.POST.get('r_alimentacao_semana_qtd')
        if r_alimentacao_semana_qtd:
            r_alimentacao_semana_qtd = str(r_alimentacao_semana_qtd)
            r_alimentacao_semana_qtd = r_alimentacao_semana_qtd.replace(',','.')
            realizado.r_alimentacao_semana_qtd = r_alimentacao_semana_qtd

        r_alimentacao_fds_un = request.POST.get('r_alimentacao_fds_un')
        if r_alimentacao_fds_un:
            r_alimentacao_fds_un = str(r_alimentacao_fds_un)
            r_alimentacao_fds_un = r_alimentacao_fds_un.replace(',','.')
            realizado.r_alimentacao_fds_un = r_alimentacao_fds_un

        r_alimentacao_fds_qtd = request.POST.get('r_alimentacao_fds_qtd')
        if r_alimentacao_fds_qtd:
            r_alimentacao_fds_qtd = str(r_alimentacao_fds_qtd)
            r_alimentacao_fds_qtd = r_alimentacao_fds_qtd.replace(',','.')
            realizado.r_alimentacao_fds_qtd = r_alimentacao_fds_qtd
        
        r_alimentacao_total=request.POST.get('r_alimentacao_total')
        if r_alimentacao_total:
            r_alimentacao_total = str(r_alimentacao_total)
            r_alimentacao_total = r_alimentacao_total.replace(',','.')
            realizado.r_alimentacao_total = r_alimentacao_total

        r_valor_mobilidade = request.POST.get('r_valor_mobilidade')
        if r_valor_mobilidade:
            r_valor_mobilidade = str(r_valor_mobilidade)
            r_valor_mobilidade = r_valor_mobilidade.replace(',','.')
            realizado.r_valor_mobilidade = r_valor_mobilidade

        r_valor_deslocamento = request.POST.get('r_valor_deslocamento')
        if r_valor_deslocamento:
            r_valor_deslocamento = str(r_valor_deslocamento)
            r_valor_deslocamento = r_valor_deslocamento.replace(',','.')
            realizado.r_valor_deslocamento = r_valor_deslocamento

        # #Voltar Fase
        # voltar_fase = request.POST.get('voltar_fase')
        # if voltar_fase == "true":
        #     realizado.status_fase1 = "PENDENTE"

        #     Realizado.objects.create()

        realizado.save()

        return redirect('realizado')
    return render(request, 'realizado/update_realizado.html', {'realizado': realizado})