from django.shortcuts import render
from django.shortcuts import redirect 
from ..models import Area, Colaborador, Tipo_contrato, Cargo
from ..forms import ColaboradorForm
from django.contrib.auth.decorators import login_required
from django.forms.utils import ErrorList


@login_required
def visualizar_colaborador(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'colaborador/colaborador.html', {'colaboradores': colaboradores})

@login_required
def c_colaborador(request):
    colaboradores = Colaborador.objects.all()
    areas = Area.objects.all()
    cargos = Cargo.objects.all()
    tipos = Tipo_contrato.objects.all()

    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data.get("nome")
            sobrenome = form.cleaned_data.get("sobrenome")
            area_id = form.cleaned_data.get("area")
            cargo_id = form.cleaned_data.get("cargo")
            tipo_id = form.cleaned_data.get("tipo")
            rg = form.cleaned_data.get("rg")
            cpf = form.cleaned_data.get("cpf")
            telefone = form.cleaned_data.get("telefone")
            cidade = form.cleaned_data.get("cidade")
            data_nascimento = form.cleaned_data.get("data_nascimento")
            
            Colaborador.objects.create(
                nome=nome,
                sobrenome=sobrenome,
                rg=rg,
                cpf=cpf,
                telefone=telefone,
                cidade=cidade,
                data_nascimento=data_nascimento
            )

            return redirect('colaborador')
        else:
            print("Formulário inválido")
            print(form.errors)
    else:
        form = ColaboradorForm()

    return render(request, 'colaborador/cadastrar_colaborador.html', {
        'colaboradores': colaboradores,
        'areas': areas,
        'cargos': cargos,
        'tipos': tipos,
        'form': form,
        }
    )

@login_required
def deletar_colaborador(request, pk):
    colaboradores = Colaborador.objects.get(id = pk)
    if request.method == 'POST':
        colaboradores.delete()
        return redirect('colaborador')
    return render(request, 'colaborador/delete_colaborador.html', {'colaborador': colaboradores})

def atualizar_colaborador(request, pk):
    colaborador = Colaborador.objects.get(id=pk)
    areas = Area.objects.all()
    cargos = Cargo.objects.all()
    tipos = Tipo_contrato.objects.all()
    form = ColaboradorForm(instance=colaborador)
    if request.method == "POST":
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('colaborador') 
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Erro no campo '{field}': {error}")
    return render(request, 'colaborador/update_colaborador.html', {'form': form, 'colaborador': colaborador, 'areas': areas, 'cargos':cargos, 'tipos': tipos})