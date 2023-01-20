# AUTOGENERATED! DO NOT EDIT! File to edit: ..\nbs\icao.ipynb.

# %% auto 0
__all__ = ['COLS_NAV', 'COLS_COM', 'convert_latitude', 'convert_longitude', 'map_channels', 'get_icao']

# %% ..\nbs\icao.ipynb 2
import os
from typing import Iterable
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# %% ..\nbs\icao.ipynb 5
COLS_NAV = ["Frequency", "Latitude", "Longitude", "Facility", "Location", "NS", "WE"]
COLS_COM = ["Frequency", "CoordLat", "CoordLong", "DOC", "Location", "NS", "WE"]

# %% ..\nbs\icao.ipynb 6
def convert_latitude(
    lat: str,  # Latitude
    hemisphere: str,  # Hemisfério: N | S
) -> float:
    """Converte a Latitude para formato decimal"""
    multiplier = 1 if hemisphere == "N" else -1
    return multiplier * (
        float(lat[:2]) + float(lat[3:5]) / 60 + float(lat[6:8]) / 3600.0
    )


def convert_longitude(
    lon: str,  # Longitude
    hemisphere: str,  # Hemisfério: W | E
) -> float:
    """Converte a longitude para formato decimal"""

    multiplier = 1 if hemisphere == "E" else -1
    return multiplier * (
        float(lon[1:3]) + float(lon[4:6]) / 60 + float(lon[7:9]) / 3600.0
    )


# %% ..\nbs\icao.ipynb 8
def _read_df(
    path: str,  # Caminho do arquivo
    usecols: Iterable[str],  # Subconjunto de colunas do arquivo
) -> pd.DataFrame:  # Dataframe formatado
    # sourcery skip: use-fstring-for-concatenation
    """Lê o DataFrame no caminho `path`, filtra as colunas `usecols` e o retorna formatado"""
    df = pd.read_excel(path, engine="openpyxl", dtype="string")[usecols]
    df.columns = COLS_NAV
    df["Latitude"] = df.apply(
        lambda x: convert_latitude(x["Latitude"], x["NS"]), axis=1
    )
    df["Longitude"] = df.apply(
        lambda x: convert_longitude(x["Longitude"], x["WE"]), axis=1
    )
    df["Description"] = "[ICAO] " + df.Facility + ", " + df.Location
    return df[["Frequency", "Latitude", "Longitude", "Description"]]


# %% ..\nbs\icao.ipynb 9
def map_channels(
    df: pd.DataFrame,  # DataFrame dos dados de origem
    origem: str,  # Descrição da emissão a ser substituída
) -> pd.DataFrame:
    """Mapeia os canais contidos em `df` e adiciona os registros ILS/DME caso houver"""
    chs = pd.read_excel(os.environ["PATH_CHANNELS"], engine="openpyxl", dtype="string")
    for row in df[df.Description.str.contains("ILS|DME")].itertuples():
        if not (ch := chs[(chs.VOR_ILSloc == row.Frequency)]).empty:
            for i, c in enumerate(ch.values[0][2:]):
                if pd.notnull(c):
                    match i:
                        case 0:
                            freq_type = "ILS glide path"
                        case 1:
                            freq_type = "Airbone DME"
                        case 2:
                            freq_type = "Ground-based DME"
                    description = (
                        f"{row.Description.replace(origem , 'DOC')} ({freq_type})"
                    )
                    df.loc[len(df)] = [c, row.Latitude, row.Longitude, description]
    return df


# %% ..\nbs\icao.ipynb 10
def get_icao(
    path_nav: str = os.environ["PATH_NAV"],  # Caminho para o arquivo NAV
    path_com: str = os.environ["PATH_COM"],  # Caminho para o arquivo COM
) -> pd.DataFrame:  # DataFrame com frequências, coordenadas e descrição das estações
    """Lê, concatena e pós-processa os arquivos do ICAO"""
    df = pd.concat(
        _read_df(p, c) for p, c in zip([path_nav, path_com], [COLS_NAV, COLS_COM])
    )
    for c in df.columns:
        df[c] = df[c].astype("string")
    return map_channels(df, "ICAO")
