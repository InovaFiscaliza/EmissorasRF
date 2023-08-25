# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/08_aisgeo.ipynb.

# %% auto 0
__all__ = ['LINK_VOR', 'LINK_DME', 'LINK_NDB', 'COLS_VOR', 'COLS_NDB', 'COLS_DME', 'UNIQUE_COLS', 'convert_frequency',
           'get_geodf', 'get_aisg']

# %% ../../nbs/08_aisgeo.ipynb 2
import json
import os
from pathlib import Path
from typing import List
from urllib.request import urlopen

import pandas as pd
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(), override=True)

# %% ../../nbs/08_aisgeo.ipynb 5
LINK_VOR = "https://geoaisweb.decea.mil.br/geoserver/ICA/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=ICA:vor&outputFormat=application%2Fjson"
LINK_DME = "https://geoaisweb.decea.mil.br/geoserver/ICA/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=ICA:dme&outputFormat=application%2Fjson"
LINK_NDB = "https://geoaisweb.decea.mil.br/geoserver/ICA/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=ICA:ndb&outputFormat=application%2Fjson"
COLS_VOR = (
    "properties.frequency",
    "properties.frequnits",
    "properties.latitude",
    "properties.longitude",
    "properties.tipo",
    "properties.txtname",
    "properties.txtrmk",
)
COLS_NDB = (
    "properties.valfreq",
    "properties.uomfreq",
    "properties.geolat",
    "properties.geolong",
    "properties.tipo",
    "properties.txtname",
    "properties.txtrmk",
)

COLS_DME = (
    "properties.valchannel",
    "properties.codechanne",
    "properties.geolat",
    "properties.geolong",
    "properties.tipo",
    "properties.txtname",
    "Channel",
)

UNIQUE_COLS = ["Frequency", "Latitude", "Longitude"]


# %% ../../nbs/08_aisgeo.ipynb 6
def convert_frequency(
    freq: float,  # Frequência Central da emissão
    unit: str,  # Unidade da Frequência: [Hz, kHz, MHZ, GHZ]
) -> float:  # Frequência em MHz
    """Converte a frequência `freq` para MHz"""
    match unit.upper():
        case "HZ":
            result = freq / 1e6
        case "KHZ":
            result = freq / 1000
        case "MHZ":
            result = freq
        case "GHZ":
            result = freq * 1000
        case _:
            result = -1
    return result


# %% ../../nbs/08_aisgeo.ipynb 7
def _process_frequency(
    df: pd.DataFrame,  # Dataframe com os dados
    cols: List[str],  # Subconjunto de Colunas relevantes do DataFrame
) -> pd.DataFrame:  # Dataframe com os dados de frequência devidamente processados
    if cols == COLS_DME:
        df_channels = pd.read_csv(
            f'{Path(__file__).parent}/{os.environ["PATH_CHANNELS"]}', dtype="string"
        )
        df = df.dropna(subset=[cols[0]])
        df["Channel"] = df[cols[0]].astype("int").astype("string") + df[cols[1]]
        df["Frequency"] = -1.0

        for row in df.itertuples(index=True):
            row_match = df_channels.loc[
                (df_channels.Channel == row.Channel), "DMEground"
            ]
            if not row_match.empty:
                df.loc[row.Index, "Frequency"] = float(row_match.item())

    else:
        df["Frequency"] = (
            df[[cols[0], cols[1]]]
            .apply(lambda x: convert_frequency(x[0], x[1]), axis=1)
            .astype("float")
        )
    return df


# %% ../../nbs/08_aisgeo.ipynb 8
def _filter_df(df, cols):  # sourcery skip: use-fstring-for-concatenation
    df.fillna("", inplace=True)
    df["Description"] = (
        "[AISG] " + df[cols[4]] + " - " + df[cols[5]] + " " + df[cols[6]]
    ).astype("string")

    df = df[["Frequency", cols[2], cols[3], "Description"]]

    return df.rename(
        columns={
            cols[2]: "Latitude",
            cols[3]: "Longitude",
        }
    )


# %% ../../nbs/08_aisgeo.ipynb 9
def get_geodf(
    link: str,  # Link para a requisição das estações VOR do GEOAISWEB
    cols: List[str],  # Subconjunto de Colunas relevantes do DataFrame
) -> (
    pd.DataFrame
):  # DataFrame com frequências, coordenadas e descrição das estações VOR
    # sourcery skip: use-fstring-for-concatenation
    """Faz a requisição do `link`, processa o json e o retorna como Dataframe"""
    response = urlopen(link)
    if (
        response.status != 200
        or "application/json" not in response.headers["content-type"]
    ):
        raise ValueError(
            f"Resposta a requisição não foi bem sucedida: {response.status=}"
        )
    data_json = json.loads(response.read())
    df = pd.json_normalize(
        data_json["features"],
    ).filter(cols, axis=1)
    df = _process_frequency(df, cols)
    return _filter_df(df, cols)


# %% ../../nbs/08_aisgeo.ipynb 13
def get_aisg() -> pd.DataFrame:  # DataFrame com todos os dados do GEOAISWEB
    """Lê e processa os dataframes individuais da API GEOAISWEB e retorna o conjunto concatenado"""
    df = pd.concat(
        get_geodf(link, cols)
        for link, cols in zip(
            [LINK_NDB, LINK_VOR, LINK_DME], [COLS_NDB, COLS_VOR, COLS_DME]
        )
    )
    return df.astype("string").drop_duplicates(UNIQUE_COLS, ignore_index=True)
