# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01c_sitarweb.ipynb.

# %% auto 0
__all__ = ['SQLSERVER_PARAMS', 'Sitarweb', 'Radcom', 'Stel']

# %% ../../nbs/01c_sitarweb.ipynb 3
import os
import sys
from decimal import Decimal, getcontext

import pandas as pd
from dotenv import find_dotenv, load_dotenv
from fastcore.foundation import GetAttr

from extracao.constants import (
    COLUNAS,
    SQL_RADCOM,
    SQL_STEL,
)

from .base import Base
from .connectors import SQLServer

# %% ../../nbs/01c_sitarweb.ipynb 4
getcontext().prec = 5
load_dotenv(find_dotenv(), override=True)

# %% ../../nbs/01c_sitarweb.ipynb 6
SQLSERVER_PARAMS = dict(
    driver=os.environ.get("SQL_DRIVER"),
    server=os.environ.get("SQL_SERVER"),
    database=os.environ.get("SQL_DATABASE"),
    trusted_conn=True,
    mult_results=True,
    encrypt=False,
    timeout=int(os.environ.get("SQL_TIMEOUT")),
)

if sys.platform in ("linux", "darwin", "cygwin"):
    SQLSERVER_PARAMS.update(
        {
            "trusted_conn": False,
            "mult_results": False,
            "username": os.environ.get("USERNAME"),
            "password": os.environ.get("PASSWORD"),
        }
    )


class Sitarweb(Base, GetAttr):
    def __init__(self, sql_params: dict = SQLSERVER_PARAMS):
        self.default = SQLServer(sql_params)

    @property
    def columns(self):
        return COLUNAS

    @property
    def query(self):
        raise NotImplementedError("Subclasses devem implementar a propriedade 'query'")

    def extraction(self):
        return pd.read_sql_query(self.query, self.connect(), dtype="category")

# %% ../../nbs/01c_sitarweb.ipynb 7
class Radcom(Sitarweb):
    def __init__(self, sql_params: dict = SQLSERVER_PARAMS):
        super().__init__(sql_params)

    @property
    def query(self):
        return SQL_RADCOM

    @property
    def stem(self):
        return "radcom"

    def _format(
        self,
        df: pd.DataFrame,  # DataFrame com o resultantes do banco de dados
    ) -> pd.DataFrame:  # DataFrame formatado
        """Formata, limpa e padroniza os dados provenientes da query no banco"""
        df["Entidade"] = df["Entidade"].str.strip()
        df["Serviço"] = "231"
        df["Classe_Emissão"] = pd.NA
        df["Largura_Emissão(kHz)"] = "256"
        df["Validade_RF"] = pd.NA
        df["Status"] = "RADCOM"
        df["Fonte"] = "SRD"
        df["Multiplicidade"] = "1"
        a = df.Situação.isna()
        df.loc[a, "Classe"] = df.loc[a, "Fase"].astype("string")
        df.loc[~a, "Classe"] = (
            df.loc[~a, "Fase"].astype("string")
            + "-"
            + df.loc[~a, "Situação"].astype("string")
        )
        df.drop(["Fase", "Situação"], axis=1, inplace=True)
        df["Log"] = ""
        df["Frequência"] = pd.to_numeric(df["Frequência"], errors="coerce").astype(
            "float"
        )
        discarded = df[df.Frequência.isna()].copy()
        if not discarded.empty:
            log = """[("Colunas", "Frequência"),  
            ("Processamento", "Valor Nulo")]"""
            self.append2discarded(self.register_log(discarded, log))
        df.dropna(subset=["Frequência"], inplace=True)
        return df.loc[:, self.columns]

# %% ../../nbs/01c_sitarweb.ipynb 8
class Stel(Sitarweb):
    def __init__(self, sql_params: dict = SQLSERVER_PARAMS):
        super().__init__(sql_params)

    @property
    def query(self):
        return SQL_STEL

    @property
    def stem(self):
        return "stel"

    def _format(
        self,
        df: pd.DataFrame,  # DataFrame com o resultantes do banco de dados
    ) -> pd.DataFrame:  # DataFrame formatado
        """Formata, limpa e padroniza os dados provenientes da query no banco"""
        df["Status"] = "L"
        df["Entidade"] = df.Entidade.str.strip()
        df["Fonte"] = "STEL"
        df["Largura_Emissão"] = df["Largura_Emissão"].astype("string")
        df.loc[:, ["Largura_Emissão(kHz)", "_"]] = (
            df.Largura_Emissão.fillna("").apply(self.parse_bw).tolist()
        )
        df.drop(["Largura_Emissão", "_"], axis=1, inplace=True)
        df.loc[:, "Validade_RF"] = df.Validade_RF.astype("string").str.slice(0, 10)
        df["Frequência"] = df["Frequência"].astype("float")
        df.loc[df.Unidade == "kHz", "Frequência"] = df.loc[
            df.Unidade == "kHz", "Frequência"
        ].apply(lambda x: float(Decimal(x) / Decimal(1000)))
        df.loc[df.Unidade == "GHz", "Frequência"] = df.loc[
            df.Unidade == "GHz", "Frequência"
        ].apply(lambda x: float(Decimal(x) * Decimal(1000)))
        df.drop("Unidade", axis=1, inplace=True)
        df["Multiplicidade"] = 1
        df["Log"] = ""
        return df.loc[:, self.columns]

# %% ../../nbs/01c_sitarweb.ipynb 10
SQLSERVER_PARAMS = dict(
    driver=os.environ.get("SQL_DRIVER"),
    server=os.environ.get("SQL_SERVER"),
    database=os.environ.get("SQL_DATABASE"),
    trusted_conn=True,
    mult_results=True,
    encrypt=False,
    timeout=int(os.environ.get("SQL_TIMEOUT")),
)

if sys.platform in ("linux", "darwin", "cygwin"):
    SQLSERVER_PARAMS.update(
        {
            "trusted_conn": False,
            "mult_results": False,
            "username": os.environ.get("USERNAME"),
            "password": os.environ.get("PASSWORD"),
        }
    )


class Sitarweb(Base, GetAttr):
    def __init__(self, sql_params: dict = SQLSERVER_PARAMS):
        self.default = SQLServer(sql_params)

    @property
    def columns(self):
        return COLUNAS

    @property
    def query(self):
        raise NotImplementedError("Subclasses devem implementar a propriedade 'query'")

    def extraction(self):
        return pd.read_sql_query(self.query, self.connect(), dtype="category")

# %% ../../nbs/01c_sitarweb.ipynb 11
class Radcom(Sitarweb):
    def __init__(self, sql_params: dict = SQLSERVER_PARAMS):
        super().__init__(sql_params)

    @property
    def query(self):
        return SQL_RADCOM

    @property
    def stem(self):
        return "radcom"

    def _format(
        self,
        df: pd.DataFrame,  # DataFrame com o resultantes do banco de dados
    ) -> pd.DataFrame:  # DataFrame formatado
        """Formata, limpa e padroniza os dados provenientes da query no banco"""
        df["Entidade"] = df["Entidade"].str.strip()
        df["Num_Serviço"] = "231"
        df["Classe_Emissão"] = pd.NA
        df["Largura_Emissão(kHz)"] = "256"
        df["Validade_RF"] = pd.NA
        df["Status"] = "RADCOM"
        df["Fonte"] = "SRD"
        df["Multiplicidade"] = "1"
        a = df.Situação.isna()
        df.loc[a, "Classe"] = df.loc[a, "Fase"].astype("string")
        df.loc[~a, "Classe"] = (
            df.loc[~a, "Fase"].astype("string")
            + "-"
            + df.loc[~a, "Situação"].astype("string")
        )
        df.drop(["Fase", "Situação"], axis=1, inplace=True)
        df["Log"] = ""
        df["Frequência"] = pd.to_numeric(df["Frequência"], errors="coerce").astype(
            "float"
        )
        discarded = df[df.Frequência.isna()].copy()
        if not discarded.empty:
            log = """[("Colunas", "Frequência"),  
            ("Processamento", "Valor Nulo")]"""
            self.append2discarded(self.register_log(discarded, log))
        df.dropna(subset=["Frequência"], inplace=True)
        return df.loc[:, self.columns]

# %% ../../nbs/01c_sitarweb.ipynb 13
class Stel(Sitarweb):
    def __init__(self, sql_params: dict = SQLSERVER_PARAMS):
        super().__init__(sql_params)

    @property
    def query(self):
        return SQL_STEL

    @property
    def stem(self):
        return "stel"

    def _format(
        self,
        df: pd.DataFrame,  # DataFrame com o resultantes do banco de dados
    ) -> pd.DataFrame:  # DataFrame formatado
        """Formata, limpa e padroniza os dados provenientes da query no banco"""
        df["Status"] = "L"
        df["Entidade"] = df.Entidade.str.strip()
        df["Fonte"] = "STEL"
        df["Largura_Emissão"] = df["Largura_Emissão"].astype("string")
        df.loc[:, ["Largura_Emissão(kHz)", "_"]] = (
            df.Largura_Emissão.fillna("").apply(self.parse_bw).tolist()
        )
        df.drop(["Largura_Emissão", "_"], axis=1, inplace=True)
        df.loc[:, "Validade_RF"] = df.Validade_RF.astype("string").str.slice(0, 10)
        df["Frequência"] = df["Frequência"].astype("float")
        df.loc[df.Unidade == "kHz", "Frequência"] = df.loc[
            df.Unidade == "kHz", "Frequência"
        ].apply(lambda x: float(Decimal(x) / Decimal(1000)))
        df.loc[df.Unidade == "GHz", "Frequência"] = df.loc[
            df.Unidade == "GHz", "Frequência"
        ].apply(lambda x: float(Decimal(x) * Decimal(1000)))
        df.drop("Unidade", axis=1, inplace=True)
        df["Multiplicidade"] = 1
        df["Log"] = ""
        return df.loc[:, self.columns]
