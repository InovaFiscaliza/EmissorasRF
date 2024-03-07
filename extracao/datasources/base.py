# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01b_base.ipynb.

# %% auto 0
__all__ = ['Base']

# %% ../../nbs/01b_base.ipynb 3
import json
import re
from dataclasses import dataclass
from functools import cached_property, partial
from typing import Tuple, Union, List, Any

import pandas as pd
from dotenv import find_dotenv, load_dotenv
from fastcore.xtras import Path, listify
from pyarrow import ArrowInvalid, ArrowTypeError
from tqdm.auto import tqdm

from ..constants import BW, RE_BW

# %% ../../nbs/01b_base.ipynb 4
load_dotenv(find_dotenv(), override=True)
tqdm.pandas()
pd.options.mode.copy_on_write = True


# %% ../../nbs/01b_base.ipynb 6
@dataclass
class Base:
	folder: Union[str, Path] = Path(__file__).parent / 'arquivos' / 'saida'
	read_cache: bool = False

	def _read(self, stem: str, backend: str = 'pyarrow') -> pd.DataFrame:
		"""Lê o dataframe formado por self.folder / self.stem.parquet.gzip"""
		file = Path(f'{self.folder}/{stem}.parquet.gzip')
		try:
			df = pd.read_parquet(file, dtype_backend=backend)
		except (ArrowInvalid, FileNotFoundError) as e:
			raise ValueError(f'Error when reading {file}') from e
		return df

	def _save(self, df: pd.DataFrame, folder: Union[str, Path], stem: str) -> pd.DataFrame:
		"""Format, Save and return a dataframe"""
		try:
			file = Path(f'{folder}/{stem}.parquet.gzip')
			df.astype('string').to_parquet(file, compression='gzip', index=False, engine='pyarrow')
		except (ArrowInvalid, ArrowTypeError) as e:
			raise Exception(f'Não foi possível salvar o arquivo parquet') from e
		return df

	@cached_property
	def df(self) -> pd.DataFrame:
		try:
			return self._read(self.stem)
		except (ArrowInvalid, FileNotFoundError) as e:
			raise ValueError(f'Não foi possível ler o arquivo parquet {self.stem}') from e

	@staticmethod
	def parse_bw(
		bw: str,  # Designação de Emissão (Largura + Classe) codificada como string
	) -> Tuple[Union[str, Any], Union[str, Any]]:  # Largura e Classe de Emissão
		"""Parse the bandwidth string"""
		if match := re.match(RE_BW, bw):
			multiplier = BW[match[2]]
			if mantissa := match[3]:
				number = float(f'{match[1]}.{mantissa}')
			else:
				number = float(match[1])
			classe = match[4]
			return str(multiplier * number), str(classe)
		return pd.NA, pd.NA

	@cached_property
	def discarded(self) -> pd.DataFrame:
		return pd.DataFrame(columns=self.columns)

	def append2discarded(self, df: pd.DataFrame) -> None:
		"""Receives one of more dataframes and append to the discarded dataframe"""
		if not self.discarded.empty:
			self.discarded = pd.concat([self.discarded, df], ignore_index=True, copy=False)
		else:
			self.discarded = df

	@staticmethod
	def register_log(
		df: pd.DataFrame,
		processing: str,
		column: Union[str, None] = None,
		row_filter: Union[pd.Series, None] = None,
	):
		"""Register a log in the dataframe"""
		if row_filter is None:
			row_filter = pd.Series(True, index=df.index)

		df['Log'] = df['Log'].astype('string', copy=False).fillna('[]')
		df['Log'] = df['Log'].str.replace('^$', r'[]', regex=True)
		log_function = partial(Base.format_log, processing=processing, column=column)
		print(f'Logging: {processing}')
		df.loc[row_filter, 'Log'] = df[row_filter].progress_apply(log_function, axis=1)

	@staticmethod
	def format_log(
		row: pd.Series,
		processing: str,
		column: Union[str, None] = None,
	) -> str:
		"""Translate log string into dict, update it and reformats it a log message
		It's assumed the typing in the signature is correct
		"""
		log = listify(json.loads(row.loc['Log']))
		new_log = {'Processamento': processing}
		if column is not None:
			new_log.update({'Coluna': column, 'Original': row.loc[column]})
		log.append(new_log)
		return json.dumps(log, ensure_ascii=False)

	@property
	def columns(self):
		raise NotImplementedError("Subclasses devem implementar a propriedade 'columns'")

	@property
	def cols_mapping(self):
		raise NotImplementedError("Subclasses devem implementar a propriedade 'cols_mapping'")

	@property
	def stem(self):
		raise NotImplementedError('Subclasses devem setar a propriedade stem!')

	def extraction(self) -> pd.DataFrame:
		raise NotImplementedError('Subclasses devem implementar o método extract')

	def _format(
		self,
		df: pd.DataFrame,  # DataFrame com os dados de Estações
	) -> pd.DataFrame:  # DataFrame formatado
		"""Formata, limpa e padroniza os dados provenientes da query no banco"""
		raise NotImplementedError('Subclasses devem implementar o método _format')

	def update(self):
		df = self.extraction()
		if not self.read_cache:
			self._save(df.drop('Log', axis=1), self.folder, f'{self.stem}_raw')
		self.df = self._format(df)

	def save(self, folder: Union[str, Path, None] = None):
		if folder is None:
			folder = self.folder
		self._save(self.df, folder, self.stem)
		self._save(self.discarded, folder, f'{self.stem}_discarded')
