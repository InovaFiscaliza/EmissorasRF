# AUTOGENERATED! DO NOT EDIT! File to edit: ..\nbs\constants.ipynb.

# %% auto 0
__all__ = ['TIMEOUT', 'RELATORIO', 'ESTACAO', 'COLUNAS', 'APP_ANALISE', 'ESTADOS', 'SIGLAS', 'BW', 'BW_MAP', 'COLS_TELECOM',
           'COLS_SRD', 'SQL_RADCOM', 'SQL_STEL', 'SQL_VALIDA_COORD', 'MONGO_TELECOM', 'MONGO_SRD', 'BW_pattern',
           'REGEX_ESTADOS']

# %% ..\nbs\constants.ipynb 2
import re

# %% ..\nbs\constants.ipynb 4
TIMEOUT = 5
RELATORIO = "http://sistemas.anatel.gov.br/se/eApp/reports/b/srd/resumo_sistema.php?id={id}&state={state}"
ESTACAO = "http://sistemas.anatel.gov.br/se/public/view/b/srd.php?wfid=estacoes&id={}"

# %% ..\nbs\constants.ipynb 6
COLUNAS = (
    "Frequência",
    "Entidade",
    "Fistel",
    "Número_Estação",
    "Município",
    "Código_Município",
    "UF",
    "Latitude",
    "Longitude",
    "Classe",
    "Num_Serviço",
    "Classe_Emissão",
    "Largura_Emissão(kHz)",
    "Validade_RF",
    "Status",
    "Fonte",
    "Multiplicidade",
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

# %% ..\nbs\constants.ipynb 8
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

BW = {"H": 0.001, "K": 1, "M": 1000, "G": 1000000}
BW_MAP = {
    "167": "6M00",
    "205": "10K0",
    "230": "256K",
    "231": "256K",
    "247": "5M70",
    "248": "6M00",
    "800": "6M00",
    "801": "5M70",
    "805": "256K",
    "":"",
}

COLS_TELECOM = {
    "NumFistel": "Fistel",
    "NumServico": "Num_Serviço",
    "NomeEntidade": "Entidade",
    "SiglaUf": "UF",
    "NumEstacao": "Número_Estação",
    "CodTipoClasseEstacao": "Classe",
    "NomeMunicipio": "Município",
    "CodMunicipio": "Código_Município",
    "DataValidade": "Validade_RF",
    "FreqTxMHz": "Frequência",
    "Latitude": "Latitude",
    "Longitude": "Longitude",
    "DesignacaoEmissao": "Designacao_Emissão",
}

COLS_SRD = {
    "frequency": "Frequência",
    "licensee": "Entidade",
    "NumFistel": "Fistel",
    "estacao.NumEstacao": "Número_Estação",
    "srd_planobasico.NomeMunicipio": "Município",
    "srd_planobasico.CodMunicipio": "Código_Município",
    "srd_planobasico.SiglaUF": "UF",
    "estacao.MedLatitudeDecimal": "Latitude",
    "estacao.MedLongitudeDecimal": "Longitude",
    "stnClass": "Classe",
    "NumServico": "Num_Serviço",
    "habilitacao.DataValFreq": "Validade_RF",
    "Status.state": "Status",
}

# %% ..\nbs\constants.ipynb 10
SQL_RADCOM = """
select 
  distinct F.MedFrequenciaInicial as 'Frequência', 
  SRD.IndFase as 'Fase', 
  ID.SiglaSituacao as 'Situação', 
  Ent.NomeEntidade as 'Entidade', 
  H.NumFistel as 'Fistel', 
  E.NumEstacao as 'Número_Estação', 
  M.NomeMunicipio as 'Município', 
  M.CodMunicipio as Código_Município,
  PB.SiglaUF as 'UF', 
  SRD.MedLatitudeDecimal as 'Latitude', 
  SRD.MedLongitudeDecimal as 'Longitude' 
from 
  SRD_PEDIDORADCOM SRD 
  left join ESTACAO E on E.IdtHabilitacao = SRD.IdtHabilitacao 
  inner join FREQUENCIA F on F.IdtEstacao = E.IdtEstacao 
  left join HABILITACAO H on H.IdtEntidade = SRD.IdtEntidade 
  left join ENTIDADE Ent on Ent.IdtEntidade = SRD.IdtEntidade 
  left join SRD_PLANOBASICO PB on PB.IdtPlanoBasico = SRD.IdtPlanoBasico 
  left join Municipio M on M.CodMunicipio = PB.CodMunicipio 
  left join SRD_INDICESESTACAO ID on ID.IdtHabilitacao = SRD.IdtHabilitacao 
  left join CONTRATO C on C.IdtContrato = E.IdtContrato 
where 
  SRD.IdtPlanoBasico is not Null 
  and SRD.IndFase is not Null 
order by 
  Frequência, 
  UF, 
  Município

"""

# %% ..\nbs\constants.ipynb 11
SQL_STEL = """
select 
  distinct f.MedTransmissaoInicial as 'Frequência', 
  uf.SiglaUnidadeFrequencia as 'Unidade', 
  d.CodClasseEmissao as 'Classe_Emissão', 
  d.SiglaLarguraEmissao as 'Largura_Emissão', 
  ce.CodTipoClasseEstacao as 'Classe', 
  e.NumServico as 'Num_Serviço', 
  ent.NomeEntidade as 'Entidade', 
  h.NumFistel as 'Fistel', 
  e.NumEstacao as 'Número_Estação', 
  mu.NomeMunicipio as 'Município',
  mu.CodMunicipio as Código_Município,
  e.SiglaUf as 'UF', 
  e.MedLatitudeDecimal as 'Latitude', 
  e.MedLongitudeDecimal as 'Longitude', 
  c.DataValidadeRadiofrequencia as 'Validade_RF' 
from 
  estacao e 
  left join contrato c on e.IdtContrato = c.Idtcontrato 
  left join frequencia f on f.IdtEstacao = e.IdtEstacao 
  left join CLASSEESTACAO ce on ce.IdtFrequencia = f.IdtFrequencia 
  left join DESIGNACAOEMISSAO d on d.IdtClasseEstacao = ce.IdtClasseEstacao 
  left join HABILITACAO h on h.IdtHabilitacao = c.IdtHabilitacao 
  left join entidade ent on ent.IdtEntidade = h.IdtEntidade 
  left join endereco en on en.IdtEstacao = e.IdtEstacao 
  left join Municipio mu on mu.CodMunicipio = en.CodMunicipio 
  left join Servico s on s.NumServico = h.NumServico 
  and s.IdtServicoAreaAtendimento = 4 
  left join UnidadeFrequencia uf on uf.IdtUnidadeFrequencia = f.IdtUnidadeTransmissao 
where 
  h.NumServico <> '010' 
  and e.DataExclusao is null 
  and e.IndStatusEstacao = 'L' 
  and e.MedLatitudeDecimal is not null 
  and e.MedLongitudeDecimal is not null 
  and f.MedTransmissaoInicial is not null 
  and f.CodStatusRegistro = 'L' 
  and c.DataValidadeRadiofrequencia is not null 
"""

# %% ..\nbs\constants.ipynb 12
SQL_VALIDA_COORD = """
    SELECT 
        mun.NO_MUNICIPIO 
        , mun.NU_LONGITUDE 
        , mun.NU_LATITUDE         
        , CONVERT(int, 
            (mun.GE_POLIGONO.STIntersects(geometry::STGeomFromText(
                'POINT({} {})', 
                mun.GE_POLIGONO.STSrid)
            )) 
        )AS COORD_VALIDA
    from 
        CORPORATIVO.dbo.TB_IBGE_MUNICIPIO mun
    WHERE
        MUN.CO_MUNICIPIO = {}
"""

# %% ..\nbs\constants.ipynb 13
MONGO_TELECOM = {
    "$and": [
        {"DataExclusao": None},
        {"DataValidade": {"$nin": ["", None]}},
        {"Status.state": "LIC-LIC-01"},
        {"NumServico": {"$nin": ["010", "045", "171", "450", "750", "", None]}},
        {"FreqTxMHz": {"$nin": [None, "", 0]}},
        {"CodMunicipio": {"$nin": [None, ""]}},
        {"Latitude": {"$nin": [None, ""]}},
        {"Longitude": {"$nin": [None, ""]}},
        {"FreqTxMHz": {"$type": 1.0}},
        {"Latitude": {"$type": 1.0}},
        {"Longitude": {"$type": 1.0}},
    ]
}


MONGO_SRD = {
    "$and": [
        {
            "frequency": {"$nin": [None, "", 0], "$type": 1.0},
            "srd_planobasico.CodMunicipio": {"$nin": [None, ""]},
            "NumFistel": {"$nin": [None, ""]},
        }
    ]
}

# %% ..\nbs\constants.ipynb 15
BW_pattern = re.compile("^(\d{1,3})([HKMG])(\d{0,2})(\w{0,3}$)")
REGEX_ESTADOS = f'({"|".join(ESTADOS)})'
