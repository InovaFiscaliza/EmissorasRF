# AUTOGENERATED! DO NOT EDIT! File to edit: constants.ipynb (unless otherwise specified).

__all__ = ['console', 'ESTADOS', 'SIGLAS', 'REGEX_ESTADOS', 'TIMEOUT', 'RELATORIO', 'ESTACOES', 'ESTACAO',
           'PLANO_BASICO', 'HISTORICO', 'REJECT_ESTACOES', 'COL_ESTACOES', 'NEW_ESTACOES', 'COL_PB', 'NEW_PB',
           'TELECOM', 'RADIODIFUSAO', 'APP_ANALISE', 'ENTIDADES', 'RADCOM', 'STEL']

# Cell
from rich.console import Console

console = Console()

# Cell
ESTADOS = [
    "AC",
    "AL",
    "AP",
    "AM",
    "BA",
    "CE",
    "ES",
    "GO",
    "MA",
    "MT",
    "MS",
    "MG",
    "PA",
    "PB",
    "PR",
    "PE",
    "PI",
    "RJ",
    "RN",
    "RS",
    "RO",
    "RR",
    "SC",
    "SP",
    "SE",
    "TO",
    "DF",
]

SIGLAS = {
    "Acre": "AC",
    "Alagoas": "AL",
    "Amapá": "AP",
    "Amazonas": "AM",
    "Bahia": "BA",
    "Ceará": "CE",
    "Espírito Santo": "ES",
    "Goiás": "GO",
    "Maranhão": "MA",
    "Mato Grosso": "MT",
    "Mato Grosso do Sul": "MS",
    "Minas Gerais": "MG",
    "Pará": "PA",
    "Paraíba": "PB",
    "Paraná": "PR",
    "Pernambuco": "PE",
    "Piauí": "PI",
    "Rio de Janeiro": "RJ",
    "Rio Grande do Norte": "RN",
    "Rio Grande do Sul": "RS",
    "Rondônia": "RO",
    "Roraima": "RR",
    "Santa Catarina": "SC",
    "São Paulo": "SP",
    "Sergipe": "SE",
    "Tocantins": "TO",
    "Distrito Federal": "DF",
}

REGEX_ESTADOS = f'({"|".join(ESTADOS)})'

# Cell
TIMEOUT = 5
RELATORIO = "http://sistemas.anatel.gov.br/se/eApp/reports/b/srd/resumo_sistema.php?id={id}&state={state}"
ESTACOES = "http://sistemas.anatel.gov.br/se/public/file/b/srd/estacao_rd.zip"
ESTACAO = "http://sistemas.anatel.gov.br/se/public/view/b/srd.php?wfid=estacoes&id={}"
PLANO_BASICO = "http://sistemas.anatel.gov.br/se/public/file/b/srd/Canais.zip"
HISTORICO = (
    "http://sistemas.anatel.gov.br/se/public/file/b/srd/documento_historicos.zip"
)
REJECT_ESTACOES = [
    "atenuacao",
    "historico_documentos",
    "estacao_auxiliar",
    "rds",
    "aprovacao_locais",
    "item",
]
COL_ESTACOES = (
    "siglaservico",
    "num_servico",
    "state",
    "entidade",
    "fistel",
    "municipio",
    "uf",
    "id",
    "numero_estacao",
    "latitude",
    "longitude",
    "cnpj",
    "habilitacao_datavalfreq",
)
NEW_ESTACOES = [
    "Serviço",
    "Num_Serviço",
    "Status",
    "Entidade",
    "Fistel",
    "Município",
    "UF",
    "Id",
    "Número_da_Estação",
    "Latitude_Transmissor",
    "Longitude_Transmissor",
    "CNPJ",
    "Validade_RF",
    "Num_Ato",
    "Data_Ato",
]
COL_PB = (
    "id",
    "municipio",
    "frequencia",
    "classe",
    "servico",
    "entidade",
    "latitude",
    "longitude",
    "uf",
    "status",
    "cnpj",
    "fistel",
    'canal'
)
NEW_PB = (
    "Id",
    "Município",
    "Frequência",
    "Classe",
    "Serviço",
    "Entidade",
    "Latitude_Estação",
    "Longitude_Estação",
    "UF",
    "Status",
    "CNPJ",
    "Fistel",
    "Canal"
)
TELECOM = (
    "Frequência",
    "Serviço",
    "Entidade",
    "Fistel",
    "Número da Estação",
    "Município",
    "UF",
    "Latitude",
    "Longitude",
    "Validade_RF"
)
RADIODIFUSAO = (
    "Frequência",
    "Num_Serviço",
    "Status",
    "Classe",
    "Entidade",
    "Fistel",
    "Número_da_Estação",
    "Município",
    "UF",
    "Latitude",
    "Longitude",
    "Validade_RF",
    "Num_Ato",
    "Data_Ato",
)

APP_ANALISE = (
    "Frequency",
    "Latitude",
    "Longitude",
    "Description",
    "Service",
    "Station",
    "ActNumber",
    "ActDate",
    "ValRF",
)

ENTIDADES = {}

# Cell
RADCOM = """
       select f.MedFrequenciaInicial as 'Frequência',
       Sitarweb.dbo.FN_SRD_RetornaIndFase(PB.NumServico, Pr.idtPedidoRadcom) as 'Fase',
       Sitarweb.dbo.FN_SRD_RetornaSiglaSituacao(h.IdtHabilitacao, Es.IdtEstacao) as 'Situação',
       uf.SiglaUnidadeFrequencia as 'Unidade',
       e.NomeEntidade as 'Entidade',
       h.NumFistel as 'Fistel',
       es.NumEstacao as 'Número da Estação',
       m.NomeMunicipio as 'Município',
       pb.SiglaUF as 'UF',
       es.MedLatitudeDecimal as 'Latitude',
       es.MedLongitudeDecimal as 'Longitude',
       e.NumCnpjCpf as 'CNPJ'
from ENTIDADE e
inner join HABILITACAO h on h.IdtEntidade = e.IdtEntidade
inner join SRD_PEDIDORADCOM pr on pr.IdtHabilitacao = h.IdtHabilitacao
inner join SRD_PLANOBASICO pb on pb.IdtPlanoBasico = pr.IdtPlanoBasico
inner join estacao es on es.IdtHabilitacao = h.IdtHabilitacao
inner join FREQUENCIA f on f.IdtEstacao = es.IdtEstacao
inner join UnidadeFrequencia uf on uf.IdtUnidadeFrequencia = f.IdtUnidadeFrequencia
inner join Municipio m on m.CodMunicipio = pb.CodMunicipio
where h.NumServico = '231'
"""

# Cell
STEL = """IF OBJECT_ID('tempDB..##faixas','U') is not null
drop table ##faixas
create table ##faixas (id int not null, faixa varchar(20), inic float, fim float,);
insert into ##faixas values(0,'De 20 MHz - 6 GHz','20000', '6000000');

select distinct f.MedTransmissaoInicial as 'Frequência',
uf.SiglaUnidadeFrequencia as 'Unidade',
d.CodClasseEmissao as 'ClasseEmissao',
d.SiglaLarguraEmissao as 'LarguraEmissao',
ce.CodTipoClasseEstacao as 'ClasseEstacao',
e.NumServico as 'Serviço',
ent.NomeEntidade as 'Entidade',
h.NumFistel as 'Fistel',
e.NumEstacao as 'Número da Estação',
mu.NomeMunicipio as 'Município',
e.SiglaUf as 'UF',
e.MedLatitudeDecimal as 'Latitude',
e.MedLongitudeDecimal as 'Longitude',
ent.NumCnpjCpf as 'CNPJ',
c.DataValidadeRadiofrequencia as 'Validade_RF',
from contrato c
inner join estacao e on e.IdtContrato = c.Idtcontrato
inner join frequencia f on f.IdtEstacao = e.IdtEstacao
inner join CLASSEESTACAO ce on ce.IdtFrequencia = f.IdtFrequencia
inner join DESIGNACAOEMISSAO d  on d.IdtClasseEstacao = ce.IdtClasseEstacao
inner join HABILITACAO h on h.IdtHabilitacao = c.IdtHabilitacao
inner join entidade ent on ent.IdtEntidade = h.IdtEntidade
inner join endereco en on en.IdtEstacao = e.IdtEstacao
inner join Municipio mu on mu.CodMunicipio = en.CodMunicipio
inner join Servico s on s.NumServico = h.NumServico and s.IdtServicoAreaAtendimento = 4
left join UnidadeFrequencia uf on uf.IdtUnidadeFrequencia = f.IdtUnidadeTransmissao
left outer join ##faixas fx on (
(fx.inic <= f.MedRecepcaoInicialKHz and fx.fim >= f.MedRecepcaoInicialKHz)
or (fx.inic <= f.MedTransmissaoInicialKHz and fx.fim >= f.medtransmissaoinicialkhz)
or (fx.inic <= f.MedFrequenciaInicialKHz and fx.fim >= f.MedFrequenciaInicialKHz)
or (fx.inic <= f.MedFrequenciaFinalKHz and fx.fim >= f.MedFrequenciaFinalKHz)
)
where e.DataExclusao is null
and fx.faixa is not null
and f.MedTransmissaoInicial is not null
and f.CodStatusRegistro = 'L'
and e.IndStatusEstacao = 'L'
and h.NumServico <> '010'
order by 'Frequência'
"""