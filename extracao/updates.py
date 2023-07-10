# AUTOGENERATED! DO NOT EDIT! File to edit: ..\nbs\updates.ipynb.

# %% auto 0
__all__ = [
    "connect_db",
    "clean_mosaico",
    "update_radcom",
    "update_stel",
    "update_srd",
    "update_telecom",
    "update_aero",
    "validar_coords",
    "update_cached_df",
    "update_base",
]

# %% ..\nbs\updates.ipynb 2
import os
from decimal import Decimal, getcontext
from typing import Union, List
import gc

import numpy as np
import pandas as pd
import pyodbc
from rich.console import Console
from rich import print
from pyarrow import ArrowInvalid, ArrowTypeError
from fastcore.xtras import Path
from fastcore.utils import partialler
from fastcore.parallel import parallel
import pyodbc
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

from .icao import get_icao
from .aisgeo import get_aisg
from .aisweb import get_aisw
from .redemet import get_redemet
from .constants import *
from .format import parse_bw, merge_on_frequency, _read_df

getcontext().prec = 5
load_dotenv(find_dotenv())


# %% ..\nbs\updates.ipynb 4
def connect_db(
    server: str = "ANATELBDRO05",  # Servidor do Banco de Dados
    database: str = "SITARWEB",  # Nome do Banco de Dados
    trusted_conn: str = "yes",  # Conexão Segura: yes | no
    mult_results: bool = True,  # Múltiplos Resultados
) -> pyodbc.Connection:
    """Conecta ao Banco `server` e retorna o 'cursor' (iterador) do Banco"""
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        f"Server={server};"
        f"Database={database};"
        f"Trusted_Connection={trusted_conn};"
        f"MultipleActiveResultSets={mult_results};",
        timeout=TIMEOUT,
    )


# %% ..\nbs\updates.ipynb 7
def clean_mosaico(
    df: pd.DataFrame,  # DataFrame com os dados de Estações e Plano_Básico mesclados
    pasta: Union[
        str, Path
    ],  # Pasta com os dados de municípios para imputar coordenadas ausentes
) -> pd.DataFrame:  # DataFrame com os dados mesclados e limpos
    """Clean the merged dataframe with the data from the MOSAICO page"""
    df = df[
        df.Status.str.contains("-C1$|-C2$|-C3$|-C4$|-C7|-C98$", na=False)
    ].reset_index(drop=True)
    for c in df.columns:
        df.loc[df[c] == "", c] = pd.NA
    df.loc["Frequência"] = df.Frequência.astype("str").str.replace(",", ".")
    df = df[df.Frequência.notna()].reset_index(drop=True)
    df.loc["Frequência"] = df.Frequência.astype("float")
    df.loc[df.Num_Serviço == "205", "Frequência"] = df.loc[
        df.Num_Serviço == "205", "Frequência"
    ].apply(lambda x: Decimal(x) / Decimal(1000))
    df.loc[:, "Validade_RF"] = df.Validade_RF.astype("string").str.slice(0, 10)
    return df


# %% ..\nbs\updates.ipynb 9
def _save_df(df: pd.DataFrame, folder: Union[str, Path], stem: str) -> pd.DataFrame:
    """Format, Save and return a dataframe"""
    df = df.copy()  # Impedir a alteração do df original
    for c in df.columns:
        df[c] = df[c].astype("string").str.lstrip().str.rstrip()
    df = df.drop_duplicates(keep="first").reset_index(drop=True)
    if "Código_Município" in df:
        df = df[df.Código_Município.notna()].reset_index(drop=True)
    try:
        file = Path(f"{folder}/{stem}.parquet.gzip")
        df.to_parquet(file, compression="gzip", index=False)
    except (ArrowInvalid, ArrowTypeError) as e:
        raise e(f"Não possível salvar o arquivo parquet {file}") from e
    return df


# %% ..\nbs\updates.ipynb 11
def update_radcom(
    conn: pyodbc.Connection,  # Objeto de conexão de banco
    folder: Union[str, Path],  # Pasta onde salvar os arquivos
) -> pd.DataFrame:  # DataFrame com os dados atualizados
    """Atualiza a tabela local retornada pela query `RADCOM`, com tratamento de erro de conectividade."""
    console = Console()
    with console.status(
        "[cyan]Lendo o Banco de Dados de Radcom...", spinner="monkey"
    ) as status:
        try:
            return _extract_radcom(conn, folder)
        except pyodbc.OperationalError as e:
            status.console.log(
                "Não foi possível abrir uma conexão com o SQL Server. Esta conexão somente funciona da rede cabeada!"
            )
            raise ConnectionError from e


def _extract_radcom(
    conn: pyodbc.Connection,  # Objeto de conexão de banco
    folder: Union[str, Path],  # Pasta onde salvar os arquivos
) -> pd.DataFrame:  # DataFrame com os dados atualizados
    df = pd.read_sql_query(SQL_RADCOM, conn, dtype="string")
    df["Entidade"] = df.Entidade.str.rstrip().str.lstrip()
    df["Num_Serviço"] = "231"
    df["Classe_Emissão"] = pd.NA
    df["Largura_Emissão(kHz)"] = "256"
    df["Validade_RF"] = pd.NA
    df["Status"] = "RADCOM"
    df["Fonte"] = "SRD"
    df["Multiplicidade"] = "1"
    a = df.Situação.isna()
    df.loc[a, "Classe"] = df.loc[a, "Fase"]
    df.loc[~a, "Classe"] = (
        df.loc[~a, "Fase"].astype("string")
        + "-"
        + df.loc[~a, "Situação"].astype("string")
    )
    df.drop(["Fase", "Situação"], axis=1, inplace=True)
    df = df.loc[:, COLUNAS]
    return _save_df(df, folder, "radcom")


# %% ..\nbs\updates.ipynb 16
def update_stel(
    conn: pyodbc.Connection,  # Objeto de conexão de banco
    folder: Union[str, Path],  # Pasta onde salvar os arquivos
) -> pd.DataFrame:  # DataFrame com os dados atualizados
    """Atualiza a tabela local retornada pela query `STEL`, com tratamento de erro de conectividade."""
    console = Console()
    with console.status(
        "[red]Lendo o Banco de Dados do STEL",
        spinner="grenade",
    ) as status:
        try:
            return _extract_stel(conn, folder)
        except pyodbc.OperationalError as e:
            status.console.log(
                "Não foi possível abrir uma conexão com o SQL Server. Esta conexão somente funciona da rede cabeada!"
            )
            raise ConnectionError from e


def _extract_stel(
    conn: pyodbc.Connection,  # Objeto de conexão de banco
    folder: Union[str, Path],  # Pasta onde salvar os arquivos
) -> pd.DataFrame:  # DataFrame com os dados atualizados
    """Atualiza a tabela local retornada pela query `STEL`"""
    stel = pd.read_sql_query(SQL_STEL, conn)
    stel["Status"] = "L"
    stel["Entidade"] = stel.Entidade.str.rstrip().str.lstrip()
    stel["Fonte"] = "STEL"
    stel.loc[:, ["Largura_Emissão(kHz)", "_"]] = (
        stel.Largura_Emissão.fillna("").apply(parse_bw).tolist()
    )
    stel.drop(["Largura_Emissão", "_"], axis=1, inplace=True)
    stel.loc[:, "Validade_RF"] = stel.Validade_RF.astype("string").str.slice(0, 10)
    stel.loc[stel.Unidade == "kHz", "Frequência"] = stel.loc[
        stel.Unidade == "kHz", "Frequência"
    ].apply(lambda x: Decimal(x) / Decimal(1000))
    stel.loc[stel.Unidade == "GHz", "Frequência"] = stel.loc[
        stel.Unidade == "GHz", "Frequência"
    ].apply(lambda x: Decimal(x) * Decimal(1000))
    stel.drop("Unidade", axis=1, inplace=True)
    stel["Multiplicidade"] = 1
    stel = stel.loc[:, COLUNAS]
    return _save_df(stel, folder, "stel")


# %% ..\nbs\updates.ipynb 19
def update_srd(
    mongo_client: MongoClient,  # Objeto de conexão com o MongoDB
    folder: Union[str, Path],  # Pasta onde salvar os arquivos
) -> pd.DataFrame:  # DataFrame com os dados atualizados
    """Efetua a query na tabela de Radiodifusão no banco mongoDB `mongo_client` e atualiza o arquivo local"""
    console = Console()
    with console.status(
        "Consolidando os dados do Mosaico...", spinner="runner"
    ) as status:
        database = mongo_client["sms"]
        collection = database["srd"]
        list_data = list(collection.find(MONGO_SRD, projection=COLS_SRD.keys()))
        mosaico = pd.json_normalize(list_data)
        mosaico = mosaico.drop(columns=["estacao"])
        mosaico = mosaico[list(COLS_SRD.keys())]
        mosaico.rename(COLS_SRD, axis=1, inplace=True)
        mosaico = clean_mosaico(mosaico, folder)
        mosaico["Fonte"] = "MOS"
        mosaico["Num_Serviço"].fillna("", inplace=True)
        mosaico.loc[:, ["Largura_Emissão(kHz)", "Classe_Emissão"]] = (
            mosaico.Num_Serviço.astype("string")
            .fillna("")
            .map(BW_MAP)
            .apply(parse_bw)
            .tolist()
        )
        mosaico.loc[mosaico.Classe_Emissão == "", "Classe_Emissão"] = pd.NA
        mosaico["Multiplicidade"] = 1
        mosaico = mosaico.loc[:, COLUNAS]
    return _save_df(mosaico, folder, "srd")


# %% ..\nbs\updates.ipynb 23
def update_telecom(
    mongo_client: MongoClient,  # Objeto de conexão com o MongoDB
    folder: Union[str, Path],  # Pasta onde salvar os arquivos
) -> pd.DataFrame:  # DataFrame com os dados atualizados
    """Efetua a query na tabela `licenciamento` no banco mongoDB `mongo_client` e atualiza o arquivo local"""

    database = mongo_client["sms"]
    collection = database["licenciamento"]
    query = collection.find(
        MONGO_TELECOM, projection={k: 1.0 for k in COLS_TELECOM.keys()}, limit=0
    )
    print(
        "[red] :warning: Executando a query na base licenciamento do Mosaico, processo demorado! :warning:"
    )
    df = pd.DataFrame(list(query), columns=COLS_TELECOM.keys(), dtype="string")
    path_cache = Path(f"{folder}/telecom_raw.parquet.gzip")
    path_out = Path(f"{folder}/telecom.parquet.gzip")
    if path_cache.is_file():
        cache_df = pd.read_parquet(path_cache)
        if df.equals(cache_df) and path_out.is_file():
            del df
            gc.collect()
            return pd.read_parquet(path_out)
    df.to_parquet(path_cache, compression="gzip", index=False)
    return _process_telecom(df, folder)


def _process_telecom(
    df: pd.DataFrame,  # Dataframe não processado de dados do Mosaico
    folder: Union[str, Path],  # Pasta onde salvar os arquivos
) -> pd.DataFrame:
    """Formata e pós-processa e mescla os dados de Telecomunicações do Mosaico"""
    # df.drop("_id", axis=1, inplace=True)
    df.rename(COLS_TELECOM, axis=1, inplace=True)
    df["Designacao_Emissão"] = df.Designacao_Emissão.str.replace(",", " ")
    df["Designacao_Emissão"] = (
        df.Designacao_Emissão.str.strip().str.lstrip().str.rstrip().str.upper()
    )
    df["Designacao_Emissão"] = df.Designacao_Emissão.str.split(" ")
    df = df.explode("Designacao_Emissão", ignore_index=True)
    df.loc[df.Designacao_Emissão == "/", "Designacao_Emissão"] = ""
    df.loc[:, ["Largura_Emissão(kHz)", "Classe_Emissão"]] = df.Designacao_Emissão.apply(
        parse_bw
    ).tolist()
    df.drop("Designacao_Emissão", axis=1, inplace=True)
    subset = [
        "Frequência",
        "Entidade",
        "Fistel",
        "Código_Município",
        "Longitude",
        "Latitude",
        "Classe",
        "Num_Serviço",
        "Classe_Emissão",
        "Largura_Emissão(kHz)",
    ]
    df.dropna(subset=subset, axis=0, inplace=True)
    df_sub = (
        df[~df.duplicated(subset=subset, keep="first")].reset_index(drop=True).copy()
    )
    df_sub["Multiplicidade"] = (
        df.groupby(subset, sort=False).count()["Número_Estação"]
    ).tolist()
    df_sub["Status"] = "L"
    df_sub["Fonte"] = "MOS"
    del df
    gc.collect()
    df_sub = df_sub.reset_index()
    df_sub = df_sub.loc[:, COLUNAS]
    return _save_df(df_sub, folder, "telecom")


# %% ..\nbs\updates.ipynb 26
def update_aero(
    folder: Union[str, Path],  # Pasta onde salvar os arquivos
) -> pd.DataFrame:  # DataFrame com os dados atualizados
    """Atualiza a base de dados de emissões da aeronáutica"""
    icao = get_icao()
    aisw = get_aisw()
    aisg = get_aisg()
    redemet = get_redemet()
    radares = pd.read_excel(os.environ["PATH_RADAR"])
    for df in [aisw, aisg, redemet, radares]:
        icao = merge_on_frequency(icao, df)
    icao = icao.astype(
        {
            "Frequency": "float64",
            "Latitude": "float32",
            "Longitude": "float32",
            "Description": "string",
        }
    )
    # TODO: Eliminate this eventually
    icao.loc[np.isclose(icao.Longitude, -472.033447), "Longitude"] = -47.2033447
    icao.loc[np.isclose(icao.Longitude, 69.934998), "Longitude"] = -69.934998
    return _save_df(icao, folder, "aero")


# %% ..\nbs\updates.ipynb 28
def validar_coords(
    row: pd.Series,  # Linha de um DataFrame
    connector: pyodbc.Connection = None,  # Conector de Banco de Dados
) -> List[str]:  # DataFrame com dados do município
    """Valida os dados de coordenadas e município em `row` no polígono dos municípios em banco corporativ do IBGE"""

    mun, cod, lat, long = (
        row.Município,
        row.Código_Município,
        row.Latitude,
        row.Longitude,
    )
    is_valid = "-1"
    conn = connect_db() if connector is None else connector
    crsr = conn.cursor()
    sql = SQL_VALIDA_COORD.format(long, lat, cod)
    crsr.execute(sql)
    result = crsr.fetchone()
    if result is not None:
        mun = result.NO_MUNICIPIO
        lat = result.NU_LATITUDE
        long = result.NU_LONGITUDE
        is_valid = result.COORD_VALIDA
    if connector is None:
        del conn
    return [str(mun), str(lat), str(long), str(is_valid)]


# %% ..\nbs\updates.ipynb 29
def update_cached_df(df: pd.DataFrame, df_cache: pd.DataFrame) -> pd.DataFrame:
    """Mescla ambos dataframes eliminando os excluídos (existentes somente em df_cache)"""

    # Merge dataframes based on all columns except "Coords_Valida_IBGE"
    merged = pd.merge(
        df_cache,
        df,
        on=list(df.columns),
        how="outer",
        indicator=True,
        copy=False,
        validate="one_to_one",
    ).astype("string")

    # Identify rows only present in df_cache
    # df_cache_only = merged[merged["_merge"] == "left_only"] #TODO: Data logging

    # Identify news rows
    # df_new = merged[merged["_merge"] == "right_only"] #TODO: Data logging

    # Exclude rows only present in df_cache
    df_cache = merged[merged["_merge"] != "left_only"]

    # inplace=True not working
    df_cache.loc[:, ["Latitude", "Longitude"]] = df_cache.loc[
        :, ["Latitude", "Longitude"]
    ].fillna("-1")

    # # Drop the _merge column
    return df_cache.drop(columns="_merge")


# %% ..\nbs\updates.ipynb 30
def _validar_coords_base(
    df: pd.DataFrame,  # DataFrame com os dados da Anatel
    df_cache: pd.DataFrame,  # DataFrame validado anteriormente, usado como cache
    connector: pyodbc.Connection = None,  # Conector de Banco de Dados
) -> pd.DataFrame:  # DataFrame com as coordenadas validadas na base do IBGE
    """Valida as coordenadas consultado a Base Corporativa do IBGE, excluindo o que já está no cache na versão anterior"""

    ibge = ["Município_IBGE", "Latitude_IBGE", "Longitude_IBGE", "Coords_Valida_IBGE"]

    df_cache = update_cached_df(df.astype("string"), df_cache.astype("string"))

    subset = df_cache.Coords_Valida_IBGE.isna()

    linhas = list(
        df_cache.loc[
            subset, ["Município", "Código_Município", "Latitude", "Longitude"]
        ].itertuples()
    )

    func = partialler(validar_coords, connector=connector)

    # Gambiarra para evitar compartilhamento da mesma conexão de banco em diferentes threads
    n_workers = 1 if connector is not None else 20

    df_cache.loc[subset, ibge] = parallel(
        func, linhas, threadpool=True, n_workers=n_workers, progress=True
    )

    df_cache = df_cache.astype("string")

    df_cache.loc[df_cache.Coords_Valida_IBGE == "-1", "Coords_Valida_IBGE"] = pd.NA

    return df_cache


# %% ..\nbs\updates.ipynb 31
def update_base(
    conn: pyodbc.Connection,  # Objeto de conexão de banco
    clientMongoDB: MongoClient,  # Objeto de conexão com o MongoDB
    folder: Union[str, Path],  # Pasta onde salvar os arquivos
    conn_threads: bool = False,  # Flag para criar uma conexão de banco por thread
) -> pd.DataFrame:  # DataFrame com os dados atualizados
    # sourcery skip: use-fstring-for-concatenation
    """Wrapper que atualiza opcionalmente lê e atualiza as 4 bases indicadas anteriormente, as combina e salva o arquivo consolidado na folder `folder`"""
    stel = update_stel(conn, folder)
    radcom = update_radcom(conn, folder)
    mosaico = update_srd(clientMongoDB, folder)
    telecom = update_telecom(clientMongoDB, folder)

    df = (
        pd.concat([mosaico, radcom, stel, telecom])
        .sort_values(["Frequência", "Latitude", "Longitude"])
        .reset_index(drop=True)
    ).astype("string")

    # inplace not working!
    df.loc[:, ["Latitude", "Longitude"]] = df.loc[:, ["Latitude", "Longitude"]].fillna(
        "0"
    )
    try:
        df_cache = _read_df(folder, "base")
    except FileNotFoundError:
        df_cache = pd.DataFrame(columns=df.columns.to_list() + ["Coords_Valida_IBGE"])

    connector = None if conn_threads else conn

    df_cache = _validar_coords_base(df, df_cache, connector)

    return _save_df(df_cache, folder, "base")
