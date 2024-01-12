# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01f_telecom.ipynb.

# %% auto 0
__all__ = ['MONGO_URI', 'Telecom']

# %% ../../nbs/01f_telecom.ipynb 3
import os

import pandas as pd
from dotenv import find_dotenv, load_dotenv

from extracao.constants import (
	AGG_LICENCIAMENTO,
	COLUNAS,
	DICT_LICENCIAMENTO,
	MONGO_TELECOM,
	PROJECTION_LICENCIAMENTO,
)

from .mosaico import Mosaico

# %% ../../nbs/01f_telecom.ipynb 4
load_dotenv(find_dotenv())

# %% ../../nbs/01f_telecom.ipynb 6
MONGO_URI = os.environ.get('MONGO_URI')


# %% ../../nbs/01f_telecom.ipynb 7
class Telecom(Mosaico):
	"""Extração e Processamento dos serviços de Telecomunições distintos de SMP"""

	def __init__(self, mongo_uri: str = MONGO_URI, limit: int = 0) -> None:
		super().__init__(mongo_uri)
		self.limit = limit

	@property
	def stem(self):
		return 'telecom'

	@property
	def collection(self):
		return 'licenciamento'

	@property
	def query(self):
		return MONGO_TELECOM

	@property
	def projection(self):
		return PROJECTION_LICENCIAMENTO

	@property
	def columns(self):
		return COLUNAS

	@property
	def cols_mapping(self):
		return DICT_LICENCIAMENTO

	def extraction(self) -> pd.DataFrame:
		pipeline = [{'$match': self.query}, {'$project': self.projection}]
		if self.limit > 0:
			pipeline.append({'$limit': self.limit})
		df = self._extract(self.collection, pipeline)
		df['Log'] = ''
		return df

	def _format(
		self,
		df: pd.DataFrame,  # DataFrame com os dados de Estações e Plano_Básico mesclados
	) -> pd.DataFrame:  # DataFrame com os dados mesclados e limpos
		"""Clean the merged dataframe with the data from the MOSAICO page"""
		df = df.rename(columns=self.cols_mapping)
		df = self.split_designacao(df)
		duplicated = df.duplicated(subset=AGG_LICENCIAMENTO, keep='first')
		df_sub = df[~duplicated].reset_index(drop=True)
		# discarded = df[duplicated].reset_index(drop=True)
		# log = f"""[("Colunas", {AGG_LICENCIAMENTO}),
		# ("Processamento", "Registro agrupado e descartado do arquivo final")]"""
		# self.append2discarded(self.register_log(discarded, log))
		# del discarded
		# gc.collect()
		# .count() drop the NaN from the subset, not keeping them
		df_sub.dropna(subset=AGG_LICENCIAMENTO, inplace=True)
		df_sub['Multiplicidade'] = (
			df.groupby(AGG_LICENCIAMENTO, dropna=True, sort=False, observed=True).size().values
		)
		log = f'[("Colunas", {AGG_LICENCIAMENTO}), ("Processamento", "Agrupamento")]'
		df_sub = self.register_log(df_sub, log, df_sub.Multiplicidade > 1)
		df_sub['Status'] = 'L'
		df_sub['Fonte'] = 'MOSAICO-LIC'
		return df_sub.loc[:, self.columns]
