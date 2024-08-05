from django.shortcuts import render
from django.shortcuts import redirect 
from ..models import Escala, Evento, Area, Tipo_contrato
from ..forms import EscalaForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta


@login_required
@login_required
def criar_quantitativo(request):
    eventos = Evento.objects.all()
    escalas = Escala.objects.all()
    areas = Area.objects.all()
    contratos = Tipo_contrato.objects.all()

    if request.method == 'POST':
        # Captura dos dados dos formulários enviados
        event_ids = request.POST.getlist("evento_select")
        area_ids = request.POST.getlist("area_select")
        contrato_ids = request.POST.getlist("contrato_select")
        quantities = request.POST.getlist("quantity_select")
        sug_hora_ida = request.POST.getlist("sugestao_ida")
        sug_hora_volta = request.POST.getlist("sugestao_volta")
        dt_inicio = request.POST.getlist("data_inicio")
        dt_fim = request.POST.getlist("data_fim")
        passa = request.POST.getlist("passagem_select")
        dt_ida = request.POST.getlist("data_ida")
        dt_volta = request.POST.getlist("data_volta")

        # Para cada formulário enviado
        for event_id, area_id, contrato_id, quantity in zip(event_ids, area_ids, contrato_ids, quantities):
            evento = Evento.objects.get(pk=event_id)
            area = Area.objects.get(pk=area_id)
            contrato = Tipo_contrato.objects.get(pk=contrato_id)
            multiplicador = int(quantity)

            for _ in range(multiplicador):
                nome_evento_completo = f"{evento.nome} - {evento.cidade}"
                data_final_obj = datetime.strptime(dt_fim[0], '%Y-%m-%d')
                data_inicio_obj = datetime.strptime(dt_inicio[0], '%Y-%m-%d')
                delta = data_final_obj - data_inicio_obj
                data_final_obj_wk = data_final_obj.weekday()
                if data_final_obj_wk == 6 and contrato.nome == "CASA": 
                    delta_pg = 2
                elif data_final_obj_wk == 5 and contrato.nome == "CASA": 
                    delta_pg = 1
                elif contrato.nome == "HUB": 
                    delta_pg = 0
                else: delta_pg = delta.days + 1
                nova_escala = Escala.objects.create(
                    id_evento=event_id,
                    nome_evento=nome_evento_completo,
                    data_evento=evento.data,
                    id_area_id=area_id,
                    nome_area=area.nome,
                    id_contrato_id=contrato_id,
                    contrato=contrato.nome,
                    sugestao_hora_ida=sug_hora_ida[0] if sug_hora_volta else None,
                    sugestao_hora_volta=sug_hora_volta[0] if sug_hora_volta else None,
                    data_inicio=dt_inicio[0],
                    data_final=dt_fim[0],
                    passagem=passa[0],
                    data_ida=dt_ida[0] if dt_ida else None,
                    data_volta=dt_volta[0] if dt_volta else None,
                    qtd_diaria = delta.days + 1,
                    qtd_dias_pgto=delta_pg
                )
                print(f"Criada nova escala: {nova_escala}")

        return redirect('quantitativo')  

    return render(request, 'quantitativo/quantitativo.html', {'eventos': eventos, 'escalas': escalas, 'areas': areas, 'contratos': contratos})

@login_required
def deletar_quantitativo(request, pk):
    escalas = Escala.objects.get(id = pk)
    if request.method == 'POST':
        escalas.delete()
        return redirect('quantitativo')
    return render(request, 'quantitativo/delete_quantitativo.html', {'escala': escalas})