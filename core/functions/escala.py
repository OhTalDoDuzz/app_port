from datetime import datetime
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from ..models import *

@login_required
def atualizar_escala(request, escala_id):
    escala = get_object_or_404(Escala, pk=escala_id)
    colaboradores = Colaborador.objects.all()
    cargos = Cargo.objects.all()
    contratos = Tipo_contrato.objects.all()
    origens = Origem.objects.all()

    if request.method == 'POST':
        # Salvar colaborador
        colaborador_id = request.POST.get('name')
        if colaborador_id:
            colaborador = get_object_or_404(Colaborador, pk=colaborador_id)
            escala.id_colaborador = colaborador_id
            escala.colaborador_name = f"{colaborador.nome} {colaborador.sobrenome}"

        # Salvar cargo
        cargo_id = request.POST.get('cargo')
        if cargo_id:
            cargo = get_object_or_404(Cargo, pk=cargo_id)
            escala.id_cargo = cargo  # Atribuir a instância de Cargo
            escala.nome_cargo = cargo.nome

        # Salvar contrato
        contrato_id = request.POST.get('contrato')
        if contrato_id:
            contrato = get_object_or_404(Tipo_contrato, pk=contrato_id)
            escala.id_contrato = contrato
            escala.contrato = contrato.nome

        # Salvar origem
        origem_id = request.POST.get('origem')
        if origem_id:
            origem = get_object_or_404(Origem, pk=origem_id)
            escala.id_origem = origem
            escala.origem = origem.name

        # Salvar quantidade de dias de pagamento
        escala.qtd_dias_pgto = request.POST.get('qtd_dias_pgto', escala.qtd_dias_pgto)
        

        #Tratamento Unidade diaria
        mapeamento_valores = {
            ("PERCURSO", "NIVEL 1", "FREELA", "LOCAL SP"): "1.129,76",
            ("PERCURSO", "NIVEL 1", "FREELA", "EM VIAGEM"): "1.129,76",
            ("PERCURSO", "NIVEL 2", "FREELA", "LOCAL SP"): "1.266,67",
            ("PERCURSO", "NIVEL 2", "FREELA", "EM VIAGEM"): "1.266,67",
            ("PRODUÇÃO", "DIRETOR DE PROVA", "CASA", "LOCAL SP"): "680",
            ("PRODUÇÃO", "DIRETOR DE PROVA", "CASA", "EM VIAGEM"): "680",
            ("PRODUÇÃO", "COORDENADOR", "CASA", "LOCAL SP"): "525",
            ("PRODUÇÃO", "COORDENADOR", "CASA", "EM VIAGEM"): "525",
            ("PRODUÇÃO", "PRODUTOR", "CASA", "LOCAL SP"): "420",
            ("PRODUÇÃO", "PRODUTOR", "CASA", "EM VIAGEM"): "420",
            ("PRODUÇÃO", "DIRETOR DE PROVA", "FREELA", "LOCAL SP"): "680",
            ("PRODUÇÃO", "DIRETOR DE PROVA", "FREELA", "EM VIAGEM"): "680",
            ("PRODUÇÃO", "PRODUTOR", "FREELA", "LOCAL SP"): "420",
            ("PRODUÇÃO", "PRODUTOR", "FREELA", "EM VIAGEM"): "470",
            ("PRODUÇÃO", "DIRETOR DE PROVA", "HUB", "LOCAL SP"): "0",
            ("PRODUÇÃO", "DIRETOR DE PROVA", "HUB", "EM VIAGEM"): "0",
            ("PRODUÇÃO", "COORDENADOR", "HUB", "LOCAL SP"): "0",
            ("PRODUÇÃO", "COORDENADOR", "HUB", "EM VIAGEM"): "0",
            ("PRODUÇÃO", "PRODUTOR", "HUB", "LOCAL SP"): "0",
            ("PRODUÇÃO", "PRODUTOR", "HUB", "EM VIAGEM"): "0",
            ("ATIVAÇÃO", "COORDENADOR", "CASA", "LOCAL SP"): "525",
            ("ATIVAÇÃO", "COORDENADOR", "CASA", "EM VIAGEM"): "525",
            ("ATIVAÇÃO", "PRODUTOR", "CASA", "LOCAL SP"): "420",
            ("ATIVAÇÃO", "PRODUTOR", "CASA", "EM VIAGEM"): "420",
            ("ATIVAÇÃO", "PRODUTOR", "FREELA", "LOCAL SP"): "420",
            ("ATIVAÇÃO", "PRODUTOR", "FREELA", "EM VIAGEM"): "470",
            ("KIT", "COORDENADOR", "CASA", "LOCAL SP"): "525",
            ("KIT", "COORDENADOR", "CASA", "EM VIAGEM"): "525",
            ("KIT", "PRODUTOR", "CASA", "LOCAL SP"): "420",
            ("KIT", "PRODUTOR", "CASA", "EM VIAGEM"): "420",
            ("KIT", "PRODUTOR", "FREELA", "LOCAL SP"): "420",
            ("KIT", "PRODUTOR", "FREELA", "EM VIAGEM"): "470",
            ("ATENDIMENTO", "GERENTE", "CASA", "LOCAL SP"): "525",
            ("ATENDIMENTO", "GERENTE", "CASA", "EM VIAGEM"): "525",
            ("ATENDIMENTO", "COORDENADOR", "CASA", "LOCAL SP"): "420",
            ("ATENDIMENTO", "COORDENADOR", "CASA", "EM VIAGEM"): "420",
            ("COMERCIAL", "REPRESENTANTE", "CASA", "LOCAL SP"): "0",
            ("COMERCIAL", "REPRESENTANTE", "CASA", "EM VIAGEM"): "0",
            ("O2 PRIME", "REPRESENTANTE", "CASA", "LOCAL SP"): "250",
            ("O2 PRIME", "REPRESENTANTE", "CASA", "EM VIAGEM"): "250",  
            ("CENOGRAFIA", "COORDENADOR", "CASA", "LOCAL SP"): "525",
            ("CENOGRAFIA", "COORDENADOR", "CASA", "EM VIAGEM"): "525",
            ("CENOGRAFIA", "SUP CENO", "CASA", "LOCAL SP"): "420",
            ("CENOGRAFIA", "SUP CENO", "CASA", "EM VIAGEM"): "420",
            ("CENOGRAFIA", "SUP CENO", "FREELA", "EM VIAGEM"): "470",
            ("CENOGRAFIA", "CENOTÉCNICO", "CASA", "LOCAL FORA"): "300",
            ("CENOGRAFIA", "CENOTÉCNICO", "CASA", "EM VIAGEM"): "0",
            ("CENOGRAFIA", "CENOTÉCNICO", "FREELA", "LOCAL SP"): "275",
            ("CENOGRAFIA", "CENOTÉCNICO", "FREELA", "EM VIAGEM"): "325"
        }

        chave = (escala.nome_area, escala.nome_cargo, escala.contrato, escala.origem)

        if chave in mapeamento_valores:
            escala.unidade_diaria = mapeamento_valores[chave]
        else:
            escala.unidade_diaria = Decimal("0.00")

        # Calcular total diária
        qtd_pgto_str = escala.qtd_dias_pgto
        qtd_pgto_str = qtd_pgto_str.replace(",", ".")
        qtd_pgto = Decimal(qtd_pgto_str)

        unidade_diaria_str = escala.unidade_diaria
        unidade_diaria_str = str(escala.unidade_diaria).replace(",", ".")
        unidade_diaria = Decimal(unidade_diaria_str)

        if escala.contrato == "FREELA":
            qtd_pgto = int(qtd_pgto_str)
            defrator1 = Decimal(1)
            defrator2 = Decimal(0.9)
            defrator3 = Decimal(0.8)
            valores = []
            for i in range(qtd_pgto):
                valor = unidade_diaria
                if i < 4:
                    valor *= defrator1
                elif 4 <= i < 8:
                    valor *= defrator2
                else:
                    valor *= defrator3
                valores.append(valor)
            final = sum(valores)
            escala.total_diaria = final
        else:
            total_diaria = qtd_pgto * unidade_diaria

            escala.total_diaria = total_diaria

        #Salvar alimentação semana uni
        if escala.contrato == "CASA" and escala.nome_cargo not in ["GERENTE", "REPRESENTANTE"]:
            unidade_semana = 8
            escala.alimentacao_semana_un = unidade_semana
        else:
            escala.alimentacao_semana_un = 0

        #Salvar alimentação semana qtd
        data_inicio = escala.data_inicio
        data_final = escala.data_final

        contador_dias_semana = 0
        
        delta = timedelta(days=1)
        data_atual = data_inicio
        if escala.contrato == "FREELA":
            alimentacao_semana_qtd = 0        
            escala.alimentacao_semana_qtd = alimentacao_semana_qtd
        else:               
            while data_atual <= data_final:
                dia_semana = data_atual.weekday()
                
                if dia_semana < 5:  
                    contador_dias_semana += 1

                data_atual += delta
            escala.alimentacao_semana_qtd = contador_dias_semana
        
        #Salvar alimentação fds uni
        if escala.contrato == "CASA" and escala.nome_area not in ["CENOGRAFIA"]:
            unidade_fds = 34
            escala.alimentacao_fds_un = unidade_fds
        elif escala.contrato == "CASA" and escala.nome_area in ["CENOGRAFIA"]:
            unidade_fds = 29
            escala.alimentacao_fds_un = unidade_fds
        else:
            escala.alimentacao_fds_un = 0

        #Salvar alimentação fds qtd
        data_inicio = escala.data_inicio
        data_final = escala.data_final

        contador_fds = 0

        delta = timedelta(days=1)
        data_atual = data_inicio

        if escala.contrato == "FREELA":
            alimentacao_fds_qtd = 0        
            escala.alimentacao_fds_qtd = alimentacao_fds_qtd
        else:   
            while data_atual <= data_final:
                dia_semana = data_atual.weekday()
                
                if dia_semana == 5 or dia_semana == 6: 
                    contador_fds += 1

                data_atual += delta

            escala.alimentacao_fds_qtd = contador_fds

        #Salvar total alimentação
        total_semana = escala.alimentacao_semana_un * escala.alimentacao_semana_qtd
        total_fds = escala.alimentacao_fds_un * escala.alimentacao_fds_qtd

        total_alimentaçao = total_semana + total_fds
        escala.alimentacao_total = total_alimentaçao

        #Salvar deslocamento
        if escala.contrato == "CASA":
            escala.saida = "NÃO ELEGÍVEL"
            escala.retorno = "NÃO ELEGÍVEL"
            escala.valor_deslocamento = 0
        else:
            escala.saida = ""
            escala.retorno = ""
            escala.valor_deslocamento = 0
        
        #Salvar passagem
        evento = get_object_or_404(Evento, pk=escala.id_evento)
        if evento.cidade != "São Paulo" and escala.origem != "LOCAL FORA":
            escala.passagem = True
        else:
            escala.passagem = False

        #Mudar status
        escala.status_fase1 = request.POST.get('status')

        if escala.passagem == False:
            escala.status_fase2 = request.POST.get('status')
        
        escala.save()
        return redirect('escalacao')

    return render(request, 'escala/update_escala.html', {
        'escala': escala,
        'colaboradores': colaboradores,
        'cargos': cargos,
        'contratos': contratos,
        'origens': origens
    })

@login_required
def deletar_escala(request, pk):
    escalas = Escala.objects.get(id = pk)
    if request.method == 'POST':
        escalas.delete()
        return redirect('escalacao')
    return render(request, 'escala/delete_escala.html', {'escala': escalas})

@login_required
def visualizar_escalacao(request):
    escalas = Escala.objects.all()
    form = None 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('escalacao')
    return render(request, 'escala/escalacao.html', {'escalas': escalas, 'form': form}) 