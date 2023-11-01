# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01f_telecom.ipynb.

# %% auto 0
__all__ = ['MONGO_URI', 'Telecom']

# %% ../../nbs/01f_telecom.ipynb 3
import os
from functools import cached_property

import pandas as pd
from dotenv import find_dotenv, load_dotenv

from extracao.constants import (
    AGG_LICENCIAMENTO,
    COLS_LICENCIAMENTO,
    DICT_LICENCIAMENTO,
    MONGO_TELECOM,
    PROJECTION_LICENCIAMENTO,
)

from .mosaico import Mosaico

# %% ../../nbs/01f_telecom.ipynb 4
load_dotenv(find_dotenv())

# %% ../../nbs/01f_telecom.ipynb 6
MONGO_URI = os.environ.get("MONGO_URI")

# %% ../../nbs/01f_telecom.ipynb 7
class Telecom(Mosaico):
    """Extração e Processamento dos serviços de Telecomunições distintos de SMP"""

    def __init__(self, mongo_uri: str = MONGO_URI, limit: int = 0) -> None:
        super().__init__(mongo_uri)
        self.limit = limit

    @property
    def stem(self):
        return "telecom"

    @property
    def collection(self):
        return "licenciamento"

    @property
    def query(self):
        return MONGO_TELECOM

    @property
    def projection(self):
        return PROJECTION_LICENCIAMENTO

    @property
    def columns(self):
        return COLS_LICENCIAMENTO

    @property
    def cols_mapping(self):
        return DICT_LICENCIAMENTO

    @cached_property
    def extraction(self) -> pd.DataFrame:
        pipeline = [{"$match": self.query}, {"$project": self.projection}]
        if self.limit > 0:
            pipeline.append({"$limit": self.limit})
        df = self._extract(self.collection, pipeline)
        df["Log"] = "[]"
        # Substitui strings vazias e somente com espaços por nulo
        return df.replace(r"^\s*$", pd.NA, regex=True)

    def _format(
        self,
        df: pd.DataFrame,  # DataFrame com os dados de Estações e Plano_Básico mesclados
    ) -> pd.DataFrame:  # DataFrame com os dados mesclados e limpos
        """Clean the merged dataframe with the data from the MOSAICO page"""
        df = df.rename(columns=self.cols_mapping)
        df = self.split_designacao(df)
        duplicated = df.duplicated(subset=AGG_LICENCIAMENTO, keep="first")
        df_sub = df[~duplicated].reset_index(drop=True)
        discarded = df[duplicated].reset_index(drop=True)
        log = f"""[("Colunas", {AGG_LICENCIAMENTO}),  
        ("Processamento", "Registro agrupado e descartado do arquivo final")]"""
        discarded = self.register_log(discarded, log)
        df_sub["Multiplicidade"] = (
            df.groupby(AGG_LICENCIAMENTO, sort=False).size().tolist()
        )
        log = f'[("Colunas", {AGG_LICENCIAMENTO}), ("Processamento", "Agrupamento")]'
        df_sub = self.register_log(df_sub, log, df_sub.Multiplicidade > 1)
        df_sub["Status"] = "L"
        df_sub["Fonte"] = "MOSAICO"
        self.append2discarded([self.discarded, discarded])
        return df_sub.loc[:, self.columns]

# %% ../../nbs/01f_telecom.ipynb 8
if __name__ == "__main__":
    import time

    start = time.perf_counter()

    data = Telecom(limit=100000)

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
