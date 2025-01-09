select distinct
    f.MedTransmissaoInicial as 'Frequência',
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
    left JOIN UnidadeFrequencia uf on uf.IdtUnidadeFrequencia = f.IdtUnidadeTransmissao
where
    h.NumServico = '185'
    --  and e.DataExclusao is null 
    --  and e.IndStatusEstacao = 'L' 
    --  and mu.CodMunicipio is not null
    --  and f.MedTransmissaoInicial is not null 
    --  and f.CodStatusRegistro = 'L' 
    --  and c.DataValidadeRadiofrequencia is not null