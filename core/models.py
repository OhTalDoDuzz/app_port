from django.db import models

# Create your models here.

class Area(models.Model):
    id = models.AutoField(primary_key=True)  
    nome = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id} - {self.nome}"


class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    data = models.DateField()
    tipo = models.CharField(max_length=100)
    sku = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.nome} - [{self.data}]"


class Permissao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome}"
    

class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id} - {self.nome}"
    

class Tipo_contrato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome}"


class Colaborador(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Origem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
    

class Escala(models.Model):
    id = models.AutoField(primary_key=True)
    id_evento = models.CharField(max_length=100, null=True, blank=True) 
    nome_evento = models.CharField(max_length=100, null=True, blank=True) 
    data_evento = models.DateField(null=True, blank=True)
    id_colaborador = models.CharField(max_length=100, null=True, blank=True)
    colaborador_name = models.CharField(max_length=100, null=True, blank=True)
    id_area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True)
    nome_area = models.CharField(max_length=100, null=True, blank=True) 
    id_cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, blank=True)
    nome_cargo = models.CharField(max_length=100, null=True, blank=True)
    id_contrato = models.ForeignKey(Tipo_contrato, on_delete=models.SET_NULL, null=True, blank=True)
    contrato = models.CharField(max_length=100, null=True, blank=True)
    id_origem = models.ForeignKey(Origem, on_delete=models.SET_NULL, null=True, blank=True)
    origem = models.CharField(max_length=100, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)
    qtd_diaria = models.IntegerField(default=0, null=True, blank=True)
    qtd_dias_pgto = models.CharField(max_length=100, null=True, blank=True)
    unidade_diaria = models.CharField(max_length=100, null=True, blank=True)
    total_diaria = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    passagem = models.BooleanField(null=True, blank=True) 
    valor_passagem = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    alimentacao_semana_un = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    alimentacao_semana_qtd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    alimentacao_fds_un = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    alimentacao_fds_qtd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    alimentacao_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    hora_ida = models.TimeField(null=True, blank=True) 
    hora_volta = models.TimeField(null=True, blank=True) 
    valor_mobilidade = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    saida = models.CharField(max_length=100, null=True, blank=True) 
    retorno = models.CharField(max_length=100, null=True, blank=True) 
    meio_transporte = models.CharField(max_length=100, null=True, blank=True) 
    companhia_aerea = models.CharField(max_length=100, null=True, blank=True) 
    loc_voo = models.CharField(max_length=100, null=True, blank=True) 
    valor_deslocamento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_hotel = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) #TODO: add
    status_fase1 = models.CharField(max_length=100, null=True, blank=True, default="PENDENTE")
    status_fase2 = models.CharField(max_length=100, null=True, blank=True, default="PENDENTE")
    status_fase3 = models.CharField(max_length=100, null=True, blank=True, default="PENDENTE")
    sugestao_hora_ida = models.CharField(max_length=100, null=True, blank=True)
    sugestao_hora_volta = models.CharField(max_length=100, null=True, blank=True)
    data_ida = models.DateField(null=True, blank=True)
    data_volta = models.DateField(null=True, blank=True)
    tipo_quarto = models.CharField(max_length=100, null=True, blank=True)
    nome_hotel = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.nome_evento} - {self.colaborador_name} - {self.nome_area}"


class Fornecedor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    cnpj = models.CharField(max_length=14)
    cpf = models.CharField(max_length=11, null=True)
    servico = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.name} - {self.cnpj}"
    
class Realizado(models.Model):
    id = models.AutoField(primary_key=True)
    escala = models.ForeignKey(Escala, on_delete=models.DO_NOTHING)
    id_evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True)
    nome_evento = models.CharField(max_length=100, null=True, blank=True)
    data_evento = models.DateField(null=True, blank=True)
    id_colaborador = models.CharField(max_length=100, null=True, blank=True)
    colaborador_name = models.CharField(max_length=100, null=True, blank=True) 
    nome_area = models.CharField(max_length=100, null=True, blank=True) 
    id_cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, blank=True)
    nome_cargo = models.CharField(max_length=100, null=True, blank=True)
    id_contrato = models.ForeignKey(Tipo_contrato, on_delete=models.SET_NULL, null=True, blank=True)
    contrato = models.CharField(max_length=100, null=True, blank=True)
    id_origem = models.ForeignKey(Origem, on_delete=models.SET_NULL, null=True, blank=True)
    origem = models.CharField(max_length=100, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)
    qtd_diaria = models.IntegerField(default=0, null=True, blank=True)
    r_qtd_diaria = models.IntegerField(default=0, null=True, blank=True)
    qtd_dias_pgto = models.CharField(max_length=100, null=True, blank=True)
    r_qtd_dias_pgto = models.CharField(max_length=100, null=True, blank=True)
    unidade_diaria = models.CharField(max_length=100, null=True, blank=True)
    r_unidade_diaria = models.CharField(max_length=100, null=True, blank=True)
    total_diaria = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    r_total_diaria = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    passagem = models.BooleanField(null=True, blank=True) 
    valor_passagem = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    r_valor_passagem = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    alimentacao_semana_un = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    r_alimentacao_semana_un = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    alimentacao_semana_qtd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    r_alimentacao_semana_qtd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    alimentacao_fds_un = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    r_alimentacao_fds_un = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    alimentacao_fds_qtd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    r_alimentacao_fds_qtd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    alimentacao_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    r_alimentacao_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hora_ida = models.TimeField(null=True, blank=True)
    # r_hora_ida = models.TimeField(null=True, blank=True)
    hora_volta = models.TimeField(null=True, blank=True)
    # r_hora_volta = models.TimeField(null=True, blank=True)
    valor_mobilidade = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    r_valor_mobilidade = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    saida = models.CharField(max_length=100, null=True, blank=True)
    # r_saida = models.CharField(max_length=100, null=True, blank=True)
    retorno = models.CharField(max_length=100, null=True, blank=True)
    # r_retorno = models.CharField(max_length=100, null=True, blank=True)
    meio_transporte = models.CharField(max_length=100, null=True, blank=True)
    r_meio_transporte = models.CharField(max_length=100, null=True, blank=True) 
    companhia_aerea = models.CharField(max_length=100, null=True, blank=True)
    r_companhia_aerea = models.CharField(max_length=100, null=True, blank=True) 
    loc_voo = models.CharField(max_length=100, null=True, blank=True)
    valor_deslocamento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    r_valor_deslocamento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_hotel = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) #TODO: add
    r_valor_hotel = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) #TODO: add
    status_fase1 = models.CharField(max_length=100, null=True, blank=True, default="PENDENTE")
    status_fase2 = models.CharField(max_length=100, null=True, blank=True, default="PENDENTE")
    status_fase3 = models.CharField(max_length=100, null=True, blank=True, default="PENDENTE")

    def __str__(self):
        return f"{self.nome_evento} - {self.colaborador_name}"
    

