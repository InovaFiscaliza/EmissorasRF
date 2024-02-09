import os
import urllib.request

from zipfile import ZipFile

from dotenv import load_dotenv, find_dotenv

from fastcore.xtras import Path
import pandas as pd
import geopandas as gpd


from extracao.constants import IBGE_MUNICIPIOS, IBGE_POLIGONO, MALHA_IBGE


# Load environment variables from .env file
load_dotenv(find_dotenv(), override=True)


class Geography:
	def __init__(self, df: pd.DataFrame):
		self.ibge = Path(IBGE_MUNICIPIOS)
		self.shapefile = Path(IBGE_POLIGONO)
		self.check_files()
		self.df = df
		self.missing = self.get_missing_info()

	def check_files(self):
		assert self.ibge.is_file(), 'File not found: ' + IBGE_MUNICIPIOS
		self.shapefile.parent.mkdir(exist_ok=True, parents=True)
		self.verify_shapefile_folder()

	def verify_shapefile_folder(self):
		"""It checks the existence and integrity of the all shapefiles from IBGE
		If any of the checks fails, it downloads, extracts and replaces the local files
		"""

		parent_folder = self.shapefile.parent
		zip_file_path = parent_folder.with_suffix('.zip')

		# Check if all required files exist
		required_files = L('.cpg', '.dbf', '.prj', '.shx').map(self.shapefile.with_suffix)
		if not all(required_files.map(Path.is_file)):
			# shutil.rmtree(str(shapefile_path.parent), ignore_errors=True)
			parent_folder.ls().map(Path.unlink)
			# Download and unzip the zipped folder
			urllib.request.urlretrieve(MALHA_IBGE, zip_file_path)
			with ZipFile(zip_file_path, 'r') as zip_ref:
				zip_ref.extractall(parent_folder)
			zip_file_path.unlink()

	def merge_df_with_ibge(
		self,
		df: pd.DataFrame,  # Input dataframe
	):  # DataFrame merged with the IBGE file
		"""Valida as coordenadas consultado a Base Corporativa do IBGE, excluindo o que já está no cache na versão anterior"""

		municipios = pd.read_csv(
			self.ibge,
			usecols=['Código_Município', 'Município', 'UF', 'Latitude', 'Longitude'],
			dtype='string',
			dtype_backend='numpy_nullable',
		)

		df['Código_Município'] = df['Código_Município'].astype('string')

		df = pd.merge(
			df,
			municipios,
			on='Código_Município',
			how='left',
			copy=False,
		)

		df.rename(
			columns={
				'Latitude_x': 'Latitude',
				'Longitude_x': 'Longitude',
				'Município_x': 'Município',
				'UF_x': 'UF',
				'Latitude_y': 'Latitude_IBGE',
				'Longitude_y': 'Longitude_IBGE',
				'Município_y': 'Município_IBGE',
				'UF_y': 'UF_IBGE',
			},
			inplace=True,
		)

		return df

	def get_missing_info(self):
		"""Check the coordinates and city code availability"""
		empty_coords = self.df.Latitude.isna() | self.df.Longitude.isna()
		empty_code = self.df.Código_Município.isna()
		both = empty_coords & empty_code
		left = empty_coords & (~empty_code)
		right = (~empty_coords) & empty_code
		return {'empty_coords': left, 'empty_code': right, 'both': both}

	def fill_missing_coords(self):
		rows = self.missing['empty_coords']
		self.df.loc[rows, ['Latitude', 'Longitude']] = self.df.loc[
			rows, ['Latitude_IBGE', 'Longitude_IBGE']
		]

	def intersect_coordinates_on_poligon(self):
		for column in ['Latitude', 'Longitude']:
			self.df[column] = pd.to_numeric(self.df[column], errors='coerce').astype('float')

		regions = gpd.read_file(self.shapefile)

		# Convert pandas dataframe to geopandas df with geometry point given coordinates
		gdf_points = gpd.GeoDataFrame(
			self.df, geometry=gpd.points_from_xy(self.df.Longitude, self.df.Latitude)
		)

		# Set the same coordinate reference system (CRS) as the regions shapefile
		gdf_points.crs = regions.crs

		# Spatial join points to the regions
		gdf = gpd.sjoin(gdf_points, regions, how='inner', predicate='within')

		gdf['CD_MUN'] = gdf.CD_MUN.astype('string')

		gdf.drop(
			[
				'geometry',
				'AREA_KM2',
				'index_right',
			],
			axis=1,
			inplace=True,
		)

		return gdf

	def validate(self):
		self.df = self.merge_df_with_ibge(self.df)
		self.fill_missing_coords()
		self.fill_missing_code()
