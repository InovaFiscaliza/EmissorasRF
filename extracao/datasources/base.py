# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01b_base.ipynb.

# %% auto 0
__all__ = ['Base']

# %% ../../nbs/01b_base.ipynb 3
import re
from dataclasses import dataclass
from functools import cached_property
from typing import Tuple, Union, List

import pandas as pd
from dotenv import find_dotenv, load_dotenv
from fastcore.xtras import Path, listify
from pyarrow import ArrowInvalid, ArrowTypeError

from ..constants import BW, RE_BW

# %% ../../nbs/01b_base.ipynb 4
load_dotenv(find_dotenv(), override=True)

# %% ../../nbs/01b_base.ipynb 6
@dataclass
class Base:
    folder: Union[str, Path] = Path(__file__).parent / "arquivos" / "saida"

    def _read(self, stem: str) -> pd.DataFrame:
        """Lê o dataframe formado por self.folder / self.stem.parquet.gzip"""
        file = Path(f"{self.folder}/{stem}.parquet.gzip")
        try:
            df = pd.read_parquet(file, dtype_backend="pyarrow")
        except (ArrowInvalid, FileNotFoundError) as e:
            raise ValueError(f"Error when reading {file}") from e
        return df

    def _save(
        self, df: pd.DataFrame, folder: Union[str, Path], stem: str
    ) -> pd.DataFrame:
        """Format, Save and return a dataframe"""
        try:
            file = Path(f"{folder}/{stem}.parquet.gzip")
            df.to_parquet(file, compression="gzip", index=False, engine="pyarrow")
        except (ArrowInvalid, ArrowTypeError) as e:
            raise e(f"Não foi possível salvar o arquivo parquet {file}") from e
        return df

    def df(self) -> pd.DataFrame:
        try:
            df = self._read(self.stem)
        except (ArrowInvalid, FileNotFoundError):
            df = self._format(self.extraction())
        return df

    @staticmethod
    def parse_bw(
        bw: str,  # Designação de Emissão (Largura + Classe) codificada como string
    ) -> Tuple[str, str]:  # Largura e Classe de Emissão
        """Parse the bandwidth string"""
        if match := re.match(RE_BW, bw):
            multiplier = BW[match[2]]
            if mantissa := match[3]:
                number = float(f"{match[1]}.{mantissa}")
            else:
                number = float(match[1])
            classe = match[4]
            return str(multiplier * number), str(classe)
        return pd.NA, pd.NA

    @cached_property
    def discarded(self) -> pd.DataFrame:
        return pd.DataFrame(columns=self.columns)

    def append2discarded(self, dfs: Union[pd.DataFrame, List]) -> None:
        """Receives one of more dataframes and append to the discarded dataframe"""
        dfs = listify(dfs)
        if not self.discarded.empty:
            dfs.append(self.discarded)
        self.discarded = pd.concat(dfs, ignore_index=True)

    @staticmethod
    def register_log(df: pd.DataFrame, log: str, row_filter: pd.Series = None):
        """Register a log in the dataframe"""
        if row_filter is None:
            row_filter = pd.Series(True, index=df.index)

        df["Log"] = df["Log"].astype("string").fillna("")

        df.loc[row_filter, "Log"] = df.loc[row_filter, "Log"].apply(
            lambda x: f"{x}|{log}" if x else log
        )
        df["Log"] = df.Log.str.replace(r"[\n\t]", "", regex=True)
        return df

    @property
    def columns(self):
        raise NotImplementedError(
            "Subclasses devem implementar a propriedade 'columns'"
        )

    @property
    def cols_mapping(self):
        raise NotImplementedError(
            "Subclasses devem implementar a propriedade 'cols_mapping'"
        )

    @property
    def stem(self):
        raise NotImplementedError("Subclasses devem setar a propriedade stem!")

    def extraction(self) -> pd.DataFrame:
        raise NotImplementedError("Subclasses devem implementar o método extract")

    def _format(
        self,
        df: pd.DataFrame,  # DataFrame com os dados de Estações
    ) -> pd.DataFrame:  # DataFrame formatado
        """Formata, limpa e padroniza os dados provenientes da query no banco"""
        raise NotImplementedError("Subclasses devem implementar o método _format")

    def update(self):
        self.df = self._format(self.extraction())

    def save(self, folder: Union[str, Path] = None):
        if folder is None:
            folder = self.folder
        self._save(self.df, folder, self.stem)
        self._save(self.discarded, folder, f"{self.stem}_discarded")
