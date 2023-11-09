# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03a_anatel.ipynb.

# %% auto 0
__all__ = ['Outorgadas']

# %% ../nbs/03a_anatel.ipynb 3
import shutil
import urllib.request
from functools import cached_property
from typing import List
from zipfile import ZipFile

import geopandas as gpd
import pandas as pd
from dotenv import find_dotenv, load_dotenv
from fastcore.foundation import L
from fastcore.parallel import parallel
from fastcore.xtras import Path

from .constants import COLUNAS, IBGE_MUNICIPIOS, IBGE_POLIGONO, MALHA_IBGE
from .datasources.aeronautica import Aero
from .datasources.base import Base
from .datasources.mosaico import MONGO_URI
from .datasources.sitarweb import SQLSERVER_PARAMS, Radcom, Stel
from .datasources.smp import SMP
from .datasources.srd import SRD
from .datasources.telecom import Telecom

# %% ../nbs/03a_anatel.ipynb 4
load_dotenv(find_dotenv())


# %% ../nbs/03a_anatel.ipynb 6
class Outorgadas(Base):
	"""Classe auxiliar para agregar os dados originários da Anatel"""

	def __init__(
		self,
		sql_params: dict = SQLSERVER_PARAMS,
		mongo_uri: str = MONGO_URI,
		limit: int = 0,
	):
		self.sql_params = sql_params
		self.mongo_uri = mongo_uri
		self.limit = limit

	@property
	def columns(self):
		return COLUNAS

	@cached_property
	def df_cache(self) -> pd.DataFrame:
		try:
			df = self._read(self.stem)
		except ValueError:
			df = pd.DataFrame(columns=self.columns)
		return df

	@property
	def stem(self):
		return 'anatel'

	@staticmethod
	def _update_instance(class_instance):
		class_instance.update()
		class_instance.save()
		return class_instance.df

	@cached_property
	def extraction(self) -> L:
		sources = [
			Aero(),
			Stel(self.sql_params),
			Radcom(self.sql_params),
			SRD(self.mongo_uri),
			Telecom(self.mongo_uri, self.limit),
			SMP(self.mongo_uri, self.limit),
		]

		return parallel(Outorgadas._update_instance, sources, n_workers=len(sources), progress=True)

	@staticmethod
	def verify_shapefile_folder():
		# Convert the file paths to Path objects
		shapefile_path = Path(IBGE_POLIGONO)
		zip_file_path = shapefile_path.parent.with_suffix('.zip')

		# Check if all required files exist
		required_files = L('.cpg', '.dbf', '.prj', '.shx').map(shapefile_path.with_suffix)
		if not all(required_files.map(Path.is_file)):
			shutil.rmtree(str(shapefile_path.parent), ignore_errors=True)
			# Download and unzip the zipped folder
			urllib.request.urlretrieve(MALHA_IBGE, zip_file_path)
			with ZipFile(zip_file_path, 'r') as zip_ref:
				zip_ref.extractall(shapefile_path.parent.parent)
			zip_file_path.unlink()

	def fill_nan_coordinates(
		self,
		df: pd.DataFrame,  # DataFrame com os dados da Anatel
	) -> pd.DataFrame:  # DataFrame com as coordenadas validadas na base do IBGE
		"""Valida as coordenadas consultado a Base Corporativa do IBGE, excluindo o que já está no cache na versão anterior"""

		municipios = pd.read_csv(
			IBGE_MUNICIPIOS,
			usecols=['Código_Município', 'Latitude', 'Longitude'],
			dtype='string[pyarrow]',
			dtype_backend='pyarrow',
		)

		df = pd.merge(df, municipios, on='Código_Município', how='left', copy=False)

		null_coords = df.Latitude_x.isna() | df.Longitude_x.isna()

		df.loc[null_coords, ['Latitude_x', 'Longitude_x']] = df.loc[
			null_coords, ['Latitude_y', 'Longitude_y']
		]

		log = """[("Colunas", ["Latitude", "Longitude"]),
		           ("Processamento", "Coordenadas Ausentes. Inserido coordenadas do Município")]"""
		df = self.register_log(df, log, null_coords)

		df.rename(
			columns={
				'Latitude_x': 'Latitude',
				'Longitude_x': 'Longitude',
				'Latitude_y': 'Latitude_ibge',
				'Longitude_y': 'Longitude_ibge',
			},
			inplace=True,
		)

		return df

	def intersect_coordinates_on_poligon(self, df: pd.DataFrame, check_municipio: bool = True):
		regions = gpd.read_file(IBGE_POLIGONO)
		# Convert pandas dataframe to geopandas df with geometry point given coordinates
		gdf_points = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))

		# Set the same coordinate reference system (CRS) as the regions shapefile
		gdf_points.crs = regions.crs

		# Spatial join points to the regions
		points_with_regions = gpd.sjoin(gdf_points, regions, how='inner', predicate='within')

		if check_municipio:
			# Check correctness of Coordinates
			check_coords = points_with_regions.Código_Município != points_with_regions.CD_MUN

			log = """[("Colunas", ["Código_Município", "Município", "UF"]),
					("Processamento", "Informações substituídas  pela localização correta das coordenadas.")		      
				"""
			self.register_log(points_with_regions, log, check_coords)

			points_with_regions.drop(['Código_Município', 'Município', 'UF'], axis=1, inplace=True)

		points_with_regions.rename(
			columns={
				'CD_MUN': 'Código_Município',
				'NM_MUN': 'Município',
				'SIGLA_UF': 'UF',
			},
			inplace=True,
		)

		return points_with_regions

	def validate_coordinates(self, df: pd.DataFrame, check_municipio: bool = True) -> pd.DataFrame:
		"""
		Validates the coordinates in the given DataFrame.

		Args:
		        df: The DataFrame containing the coordinates to be validated.
		        check_municipio: A boolean indicating whether to check the municipality information (default: True).

		Returns:
		        pd.DataFrame: The DataFrame with validated coordinates.

		Raises:
		        None
		"""
		self.verify_shapefile_folder()
		if check_municipio:
			df = self.fill_nan_coordinates(df)
		return self.intersect_coordinates_on_poligon(df, check_municipio)

	def _format(
		self,
		dfs: List,  # List with the individual API sources
	) -> pd.DataFrame:  # Processed DataFrame
		aero = self.validate_coordinates(dfs.pop(0), False)
		anatel = self.validate_coordinates(pd.concat(dfs, ignore_index=True))
		return pd.concat([aero, anatel], ignore_index=True).sort_values(
			['Frequência', 'Latitude', 'Longitude'], ignore_index=True
		)
