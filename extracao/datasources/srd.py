# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01e_srd.ipynb.

# %% auto 0
__all__ = ['MONGO_URI', 'SRD']

# %% ../../nbs/01e_srd.ipynb 3
import os
from decimal import Decimal
from functools import cached_property

import pandas as pd
from dotenv import find_dotenv, load_dotenv

from extracao.constants import (
    BW_MAP,
    COLUNAS,
    DICT_SRD,
    MONGO_SRD,
    PROJECTION_SRD,
)

from .mosaico import Mosaico

# %% ../../nbs/01e_srd.ipynb 4
load_dotenv(find_dotenv())

# %% ../../nbs/01e_srd.ipynb 6
MONGO_URI = os.environ.get("MONGO_URI")

# %% ../../nbs/01e_srd.ipynb 7
class SRD(Mosaico):
    """Classe para encapsular a lógica de extração de Radiodifusão"""

    def __init__(self, mongo_uri: str = MONGO_URI) -> None:
        super().__init__(mongo_uri)

    @property
    def stem(self):
        return "srd"

    @property
    def collection(self):
        return "srd"

    @property
    def query(self):
        return MONGO_SRD

    @property
    def projection(self):
        return PROJECTION_SRD

    @property
    def columns(self):
        return COLUNAS

    @property
    def cols_mapping(self):
        return DICT_SRD

    @cached_property
    def extraction(self) -> pd.DataFrame:
        pipeline = [
            # match the documents that satisfy your query
            {"$match": self.query},
            # project the fields that you want to keep
            {"$project": self.projection},
        ]
        df = self._extract(self.collection, pipeline)
        df.loc[df["estacao"] == "[]", "estacao"] = "{}"
        cols = ["srd_planobasico", "estacao", "habilitacao", "Status"]
        for col in cols:
            df = df.join(pd.json_normalize(df[col].apply(eval)))
        df.drop(columns=cols, inplace=True)
        df["Log"] = ""
        return df

    def _format(
        self,
        df: pd.DataFrame,  # DataFrame com o resultantes do banco de dados
    ) -> pd.DataFrame:  # DataFrame formatado
        """Formata, limpa e padroniza os dados provenientes da query no banco"""

        df = df.rename(columns=self.cols_mapping)
        status = df.Status.str.contains("-C1$|-C2$|-C3$|-C4$|-C7|-C98$", na=False)
        # discarded = df[~status].copy()
        # log = """[("Registro", "Status"),
        #         ("Processamento", "Registro com Status não considerado para fins de monitoração")]"""
        # discarded = self.register_log(discarded, log)
        df = df[
            df.Status.str.contains("-C1$|-C2$|-C3$|-C4$|-C7|-C98$", na=False)
        ].reset_index(drop=True)
        df["Frequência"] = (
            df.Frequência.astype("string").str.replace(",", ".").astype("float")
        )
        # discarded_with_na = df[df.Frequência.isna()].copy()
        # log = """[("Registro", "Frequência"),
        #         ("Processamento", "Registro com valor nulo presente")]"""
        # discarded_with_na = self.register_log(discarded_with_na, log)
        df.dropna(subset="Frequência", ignore_index=True, inplace=True)  # type: ignore
        df.loc[df["Num_Serviço"] == "205", "Frequência"] = df.loc[
            df["Num_Serviço"] == "205", "Frequência"
        ].apply(lambda x: float(Decimal(x) / Decimal(1000)))
        df["Frequência"] = df["Frequência"].astype("float")
        df["Validade_RF"] = df.Validade_RF.astype("string").str.slice(0, 10)
        df["Fonte"] = "MOSAICO"
        df["Num_Serviço"] = df["Num_Serviço"].fillna("")
        df["Designação_Emissão"] = (
            df.Num_Serviço.astype("string").fillna("").map(BW_MAP)
        )
        df = self.split_designacao(df)
        df["Multiplicidade"] = 1
        # self.append2discarded([self.discarded, discarded, discarded_with_na])
        return df.loc[:, self.columns]

# %% ../../nbs/01e_srd.ipynb 8
if __name__ == "__main__":
    import time

    start = time.perf_counter()

    data = SRD()

    data.update()

    print("DATA")

    display(data.df)

    print(150 * "=")

    print("DISCARDED!")

    display(data.discarded[["Frequência", "Entidade", "Log"]])

    print(150 * "=")

    print(data.df.Multiplicidade.sum())

    data.save()

    print(f"Elapsed time: {time.perf_counter() - start} seconds")
