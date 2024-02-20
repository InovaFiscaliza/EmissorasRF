# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_constants.ipynb.

# %% auto 0
__all__ = [
	'TIMEOUT',
	'RELATORIO_SRD',
	'ESTACAO',
	'MALHA_IBGE',
	'FILES',
	'PATH_NAV',
	'PATH_COM',
	'VOR_ILS_DME',
	'CHANNELS',
	'IBGE_MUNICIPIOS',
	'IBGE_POLIGONO',
	'COLUNAS',
	'COLS_SRD',
	'FLOAT_COLUMNS',
	'INT_COLUMNS',
	'STR_COLUMNS',
	'CAT_COLUMNS',
	'AGG_LICENCIAMENTO',
	'AGG_SMP',
	'APP_ANALISE_PT',
	'APP_ANALISE_EN',
	'ESTADOS',
	'SIGLAS',
	'BW',
	'BW_MAP',
	'DICT_SRD',
	'PROJECTION_SRD',
	'DICT_LICENCIAMENTO',
	'PROJECTION_LICENCIAMENTO',
	'MONGO_TELECOM',
	'MONGO_SRD',
	'MONGO_SMP',
	'SQL_RADCOM',
	'SQL_STEL',
	'SQL_VALIDA_COORD',
	'REGEX_ESTADOS',
	'RE_BW',
	'MIN_LAT',
	'MAX_LAT',
	'MIN_LONG',
	'MAX_LONG',
]

# %% ../nbs/00_constants.ipynb 2
import re
from pathlib import Path

# %% ../nbs/00_constants.ipynb 4
TIMEOUT = 5
RELATORIO_SRD = (
	'http://sistemas.anatel.gov.br/se/eApp/reports/b/srd/resumo_sistema.php?id={}&state={}'
)
ESTACAO = 'http://sistemas.anatel.gov.br/se/public/view/b/srd.php?wfid=estacoes&id={}'
MALHA_IBGE = 'https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/Brasil/BR/BR_Municipios_2022.zip'
FILES = Path(__file__).parent / 'datasources' / 'arquivos'
PATH_NAV = FILES / 'VHF_NAV.csv'
PATH_COM = FILES / 'VHF_COM.csv'
VOR_ILS_DME = FILES / 'VOR_ILS_DME_Channel.csv'
CHANNELS = FILES / 'canalizacao_smp.csv'
IBGE_MUNICIPIOS = FILES / 'municipios.csv'
IBGE_POLIGONO = FILES / 'BR_Municipios_2022' / 'BR_Municipios_2022.shp'

# %% ../nbs/00_constants.ipynb 6
COLUNAS = [
	'Frequência',
	'Entidade',
	'Fistel',
	'Serviço',
	'Estação',
	'Latitude',
	'Longitude',
	'Código_Município',
	'Município',
	'UF',
	'Classe',
	'Classe_Emissão',
	'Largura_Emissão(kHz)',
	'Validade_RF',
	'Status',
	'Fonte',
	'Multiplicidade',
	'Log',
]

COLS_SRD = COLUNAS + [
	'Cota_Base_Torre(m)',
	'Potência_Transmissor(W)',
	'Ganho_Antena(dBd)',
	'Ângulo_Elevação_Antena',
	'Azimute_Antena',
	'Altura_Antena(m)',
	'Atenuação_Linha(db/100m)',
	'Perdas_Acessórias_Linha(db)',
	'Padrão_Antena(dBd)',
	'Comprimento_Linha(m)',
	'Relatório_Canal',
]

FLOAT_COLUMNS = [
	'Latitude',
	'Longitude',
	'Largura_Emissão(kHz)',
	'Cota_Base_Torre(m)',
	'Potência_Transmissor(W)',
	'Ganho_Antena(dBd)',
	'Ângulo_Elevação_Antena',
	'Azimute_Antena',
	'Altura_Antena(m)',
	'Atenuação_Linha(db/100m)',
	'Perdas_Acessórias_Linha(db)',
	'Comprimento_Linha(m)',
]

INT_COLUMNS = ['Fistel', 'Serviço', 'Multiplicidade']


STR_COLUMNS = ['Entidade', 'Estação', 'Log', 'Padrão_Antena(dBd)', 'Relatório_Canal']

CAT_COLUMNS = [
	'Código_Município',
	'Município',
	'UF',
	'Classe',
	'Classe_Emissão',
	'Validade_RF',
	'Status',
	'Fonte',
]

# DTYPES = {
# 	'Frequência'
# 	'Entidade'
# 	'Fistel'
# 	'Serviço'
# 	'Estação'
# 	'Latitude'
# 	'Longitude'
# 	'Código_Município'
# 	'Município'
# 	'UF'
# 	'Classe'
# 	'Classe_Emissão'
# 	'Largura_Emissão(kHz)'
# 	'Validade_RF'
# 	'Status'
# 	'Fonte'
# 	'Multiplicidade'
# 	'Log'
# 	'Cota_Base_Torre(m)'
# 	'Potência_Transmissor(W)'
# 	'Ganho_Antena(dBd)'
# 	'Ângulo_Elevação_Antena'
# 	'Azimute_Antena'
# 	'Altura_Antena(m)'
# 	'Atenuação_Linha(db/100m)'
# 	'Perdas_Acessórias_Linha(db)'
# 	'Padrão_Antena(dBd)'
# 	'Comprimento_Linha(m)'
# 	'Relatório_Canal'
# }

# COLS_LICENCIAMENTO = [
# 	'Frequência',
# 	'Entidade',
# 	'Fistel',
# 	'Estação',
# 	'Município',
# 	'Código_Município',
# 	'UF',
# 	'Latitude',
# 	'Longitude',
# 	'Classe',
# 	'Serviço',
# 	'Classe_Emissão',
# 	'Largura_Emissão(kHz)',
# 	'Validade_RF',
# 	'Status',
# 	'Fonte',
# 	'Multiplicidade',
# 	'Potência_Transmissor(W)',
# 	'Cod_Tipo_Antena',
# 	'Polarização_Antena',
# 	# "Raio_Antena",
# 	'Ganho_Antena',
# 	'FC_Antena',
# 	'Ang_MP_Antena',
# 	'Ângulo_Elevação_Antena',
# 	'Azimute_Antena',
# 	'Altura_Antena',
# 	'Perdas_Acessorias',
# 	'Log',
# ]

AGG_LICENCIAMENTO = [
	'Frequência',
	'Fistel',
	'Código_Município',
	'Longitude',
	'Latitude',
	'Classe',
	'Serviço',
	'Classe_Emissão',
	'Largura_Emissão(kHz)',
]

AGG_SMP = [
	'Código_Município',
	'Fistel',
	'Frequência',
	'Largura_Emissão(kHz)',
	'Classe_Emissão',
	'Tecnologia',
]

APP_ANALISE_PT = (
	'Frequência',
	'Latitude',
	'Longitude',
	'Descrição',
	'Serviço',
	'Estação',
	'Classe_Emissão',
	'Largura_Emissão(kHz)',
)

APP_ANALISE_EN = (
	'Frequency',
	'Latitude',
	'Longitude',
	'Description',
	'Service',
	'Station',
	'Class',
	'BW',
)

ESTADOS = (
	'AC',
	'AL',
	'AP',
	'AM',
	'BA',
	'CE',
	'ES',
	'GO',
	'MA',
	'MT',
	'MS',
	'MG',
	'PA',
	'PB',
	'PR',
	'PE',
	'PI',
	'RJ',
	'RN',
	'RS',
	'RO',
	'RR',
	'SC',
	'SP',
	'SE',
	'TO',
	'DF',
)

# %% ../nbs/00_constants.ipynb 8
SIGLAS = {
	'Acre': 'AC',
	'Alagoas': 'AL',
	'Amapá': 'AP',
	'Amazonas': 'AM',
	'Bahia': 'BA',
	'Ceará': 'CE',
	'Espírito Santo': 'ES',
	'Goiás': 'GO',
	'Maranhão': 'MA',
	'Mato Grosso': 'MT',
	'Mato Grosso do Sul': 'MS',
	'Minas Gerais': 'MG',
	'Pará': 'PA',
	'Paraíba': 'PB',
	'Paraná': 'PR',
	'Pernambuco': 'PE',
	'Piauí': 'PI',
	'Rio de Janeiro': 'RJ',
	'Rio Grande do Norte': 'RN',
	'Rio Grande do Sul': 'RS',
	'Rondônia': 'RO',
	'Roraima': 'RR',
	'Santa Catarina': 'SC',
	'São Paulo': 'SP',
	'Sergipe': 'SE',
	'Tocantins': 'TO',
	'Distrito Federal': 'DF',
}

BW = {'H': 0.001, 'K': 1, 'M': 1000, 'G': 1000000}

BW_MAP = {
	'167': '6M00',
	'205': '10K0',
	'230': '256K',
	'231': '256K',
	'247': '5M70',
	'248': '6M00',
	'800': '6M00',
	'801': '5M70',
	'805': '256K',
	'': '',
}

DICT_SRD = {
	'_id': 'Id',
	'frequency': 'Frequência',
	'licensee': 'Entidade',
	'NumFistel': 'Fistel',
	'NumEstacao': 'Estação',
	'NomeMunicipio': 'Município',
	'CodMunicipio': 'Código_Município',
	'SiglaUF': 'UF',
	'MedLatitudeDecimal': 'Latitude',
	'MedLongitudeDecimal': 'Longitude',
	'stnClass': 'Classe',
	'NumServico': 'Serviço',
	'DataValFreq': 'Validade_RF',
	'state': 'Status',
	'MedCotaBaseTorre': 'Cota_Base_Torre(m)',
	'hpat': 'Padrão_Antena(dBd)',
	'MedPotenciaOperacao': 'Potência_Transmissor(W)',
	'IndPolariz': 'Polarização_Antena',
	'MedGMaxdBd': 'Ganho_Antena(dBd)',
	'MedBeamTilt': 'Ângulo_Elevação_Antena',
	'MedOrientNV': 'Azimute_Antena',
	'MedHCI': 'Altura_Antena(m)',
	'MedAtenLinhaTransmissaodB100m': 'Atenuação_Linha(db/100m)',
	'MedComprimento': 'Comprimento_Linha(m)',
	'PerdasAcessorias_db': 'Perdas_Acessórias_Linha(db)',
}

PROJECTION_SRD = {
	'_id': 1.0,
	'frequency': 1.0,
	'licensee': 1.0,
	'NumFistel': 1.0,
	'NumEstacao': '$estacao.NumEstacao',
	# flatten the nested fields with dot notation
	'NomeMunicipio': '$srd_planobasico.NomeMunicipio',
	'CodMunicipio': '$srd_planobasico.CodMunicipio',
	'SiglaUF': '$srd_planobasico.SiglaUF',
	'MedLatitudeDecimal': '$estacao.MedLatitudeDecimal',
	'MedLongitudeDecimal': '$estacao.MedLongitudeDecimal',
	'stnClass': 1.0,
	'NumServico': 1.0,
	'DataValFreq': '$habilitacao.DataValFreq',
	'state': '$Status.state',
	'MedCotaBaseTorre': '$estacao.MedCotaBaseTorre',
	'hpat': 1,
	'MedPotenciaOperacao': '$equipamento.transmissor.MedPotenciaOperacao',
	'MedGMaxdBd': '$antena.principal.MedGMaxdBd',
	'MedBeamTilt': '$antena.principal.MedBeamTilt',
	'MedOrientNV': '$antena.principal.MedOrientNV',
	'IndPolariz': '$antena.principal.IndPolariz',
	'MedHCI': '$antena.principal.MedHCI',
	'MedAtenLinhaTransmissaodB100m': '$linhatransmissao.principal.MedAtenLinhaTransmissaodB100m',
	'MedComprimento': '$linhatransmissao.principal.MedComprimento',
	'PerdasAcessorias_db': '$linhatransmissao.principal.PerdasAcessorias_db',
}

DICT_LICENCIAMENTO = {
	'NumAto': 'Num_Ato',
	'NumFistel': 'Fistel',
	'NumServico': 'Serviço',
	'NomeEntidade': 'Entidade',
	'SiglaUf': 'UF',
	'NumEstacao': 'Estação',
	'CodTipoClasseEstacao': 'Classe',
	'NomeMunicipio': 'Município',
	'CodMunicipio': 'Código_Município',
	'DataValidade': 'Validade_RF',
	'FreqTxMHz': 'Frequência',
	'formId': 'Tipo_Estação',
	'Tecnologia': 'Tecnologia',
	'Latitude': 'Latitude',
	'Longitude': 'Longitude',
	'DesignacaoEmissao': 'Designação_Emissão',
	# 'PotenciaTransmissorWatts': 'Potência_Transmissor(W)',
	# 'CodTipoAntena': 'Cod_Tipo_Antena',
	# 'Polarizacao': 'Polarização_Antena',
	# 'GanhoAntena': 'Ganho_Antena',
	# 'FrenteCostaAntena': 'FC_Antena',
	# 'AnguloMeiaPotenciaAntena': 'Ang_MP_Antena',
	# 'AnguloElevacao': 'Ângulo_Elevação_Antena',
	# 'Azimute_Antena': 'Azimute_Antena',
	# 'AlturaAntena': 'Altura_Antena',
	# 'PerdasAcessorias': 'Perdas_Acessorias',
}

PROJECTION_LICENCIAMENTO = {k: 1.0 for k in DICT_LICENCIAMENTO}

# %% ../nbs/00_constants.ipynb 9
MONGO_TELECOM = {
	'$and': [
		{'DataExclusao': None},
		{'DataValidade': {'$nin': ['', None]}},
		{'Status.state': 'LIC-LIC-01'},
		{'NumServico': {'$nin': ['010', '045', '171', '450', '750', '', None]}},
		{'FreqTxMHz': {'$nin': [None, '', 0], '$type': 1.0}},
		{'CodMunicipio': {'$nin': [None, '']}},
		{'NumFistel': {'$nin': [None, '']}},
		{'CodTipoClasseEstacao': {'$nin': [None, '']}},
		{'DesignacaoEmissao': {'$nin': [None, '']}},
	]
}


MONGO_SRD = {
	'$and': [
		{'frequency': {'$nin': [None, '', 0], '$type': 1.0}},
		{'srd_planobasico.CodMunicipio': {'$nin': [None, '']}},
		{'NumFistel': {'$nin': [None, '']}},
		# {'habilitacao.DataValFreq': {'$nin': [None, '']}},
	]
}

MONGO_SMP = {
	'$and': [
		{'DataExclusao': None},
		{'DataValidade': {'$nin': ['', None]}},
		{'Status.state': 'LIC-LIC-01'},
		{'NumServico': '010'},
		{'FreqTxMHz': {'$nin': [None, '', 0], '$type': 1.0}},
		{'CodMunicipio': {'$nin': [None, '']}},
		{'NumFistel': {'$nin': [None, '']}},
		{'CodTipoClasseEstacao': {'$nin': [None, '']}},
		{'DesignacaoEmissao': {'$nin': [None, '']}},
		{'Tecnologia': {'$nin': [None, '']}},
	]
}

# %% ../nbs/00_constants.ipynb 11
SQL_RADCOM = """
select 
  distinct F.MedFrequenciaInicial as 'Frequência', 
  SRD.IndFase as 'Fase', 
  ID.SiglaSituacao as 'Situação', 
  Ent.NomeEntidade as 'Entidade', 
  H.NumFistel as 'Fistel', 
  E.NumEstacao as 'Estação', 
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

# %% ../nbs/00_constants.ipynb 12
SQL_STEL = """
select 
  distinct f.MedTransmissaoInicial as 'Frequência', 
  uf.SiglaUnidadeFrequencia as 'Unidade', 
  d.CodClasseEmissao as 'Classe_Emissão', 
  d.SiglaLarguraEmissao as 'Largura_Emissão', 
  ce.CodTipoClasseEstacao as 'Classe', 
  e.NumServico as 'Serviço', 
  ent.NomeEntidade as 'Entidade', 
  h.NumFistel as 'Fistel', 
  e.NumEstacao as 'Estação', 
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
  and mu.CodMunicipio is not null
  and f.MedTransmissaoInicial is not null 
  and f.CodStatusRegistro = 'L' 
  and c.DataValidadeRadiofrequencia is not null 
"""

# %% ../nbs/00_constants.ipynb 13
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

# %% ../nbs/00_constants.ipynb 14
REGEX_ESTADOS = f'({"|".join(ESTADOS)})'
RE_BW = re.compile(r'^(\d{1,3})([HKMG])(\d{0,2})(\w{0,3})')

# %% ../nbs/00_constants.ipynb 16
MIN_LAT = -33.7509907  # Arroio Chuy RS
MAX_LAT = 5.2718317  # Monte Caburaí RR
MIN_LONG = -73.80658592032779
MAX_LONG = -32.377816
