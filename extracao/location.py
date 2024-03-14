from typing import Dict

from functools import cached_property
import urllib.request

from zipfile import ZipFile

from dotenv import load_dotenv, find_dotenv

from fastcore.xtras import Path
from fastcore.foundation import L
import pandas as pd
import geopandas as gpd
from tqdm.auto import tqdm

tqdm.pandas()


from extracao.constants import IBGE_MUNICIPIOS, IBGE_POLIGONO, MALHA_IBGE
from extracao.datasources.base import Base


# Load environment variables from .env file
load_dotenv(find_dotenv(), override=True)
pd.options.mode.copy_on_write = True


class Geography:
	def __init__(self, df: pd.DataFrame):
		self.ibge: Path = Path(IBGE_MUNICIPIOS)
		self.shapefile: Path = Path(IBGE_POLIGONO)
		self.check_files()
		self.df: pd.DataFrame = df

	def check_files(self):
		"""Check if the `municipios.csv` file from IBGE exists
		It also calls the `verify_shapefile_folder` method
		"""
		assert self.ibge.is_file(), f'File not found: {IBGE_MUNICIPIOS}'
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

	def replace_bad_city_codes(self, df: pd.DataFrame) -> pd.DataFrame:
		"""Tries to fix the wrong city codes by looking at the normalized city names"""
		import re
		import unicodedata

		def remove_punctuation(word):
			# Unicode normalize transforma um caracter em seu equivalente em latin.
			nfkd = unicodedata.normalize('NFKD', word.lower())
			decoded_word = ''.join(c for c in nfkd if not unicodedata.combining(c))

			return re.sub(r'[^a-zA-Z0-9 ]', '', decoded_word)

		municipios = pd.read_csv(
			self.ibge,
			usecols=['Código_Município', 'Município', 'UF'],
			dtype='string',
			dtype_backend='numpy_nullable',
		)

		municipios['Município_ASCII'] = municipios['Município'].apply(remove_punctuation)

		bad_codes = ~self.log['empty_code']
		bad_codes &= ~df['Código_Município'].isin(municipios['Código_Município'])
		self.log.update({'invalid_code': bad_codes})

		df['Município'] = df['Município'].astype('string', copy=False)

		df.loc[bad_codes, 'Município'] = df.loc[bad_codes, 'Município'].fillna('')

		df.loc[bad_codes, 'Município_ASCII'] = df.loc[bad_codes, 'Município'].apply(
			remove_punctuation
		)

		df = pd.merge(
			df,
			municipios,
			on='Município_ASCII',
			how='left',
			copy=False,
		)

		processing = 'Código do Município inválido mesmo após limpeza.'
		processing += '\nMunicípio normalizado e usado como chave para cruzamento com o IBGE.'
		processing += '\nColuna {} substituída conforme consta no IBGE'
		# TODO: Verify if there isn't a wrong Município match, given Município is not unique
		for column in ['Município', 'Código_Município', 'UF']:
			df[f'#{column}'] = df[f'{column}_y'].fillna('')
			Base.register_log(df, processing.format(column).strip(), f'#{column}', bad_codes)
			df.loc[bad_codes, f'{column}_x'] = df.loc[bad_codes, f'{column}_y']
			df.drop(f'#{column}', inplace=True, axis=1)

		df.drop(
			columns=['Município_y', 'Município_ASCII', 'Código_Município_y', 'UF_y'],
			inplace=True,
		)

		df.rename(
			columns={
				'Município_x': 'Município',
				'UF_x': 'UF',
				'Código_Município_x': 'Código_Município',
			},
			inplace=True,
		)

		df[['Município', 'Código_Município', 'UF']] = df[
			['Município', 'Código_Município', 'UF']
		].astype('string', copy=False)

		return df

	def merge_df_with_ibge(
		self,
		df: pd.DataFrame,  # Input dataframe
	) -> pd.DataFrame:  # DataFrame merged with the IBGE file
		"""It merges the instance df with the IBGE dfs based on `Código_Município`
		The additional columns are: `Latitude_IBGE`, `Longitude_IBGE`, `Município_IBGE`, `UF_IBGE`
		"""

		df['Código_Município'] = df['Código_Município'].astype('string', copy=False).str.strip()
		df['#Código_Município'] = df['Código_Município'].fillna('')
		df['Código_Município'] = pd.to_numeric(
			df['Código_Município'], errors='coerce', downcast='unsigned'
		)
		row_filter = df['Código_Município'].isna()
		processing = 'Código_Município nulo ou inválido.'
		column = '#Código_Município'
		Base.register_log(df, processing, column, row_filter)
		df['Código_Município'] = df['Código_Município'].astype('string', copy=False)

		df = self.replace_bad_city_codes(df)

		municipios = pd.read_csv(
			self.ibge,
			usecols=['Código_Município', 'Município', 'Latitude', 'Longitude', 'UF'],
			dtype='string',
			dtype_backend='numpy_nullable',
		)

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
				'UF_y': 'UF_IBGE',
				'Latitude_y': 'Latitude_IBGE',
				'Longitude_y': 'Longitude_IBGE',
				'Município_y': 'Município_IBGE',
			},
			inplace=True,
		)

		return df.astype('string', copy=False)

	@cached_property
	def log(self) -> Dict[str, pd.Series]:
		"""Check the coordinates and city code availability"""
		empty_coords = self.df.Latitude.isna() | self.df.Longitude.isna()
		empty_code = self.df.Código_Município.isna()
		both = empty_coords & empty_code
		left = empty_coords & (~empty_code)
		right = (~empty_coords) & empty_code
		return {'empty_coords': left, 'empty_code': right, 'both': both}

	def fill_missing_coords(self) -> None:
		"""Fill the missing coordinates with the central coordinates of the city from IBGE"""
		rows = self.log['empty_coords']
		rows &= self.log['city_normalized']
		self.log.update({'filled_city_coords': rows})
		self.df.loc[rows, 'Latitude'] = self.df.loc[rows, 'Latitude_IBGE']
		self.df.loc[rows, 'Longitude'] = self.df.loc[rows, 'Longitude_IBGE']
		self.df['#Latitude'] = self.df['Latitude'].astype('string', copy=False).fillna('')
		self.df['#Longitude'] = self.df['Longitude'].astype('string', copy=False).fillna('')
		for column in ('Latitude', 'Longitude'):
			log = f'{column} do Município inserida.'
			Base.register_log(self.df, log, column, rows)
		self.df.drop(columns=['#Latitude', '#Longitude'], inplace=True)

	def normalize_location_names(self) -> None:
		rows = self.df['Latitude_IBGE'].notna()
		rows &= self.df['Longitude_IBGE'].notna()
		self.log.update({'city_normalized': rows})
		self.df['#Município'] = self.df['Município'].fillna('')
		self.df['#UF'] = self.df['UF'].fillna('')
		self.df.loc[rows, 'Município'] = self.df.loc[rows, 'Município_IBGE']
		self.df.loc[rows, 'UF'] = self.df.loc[rows, 'UF_IBGE']
		for column in ('#Município', '#UF'):
			log = f'Coluna {column.replace("#", "")} normalizada como consta no IBGE.'
			Base.register_log(self.df, log, column, rows)
		self.df.drop(columns=['#Município', '#UF'], inplace=True)

	def drop_rows_without_location_info(self) -> None:
		rows = self.log['both']
		processing = 'Coordenadas e Código do Município nulos'
		Base.register_log(self.df, processing, row_filter=rows)
		self.df = self.df[~rows].reset_index(drop=True)

	def validate_coordinates(self) -> None:
		"""Check if the coordinates are actually valid float numbers."""
		invalid_lats = pd.to_numeric(self.df['Latitude'], errors='coerce')  # type: ignore
		invalid_longs = pd.to_numeric(self.df['Longitude'], errors='coerce')  # type: ignore
		invalid = invalid_lats.isna() | invalid_longs.isna()
		self.log.update({'invalid_coords': invalid})
		# TODO: Log original invalid values

	def intersect_coordinates_on_poligon(self):
		"""Intersect the coordinates with the shapefile of the IBGE
		Returns a geopandas dataframe with additional columns `CD_MUN, NM_MUN, SIGLA_UF`
		"""
		self.df['Latitude'] = self.df['Latitude'].astype('string', copy=False).str.strip()
		self.df['Longitude'] = self.df['Longitude'].astype('string', copy=False).str.strip()
		self.df['#Longitude'] = self.df['Longitude'].astype('string', copy=False).fillna('')
		for column in ['Latitude', 'Longitude']:
			self.df[f'#{column}'] = self.df[column].astype('string', copy=False).fillna('')
			self.df[column] = pd.to_numeric(self.df[column], errors='coerce').astype(
				'float', copy=False
			)  # type: ignore
			bad_coords = self.df[column].isna() & self.df[f'#{column}'].notna()
			Base.register_log(self.df, f'Coluna {column} não numérica.', f'#{column}', bad_coords)
			self.df.drop(columns=[f'#{column}'], inplace=True)

		regions = gpd.read_file(self.shapefile)

		# Convert pandas dataframe to geopandas df with geometry point given coordinates
		gdf_points = gpd.GeoDataFrame(
			self.df, geometry=gpd.points_from_xy(self.df.Longitude, self.df.Latitude)
		)  # type: ignore

		# Set the same coordinate reference system (CRS) as the regions shapefile
		gdf_points.crs = regions.crs

		# Spatial join points to the regions
		gdf_joined = gpd.sjoin(gdf_points, regions, how='left', predicate='within')

		gdf_joined['CD_MUN'] = gdf_joined.CD_MUN.astype('string', copy=False)
		gdf_joined['LAT'] = gdf_joined.geometry.centroid.y.astype('string', copy=False)
		gdf_joined['LON'] = gdf_joined.geometry.centroid.x.astype('string', copy=False)

		gdf_joined.drop(
			[
				'geometry',
				'AREA_KM2',
				'index_right',
			],
			axis=1,
			inplace=True,
		)

		self.df = gdf_joined

	def fill_missing_city_info(self):
		"""Fill the missing city code
		The missing ones are replaces with the city code derived from the intersection with the shapefile from IBGE"""
		rows = self.log['empty_code']
		rows &= self.df['CD_MUN'].notna()
		self.log.update({'filled_city_info': rows})
		self.df.loc[rows, 'Código_Município'] = self.df.loc[rows, 'CD_MUN']
		self.df.loc[rows, 'Município'] = self.df.loc[rows, 'NM_MUN']
		self.df.loc[rows, 'UF'] = self.df.loc[rows, 'SIGLA_UF']

	def substitute_wrong_city_info(self):
		"""Replace city info for invalid city codes
		They are replaced with the city code derived from the intersection with the shapefile from IBGE"""
		rows = ~self.log['empty_code']
		rows &= self.df['Município_IBGE'].isna()
		rows &= self.df['CD_MUN'].notna()
		self.log.update({'replaced_city_info': rows})
		self.df.loc[rows, 'Código_Município'] = self.df.loc[rows, 'CD_MUN']
		self.df.loc[rows, 'Município'] = self.df.loc[rows, 'NM_MUN']
		self.df.loc[rows, 'UF'] = self.df.loc[rows, 'SIGLA_UF']

	def substitute_divergent_coordinates(self):
		"""Substitute the coordinates with the centroid from the IBGE `municipios.csv`
		After the intersection of the coordinates with the shapefile, the city code from the data
		should match the one returned from the shapefile.
		If it doesn't the original coordinates are replaced by the ones representing the centroid of the original city code
		"""
		# TODO: keep track of "unchanged divergent coordinates, i.e. with IBGE coords null"
		wrong_city_coords = self.df['Código_Município'].notna()
		wrong_city_coords &= self.df['CD_MUN'].notna()
		wrong_city_coords &= self.df['Código_Município'] != self.df['CD_MUN']
		wrong_city_coords &= self.log['city_normalized']
		self.log.update({'wrong_city_coords': wrong_city_coords})
		self.df.loc[wrong_city_coords, 'Latitude'] = self.df.loc[wrong_city_coords, 'Latitude_IBGE']
		self.df.loc[wrong_city_coords, 'Longitude'] = self.df.loc[
			wrong_city_coords, 'Longitude_IBGE'
		]

	def input_info_from_coords(self):
		from geopy.geocoders import Nominatim

		rows = self.df['Código_Município'].isna()
		geolocator = Nominatim(user_agent='rfdatahub')
		pbar = tqdm(self.df[rows].itertuples(), total=len(self.df[rows]))
		pbar.set_description('Utilizando API geocoders.Local fora do perímetro brasileiro.')
		for row in pbar:
			location = geolocator.reverse(
				f'{row.Latitude}, {row.Longitude}', exactly_one=True, language='pt'
			)
			if location is None:
				continue
			address = location.raw['address']
			city = address.get('city', '')
			state = address.get('state', '')
			country = address.get('country', '')
			if any([city, state, country]):
				self.df.loc[row.Index, 'Município'] = city
				self.df.loc[row.Index, 'UF'] = (
					f'{state}-{country}' if country != 'Brasil' else state
				)

		self.log.update({'city_state_country': rows})

	def validate(self) -> pd.DataFrame:
		"""Helper function to load the IBGE data, enrich and and validate the location information"""
		self.drop_rows_without_location_info()
		self.df = self.merge_df_with_ibge(self.df)
		self.normalize_location_names()
		self.fill_missing_coords()
		self.intersect_coordinates_on_poligon()
		self.fill_missing_city_info()
		self.substitute_wrong_city_info()
		self.substitute_divergent_coordinates()
		self.input_info_from_coords()
		return self.df.astype('string', copy=False)
