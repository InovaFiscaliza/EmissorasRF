# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/07_aisweb.ipynb.

# %% auto 0
__all__ = ['SIGLA_AERO', 'URL', 'TYPE', 'COLUMNS', 'UNIQUE_COLS', 'convert_latitude', 'convert_longitude', 'AisWeb', 'get_aisw']

# %% ../../nbs/07_aisweb.ipynb 2
import os
import re
from functools import cached_property
from typing import Iterable

import pandas as pd
import requests
import xmltodict
from dotenv import find_dotenv, load_dotenv
from fastcore.parallel import parallel
from fastcore.utils import store_attr

from .icao import map_channels

load_dotenv(find_dotenv(), override=True)

# %% ../../nbs/07_aisweb.ipynb 5
SIGLA_AERO = ["MIL", "PRIV/PUB", "PUB", "PUB/MIL", "PUB/REST"]
URL = "http://aisweb.decea.gov.br/api/?apiKey={}&apiPass={}&area=rotaer&rowend=10000"
TYPE = ["COM", "NAV"]
COLUMNS = ["Frequency", "Latitude", "Longitude", "Description"]
UNIQUE_COLS = ["Frequency", "Latitude", "Longitude"]

# %% ../../nbs/07_aisweb.ipynb 6
def convert_latitude(
    lat: str,  # Latitude
) -> float:
    """Converte a Latitude para formato decimal"""
    hemisphere = lat[-1]
    multiplier = 1 if hemisphere == "N" else -1
    return multiplier * (
        float(lat[:2]) + float(lat[2:4]) / 60 + float(lat[5:7]) / 3600.0
    )


def convert_longitude(
    lon: str,  # Longitude
) -> float:
    """Converte a longitude para formato decimal"""
    hemisphere = lon[-1]
    multiplier = 1 if hemisphere == "E" else -1
    return multiplier * (
        float(lon[:3]) + float(lon[3:5]) / 60 + float(lon[6:8]) / 3600.0
    )

# %% ../../nbs/07_aisweb.ipynb 7
class AisWeb:
    """Classe para encapsular requisições REST à API do AISWEB"""

    def __init__(
        self,
        api_key: str,  # Chave API
        api_pass: str,  # Senha API
        type_aero: Iterable[str] = SIGLA_AERO,  # Lista com os tipos de Aeroportos
    ):
        store_attr()
        self.url = URL.format(api_key, api_pass)

    def _get_request(self, key, value):
        request_url = f"{self.url}{key}{value}"
        response = requests.get(request_url)
        if response.status_code != 200:
            raise ValueError(
                f"Resposta a requisição não foi bem sucedida: {response.status_code:=}"
            )
        return xmltodict.parse(response.content)

    def request_aero(
        self,
        aero_util: str,  # Sigla de identificação do tipo de Aeroporto
    ) -> pd.DataFrame:  # DataFrame com os dados do Aeroporto
        """Recebe a sigla `aero_util` do tipo de aeroporto e faz a requisição à API"""
        dict_data = self._get_request("&util=", aero_util)
        if int(dict_data["aisweb"]["rotaer"]["@total"]) > 0:
            df = pd.json_normalize(dict_data["aisweb"]["rotaer"]["item"])
            df.drop(["@ciad_id", "id", "ciad", "dt"], axis=1, inplace=True)
            # Remove os não aeródromos
            return df[df.type == "AD"].reset_index(drop=True)
        return pd.DataFrame()

    @cached_property
    def airports(
        self,
    ) -> pd.DataFrame:  # DataFrame com os dados de aeroportos
        """Retorna a lista de aeroportos"""
        airports = parallel(
            self.request_aero,
            self.type_aero,
            n_workers=1,
            pause=0.1,
            progress=True,
            threadpool=True,
        )
        return pd.concat(airports)

    def _parse_type(self, df):
        df = df[df["@type"].isin(TYPE)].reset_index(drop=True)
        if "type" in df.columns:
            df["Description"] = [
                ", ".join(cols) for cols in zip(df["@type"], df["type"])
            ]  # Only way to prevent bizarre errors
            df = df.drop(["@type", "type"], axis=1)
        return df

    def _filter_freq(self, df):
        if "freqs.freq" in df:
            df = df.explode("freqs.freq")
            idx = df["freqs.freq"].notnull()
            df.loc[idx, "Frequency"] = df.loc[idx, "freqs.freq"].apply(
                lambda x: x.get("#text", pd.NA)
            )
            df = df.drop("freqs.freq", axis=1)

        if (column := "freqs.freq.#text") in df:
            idx = df[column].notnull()
            df.loc[idx, "Frequency"] = df.loc[idx, column]
            df = df.drop("freqs.freq.#text", axis=1)

        return df.reset_index(drop=True)

    def _check_ils_dme(self, df):
        if (columns := {"freq", "lat", "lng", "thr", "ident"}).issubset(df.columns):
            idx = df.freq.notna()
            df.loc[idx, "Frequency"] = df.loc[idx, "freq"]
            df.loc[idx, "Latitude"] = df.loc[idx, "lat"].apply(
                lambda x: convert_latitude(x)
            )
            df.loc[idx, "Longitude"] = df.loc[idx, "lng"].apply(
                lambda x: convert_longitude(x)
            )
            df.loc[idx, "Description"] = (
                df.loc[idx, "Description"]
                + " "
                + df.loc[idx, "thr"]
                + " "
                + df.loc[idx, "ident"]
            )
            df = df.drop(columns, axis=1)
        return df

    def _process_coords(self, df, airport_data):
        # sourcery skip: use-fstring-for-concatenation
        df.loc[df["Latitude"] == "", "Latitude"] = airport_data.lat
        df.loc[df["Longitude"] == "", "Longitude"] = airport_data.lng
        if not df.empty:
            df["Description"] = (
                r"[AISW] "
                + str(airport_data["AeroCode"])
                + "-"
                + df["Description"]
                + ", "
                + str(airport_data["name"])
            )
        return df

    def _process_data(
        self,
        dict_data,  # xml com os dados não processados
    ) -> pd.DataFrame:  # DataFrame com os dados pós-processados
        airport_data = pd.json_normalize(dict_data["aisweb"])
        columns = {"AeroCode", "name", "lat", "lng"}
        if not columns.issubset(airport_data.columns):
            return pd.DataFrame()
        airport_data = airport_data[list(columns)].iloc[0]
        df = pd.json_normalize(dict_data, ["aisweb", ["services", "service"]])
        df[COLUMNS] = ""
        df = self._parse_type(df)
        df = self._filter_freq(df)
        df = self._check_ils_dme(df)
        df = self._process_coords(df, airport_data)
        df = df[COLUMNS]
        df["Frequency"] = df.Frequency.apply(lambda x: "".join(re.findall("\d|\.", x)))
        df = df[~df["Frequency"].isin({"", "0"})].reset_index(drop=True)
        df["Frequency"] = df.Frequency.str.extract(r"(^\d+\.?\d*)")
        df["Frequency"] = df.Frequency.astype("float")
        return df

    def request_stations(
        self,
        icao_code: str,  # Código ICAO identificando o aeroporto
    ) -> (
        pd.DataFrame
    ):  # DataFrame com os dados de estações do aeroporto de código `icao_code`
        """Recebe o código do aeroporto `icao_code` e retorna as estações registradas nele"""
        dict_data = self._get_request("&icaoCode=", icao_code)
        return (
            self._process_data(dict_data) if dict_data.get("aisweb") else pd.DataFrame()
        )

    @cached_property
    def records(
        self,
    ) -> pd.DataFrame:  # DataFrame com os dados de estações emissoras
        """Retorna os registros de estações emissoras de RF contidas nos aeroportos"""
        records = parallel(
            self.request_stations,
            self.airports.AeroCode,
            threadpool=True,
            n_workers=8,
            pause=0.1,
            progress=True,
        )
        df = pd.concat(records).astype("string")
        return map_channels(df, "AISW").drop_duplicates(UNIQUE_COLS, ignore_index=True)

# %% ../../nbs/07_aisweb.ipynb 8
def get_aisw() -> pd.DataFrame:  # DataFrame com todos os dados do GEOAISWEB
    """Lê e processa os dataframes individuais da API AISWEB e retorna o conjunto concatenado"""
    aisweb = AisWeb(os.environ["AISWKEY"], os.environ["AISWPASS"])
    return aisweb.records
