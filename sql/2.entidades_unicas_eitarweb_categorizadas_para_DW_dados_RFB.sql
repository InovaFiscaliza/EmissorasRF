SELECT 
  DISTINCT SRF.NumCNPJCPF AS 'CPF/CNPJ', 
  CASE WHEN SRF.CodNaturezaJuridica IS NOT NULL THEN 'Pessoa Jurídica' ELSE 'Pessoa Física' END AS 'Tipo RFB', 
  SRF.NomeEntidade AS 'Nome da Entidade RFB', 
  CASE WHEN SRF.CodNaturezaJuridica IS NOT NULL THEN Situ.DescSituacaoCadastralCNPJ ELSE situ.DescSituacaoCadastralCPF END AS 'Situação Cadastral RFB', 
  CASE WHEN SRF.CodNaturezaJuridica IS NOT NULL THEN SRF.DataSituacaoCadastral ELSE PF.DataAtualizacaoReceita END AS 'Data Alteração Situação Cadastral RFB', 
  CASE WHEN CNPJ.IndMatriz = 1 THEN 'Sim' ELSE NULL END AS 'Sede RFB', 
  CASE WHEN SRF.CodNaturezaJuridica IS NULL 
  AND PF.IndSexo = 1 THEN ' Masculino' WHEN SRF.CodNaturezaJuridica IS NULL 
  AND PF.IndSexo = 2 THEN ' Feminino' ELSE NULL END AS 'Sexo RFB', 
  LOWER(CNPJ.Email) AS 'E-Mail RFB', 
  SRF.EndLogradouro AS 'Logradouro RFB', 
  SRF.EndNumero AS 'Número RFB', 
  SRF.EndComplemento AS 'Complemento RFB', 
  SRF.EndBairro AS 'Bairro RFB', 
  SRF.EndCEP AS 'CEP RFB', 
  Cidade.NO_MUNICIPIO AS 'Município RFB', 
  SRF.SiglaUF AS 'UF RFB', 
  CASE WHEN SRF.CodPais = '   ' THEN 'Brasil' ELSE CNPJ.NomePaisCidadeExterior END AS 'País RFB', 
  CASE WHEN SRF.CodNaturezaJuridica IS NOT NULL THEN CNPJ.NumCpfResponsavel ELSE NULL END AS 'CPF do Responsável Legal RFB', 
  CASE WHEN SRF.CodNaturezaJuridica IS NOT NULL THEN CNPJ.NomeResponsavel ELSE NULL END AS 'Nome do Responsável Legal RFB', 
  SRF.DataCarga AS 'Data Registro Anatel RFB' --TIPO SERVICO
  , 
  CASE WHEN tipo_entidade.out_telecom IS NOT NULL THEN 'Outorgada Telecomunicações' WHEN tipo_entidade.out_telecom IS NULL 
  AND tipo_entidade.out_radiodifusao IS NOT NULL THEN 'Outorgada Radiodifusão' WHEN tipo_entidade.out_telecom IS NULL 
  AND EnCer.IC_SITUACAO IS NOT NULL THEN 'Certificação' WHEN tipo_entidade.out_telecom_temp IS NOT NULL THEN 'Outorgada Telecomunicações Temporário' WHEN tipo_entidade.out_prestador_disp_out IS NOT NULL THEN 'Prestador de Telecomunicações Dispensado de Outorga' WHEN Hab.IdtEntidade IS NULL 
  AND Ent.NumCnpjCpf NOT IN (
    SELECT 
      DISTINCT NU_CPF_CNPJ COLLATE Latin1_General_CI_AI AS NumCPFCNPJ 
    FROM 
      [DB_TELECOM].SC_CORPORATIVO.TB_ENTIDADE_NACIONAL
  ) THEN 'Não Outorgada' ELSE 'Não definido' END AS 'Tipo Entidade' --ATIVA/INATIVA
  , 
  CASE WHEN EnCer.IC_SITUACAO <> 1 
  AND EnCer.IC_SITUACAO IS NOT NULL THEN 'Cert Inativa' WHEN EnCer.IC_SITUACAO = 1 THEN 'Cert Ativa' WHEN EXISTS (
    SELECT 
      ent.NumCnpjCpf, 
      COUNT(hab.DataExclusao) AS Exclusao, 
      -- Alterado ORLE
      COUNT(hab.DataInclusao) AS Inclusao -- Alterado ORLE
    FROM 
      SITARWEB.DBO.entidade AS ent 
      LEFT JOIN SITARWEB.DBO.habilitacao AS hab ON ent.idtentidade = hab.idtentidade --RIGHT JOIN SITARWEB.DBO.contrato AS Cont ON Cont.idthabilitacao = Hab.idthabilitacao -- Excluído ORLE
    WHERE 
      ent.NumCnpjCpf COLLATE Latin1_General_CI_AI = SRF.NumCNPJCPF 
    GROUP BY 
      ent.NumCnpjCpf 
    HAVING 
      COUNT(hab.DataExclusao) = COUNT(hab.DataInclusao)
  ) THEN 'Inativa' WHEN EXISTS (
    SELECT 
      ent.NumCnpjCpf 
    FROM 
      SITARWEB.DBO.entidade AS ent 
      LEFT JOIN SITARWEB.DBO.habilitacao AS hab ON ent.idtentidade = hab.idtentidade --RIGHT JOIN SITARWEB.DBO.contrato AS Cont ON Cont.idthabilitacao = Hab.idthabilitacao -- Excluído ORLE
    WHERE 
      ent.NumCnpjCpf COLLATE Latin1_General_CI_AI = SRF.NumCNPJCPF
  ) THEN 'Ativa' WHEN Hab.IdtEntidade IS NULL 
  AND Ent.NumCnpjCpf NOT IN (
    SELECT 
      DISTINCT NU_CPF_CNPJ COLLATE Latin1_General_CI_AI AS NumCPFCNPJ 
    FROM 
      [DB_TELECOM].SC_CORPORATIVO.TB_ENTIDADE_NACIONAL
  ) THEN 'Não Outorgada' ELSE 'Não Definido' END AS 'Situação Entidade na Anatel', 
  LOWER(Ent.EndEletronico) AS 'E-mail SitarWeb' 
FROM 
  CORPORATIVO.dbo.CadastroSRF AS SRF 
  LEFT JOIN CORPORATIVO.dbo.CadastroSRFComplementoPJ AS CNPJ ON SRF.NumCNPJCPF = CNPJ.NumCNPJ 
  LEFT JOIN CORPORATIVO.dbo.CadastroSRFComplementoPF AS PF ON SRF.NumCNPJCPF = PF.NumCPF 
  LEFT JOIN CORPORATIVO.dbo.CadastroSRFMunicipioTom AS Munic ON SRF.CodMunicipio = Munic.CodIBGE 
  LEFT JOIN CORPORATIVO.dbo.TB_IBGE_MUNICIPIO AS Cidade ON SRF.CodMunicipio = Cidade.CO_MUNICIPIO 
  INNER JOIN SITARWEB.DBO.ENTIDADE AS Ent ON SRF.NumCNPJCPF = Ent.NumCnpjCpf COLLATE Latin1_General_CI_AI 
  LEFT JOIN SITARWEB.DBO.HABILITACAO AS Hab ON Ent.IdtEntidade = Hab.idtEntidade 
  LEFT JOIN SITARWEB.DBO.contrato AS Cont ON Cont.idthabilitacao = Hab.idthabilitacao 
  LEFT JOIN CORPORATIVO.dbo.CadastroSRFSituacaoCadastral AS Situ ON SRF.CodSituacaoCadastral = Situ.CodSituacaoCadastral 
  LEFT JOIN DB_TELECOM.SC_CORPORATIVO.TB_ENTIDADE_NACIONAL AS EnNas ON Ent.NumCnpjCpf = EnNas.NU_CPF_CNPJ 
  LEFT JOIN DB_TELECOM.SC_CORPORATIVO.TB_ENTIDADE AS EnCer ON EnNas.CO_ENTIDADE = EnCer.CO_SEQ_ENTIDADE 
  LEFT JOIN (
    SELECT 
      DISTINCT IdtEntidade, 
      MAX(
        CASE WHEN numserviço IN (
          '729', '116', '175', '176', '172', '173', 
          '174', '171', '034', '030', '040', 
          '010', '189', '020', '108', '049', 
          '050', '060', '023', '094', '038', 
          '039', '051', '076', '187', '077', 
          '041', '042', '078', '079', '036', 
          '002', '001', '047', '045', '163', 
          '191', '188', '069', '750', '067', 
          '031', '350', '054', '053', '032', 
          '016', '012', '027', '022', '029', 
          '025', '024', '013', '014', '033', 
          '026', '046', '015', '159', '302', 
          '048', '400', '064', '604', '018', 
          '507', '181', '028', '011', '019', 
          '182', '017', '140', '021', '186', 
          '185', '167', '124', '125', '043', 
          '132', '701', '086', '183', '264', 
          '740', '044', '735', '820', '251', 
          '252', '253', '256', '255', '254'
        ) THEN 1 END
      ) AS out_telecom, 
      MAX(
        CASE WHEN numserviço IN (
          '810', '728', '730', '710', '803', '247', 
          '802', '231', '248', '230', '205', 
          '221', '213', '800', '801', '229', 
          '804', '228'
        ) THEN 1 END
      ) AS out_radiodifusao, 
      MAX(
        CASE WHEN numserviço IN ('035', '037') THEN 1 END
      ) AS out_telecom_temp, 
      MAX(
        CASE WHEN numserviço IN ('099', '401', '190', '450') THEN 1 END
      ) AS out_prestador_disp_out 
    FROM 
      SITARWEB.DBO.HABILITACAO a 
    WHERE 
      a.DataExclusao is null -- Incluído ORLE
    GROUP BY 
      IdtEntidade
  ) AS tipo_entidade ON Ent.IdtEntidade = tipo_entidade.idtEntidade 
WHERE 
  
  /* SUBQUERIES */
  ent.NumCnpjCpf NOT IN (
    '00000000000', '00000000000000', 
    '12312312387', '50003731030', '50010027459'
  ) -- Meros registros de teste
  AND SRF.NumCNPJCPF IN (
    -- QUERY Entidades Certificadoras/Fabricantes/Solicitantes/Laboratórios
    SELECT 
      DISTINCT EnNas.NU_CPF_CNPJ COLLATE Latin1_General_CI_AI AS NumCPFCNPJ 
    FROM 
      [DB_TELECOM].SC_CORPORATIVO.TB_ENTIDADE_NACIONAL AS EnNas 
      INNER JOIN db_telecom.SC_CORPORATIVO.TB_ENTIDADE AS EnCer ON EnNas.CO_ENTIDADE = EnCer.CO_SEQ_ENTIDADE 
    WHERE 
      EnNas.CO_ENTIDADE IN (
        SELECT 
          MAX(EnNas.CO_ENTIDADE) 
        FROM 
          [DB_TELECOM].SC_CORPORATIVO.TB_ENTIDADE_NACIONAL AS EnNas 
          INNER JOIN [DB_TELECOM].SC_CORPORATIVO.TB_ENTIDADE ON EnNas.CO_ENTIDADE = CO_SEQ_ENTIDADE 
        WHERE 
          IC_SITUACAO = 1 
        GROUP BY 
          EnNas.NU_CPF_CNPJ
      ) 
    UNION 
      -- QUERY Todas as Entidades no Sitarweb
    SELECT 
      DISTINCT ent.numcnpjcpf COLLATE Latin1_General_CI_AI AS NumCNPJCPF 
    FROM 
      SITARWEB.DBO.ENTIDADE AS Ent 
    UNION 
      -- QUERY Todas as Entidades sancionadas em Pados pela Agência
    SELECT 
      DISTINCT pad.NumCnpjCpf COLLATE Latin1_General_CI_AI AS NumCNPJCPF 
    FROM 
      SPADO.dbo.InstauracaoFoto AS pad
  ) 
  AND SRF.NumCNPJCPF NOT IN (
    -- retira Servidores da Anatel da pesquisa
    SELECT 
      DISTINCT [NumCpf] COLLATE Latin1_General_CI_AI AS NumCPFCNPJ 
    FROM 
      [SARH].[dbo].[Empregado] 
    WHERE 
      NumCpf IS NOT NULL 
    UNION 
      -- retira colaboradores terceirizados da Anatel da pessquisa
    SELECT 
      DISTINCT [NumCPFEmpTer] COLLATE Latin1_General_CI_AI AS NumCPFCNPJ 
    FROM 
      [SARH].[dbo].[EmpregadoTerceirizado] 
    WHERE 
      [NumCPFEmpTer] IS NOT NULL 
    UNION 
      --Query retira usuários DO SIS
    SELECT 
      DISTINCT ent.numcnpjcpf COLLATE Latin1_General_CI_AI AS NumCNPJCPF 
    FROM 
      SITARWEB.DBO.ENTIDADE AS Ent 
      LEFT JOIN SITARWEB.DBO.HABILITACAO AS Hab ON Ent.IdtEntidade = Hab.idtEntidade 
      LEFT JOIN SPADO.dbo.InstauracaoFoto AS pado ON ent.NumCnpjCpf = pado.NumCnpjCpf 
    WHERE 
      hab.NumFistel IS NULL 
      AND Hab.IdtEntidade IS NULL 
      AND pado.NumCnpjCpf IS NULL
  );
