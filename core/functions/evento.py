from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect 
from ..models import *
from django.contrib.auth.decorators import login_required
from ..forms import EventoForm


@login_required
def deletar_evento(request, pk):
    evento = Evento.objects.get(id=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('cadastrar_evento')
    return render(request, 'evento/delete_evento.html', {'evento': evento})


@login_required
def cadastrar_evento(request):
    if request.method == 'POST':
        evento_form = EventoForm(request.POST)
        if evento_form.is_valid():
            evento_form.save()
            return redirect('cadastrar_evento')  
    else:
        evento_form = EventoForm()
    eventos = Evento.objects.all()
    return render(request, 'evento/cadastrar_evento.html', {'eventos': eventos, 'form': evento_form})


@login_required
def atualizar_evento(request, pk):
    evento = Evento.objects.get(id=pk)
    form = EventoForm(instance=evento)
    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento atualizado com sucesso.')
            return redirect('cadastrar_evento')  
        else:
            messages.error(request, 'Erro ao atualizar o evento. Por favor, corrija os erros abaixo.')
    return render(request, 'evento/update_evento.html', {'form': form, 'evento': evento})