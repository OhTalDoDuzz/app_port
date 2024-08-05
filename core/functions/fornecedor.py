from django.shortcuts import render
from django.shortcuts import redirect 
from ..models import Fornecedor
from ..forms import FornecedorForm
from django.contrib.auth.decorators import login_required

@login_required
def  visualizar_fornecedor(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedor/fornecedor.html', {'fornecedores': fornecedores})

@login_required
def cadastrar_fornecedor(request):
    fornecedores = Fornecedor.objects.all()
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            cnpj = form.cleaned_data.get("cnpj") 
            cpf = form.cleaned_data.get("cpf")
            servico = form.cleaned_data.get("servico")
            
            Fornecedor.objects.create(
                name=name,
                cnpj=cnpj,
                cpf=cpf,
                servico=servico,
            )

            return redirect('fornecedor')
        else:
            print("Formulário inválido")
            print(form.errors)
    else:
        form = FornecedorForm()

    return render(request, 'fornecedor/cadastrar_fornecedor.html', {
        'fornecedores': fornecedores,
        'form': form,
    })

@login_required
def deletar_fornecedor(request, pk):
    fornecedores = Fornecedor.objects.get(id = pk)
    if request.method == 'POST':
        fornecedores.delete()
        return redirect('fornecedor')
    return render(request, 'fornecedor/delete_fornecedor.html', {'fornecedor': fornecedores})

@login_required
def atualizar_fornecedor(request, pk):
    fornecedor = Fornecedor.objects.get(id = pk)
    form = FornecedorForm(instance=fornecedor)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('fornecedor')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Erro no campo '{field}': {error}")
    return render(request, 'fornecedor/update_fornecedor.html', {'form': form, 'fornecedor': fornecedor})

