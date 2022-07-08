# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/constants.ipynb (unless otherwise specified).

__all__ = ['TIMEOUT', 'RELATORIO', 'ESTACOES', 'ESTACAO', 'PLANO_BASICO', 'HISTORICO', 'REJECT_ESTACOES',
           'COL_ESTACOES', 'NEW_ESTACOES', 'COL_PB', 'NEW_PB', 'SRD', 'TELECOM', 'RADIODIFUSAO', 'APP_ANALISE',
           'ESTADOS', 'ENTIDADES', 'SIGLAS', 'BW', 'BW_MAP', 'RADCOM', 'STEL', 'BW_pattern', 'REGEX_ESTADOS']

# Cell
import re

# Cell
TIMEOUT = 5
RELATORIO = "http://sistemas.anatel.gov.br/se/eApp/reports/b/srd/resumo_sistema.php?id={id}&state={state}"
ESTACOES = "http://sistemas.anatel.gov.br/se/public/file/b/srd/estacao_rd.zip"
ESTACAO = "http://sistemas.anatel.gov.br/se/public/view/b/srd.php?wfid=estacoes&id={}"
PLANO_BASICO = "http://sistemas.anatel.gov.br/se/public/file/b/srd/Canais.zip"
HISTORICO = "http://sistemas.anatel.gov.br/se/public/file/b/srd/documento_historicos.zip"

# Cell
REJECT_ESTACOES = (
    "atenuacao",
    "historico_documentos",
    "estacao_auxiliar",
    "rds",
    "aprovacao_locais",
    "item",
)
COL_ESTACOES = (
    "siglaservico",
    "num_servico",
    "state",
    "entidade",
    "fistel",
    "uf",
    "id",
    "numero_estacao",
    "latitude",
    "longitude",
    "cnpj",
    "habilitacao_datavalfreq",
)
NEW_ESTACOES = (
    "Serviço",
    "Num_Serviço",
    "Status",
    "Entidade",
    "Fistel",
    "UF",
    "Id",
    "Número_Estação",
    "Latitude_Transmissor",
    "Longitude_Transmissor",
    "CNPJ",
    "Validade_RF",
)
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
)

SRD = (
"Frequência",
"Entidade",
"Fistel",
"Número_Estação",
"Município",
"UF",
"Latitude",
"Longitude",
"CNPJ",
"Num_Serviço",
"Classe",
)

TELECOM = SRD + (
    "Classe_Emissão",
    "Largura_Emissão",
    "Validade_RF",
)

RADIODIFUSAO = SRD + (
    "Validade_RF",
    "Status",
    # "Num_Ato",
    # "Data_Ato",
)

APP_ANALISE = (
    "Frequency",
    "Latitude",
    "Longitude",
    "Description",
    "Service",
    "Station",
    "Class",
    "BW",
)

ESTADOS = (
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
)

# Cell
ENTIDADES = {}

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

BW = {'H': 0.001, 'K': 1, 'M': 1000, 'G': 1000000}
BW_MAP = {'167': '6M00', '205': '10K0', '230': '256K', '231': '256K', '247': '5M70', '248': '6M00', '800': '6M00', '801': '5M70', '805': '256K'}

# Cell
RADCOM = """SELECT F.MedFrequenciaInicial as 'Frequência',
SRD.IndFase as 'Fase',
ID.SiglaSituacao as 'Situação',
Ent.NomeEntidade as 'Entidade',
H.NumFistel as 'Fistel',
E.NumEstacao as 'Número_da_Estação',
M.NomeMunicipio as 'Município',
PB.SiglaUF as 'UF',
SRD.MedLatitudeDecimal as 'Latitude',
SRD.MedLongitudeDecimal as 'Longitude',
Ent.NumCnpjCpf as 'CNPJ'

  FROM SRD_PEDIDORADCOM SRD

  inner join ESTACAO E on E.IdtHabilitacao =  SRD.IdtHabilitacao
  inner join FREQUENCIA F on F.IdtEstacao = E.IdtEstacao
  inner join HABILITACAO H on H.IdtEntidade = SRD.IdtEntidade
  inner join ENTIDADE Ent on Ent.IdtEntidade = SRD.IdtEntidade
  inner join SRD_PLANOBASICO PB on PB.IdtPlanoBasico = SRD.IdtPlanoBasico
  inner join Municipio M on M.CodMunicipio = PB.CodMunicipio
  left join SRD_INDICESESTACAO ID on ID.IdtHabilitacao = SRD.IdtHabilitacao
  where SRD.IdtPlanoBasico is not Null and SRD.IndFase is not Null

  order by Frequência, UF, Município"""

# Cell
STEL = """select distinct f.MedTransmissaoInicial as 'Frequência',
uf.SiglaUnidadeFrequencia as 'Unidade',
d.CodClasseEmissao as 'Classe_Emissão',
d.SiglaLarguraEmissao as 'Largura_Emissão',
ce.CodTipoClasseEstacao as 'Classe',
e.NumServico as 'Num_Serviço',
ent.NomeEntidade as 'Entidade',
h.NumFistel as 'Fistel',
e.NumEstacao as 'Número_da_Estação',
mu.NomeMunicipio as 'Município',
e.SiglaUf as 'UF',
e.MedLatitudeDecimal as 'Latitude',
e.MedLongitudeDecimal as 'Longitude',
ent.NumCnpjCpf as 'CNPJ',
c.DataValidadeRadiofrequencia as 'Validade_RF'
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
where h.NumServico <> '010'
and e.DataExclusao is null
and e.IndStatusEstacao = 'L'
and f.MedTransmissaoInicial is not null
and f.CodStatusRegistro = 'L'
and c.DataValidadeRadiofrequencia is not null
order by Frequência, UF, Município"""

# Cell
BW_pattern = re.compile("^(\d{1,3})([HKMG])(\d{0,2})$")
REGEX_ESTADOS = f'({"|".join(ESTADOS)})'