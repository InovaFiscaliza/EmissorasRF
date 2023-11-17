# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_estacoes.ipynb.

# %% auto 0
__all__ = ['Estacoes']

# %% ../nbs/04_estacoes.ipynb 3
import urllib.request
from typing import List
from zipfile import ZipFile

import geopandas as gpd
import pandas as pd
from dotenv import find_dotenv, load_dotenv
from fastcore.foundation import L
from fastcore.parallel import parallel
from fastcore.xtras import Path

from extracao.constants import (
    COLS_SRD,
    IBGE_MUNICIPIOS,
    IBGE_POLIGONO,
    MALHA_IBGE,
    FLOAT_COLUMNS,
    INT_COLUMNS,
    STR_COLUMNS,
    CAT_COLUMNS,
)
from .datasources.aeronautica import Aero
from .datasources.base import Base
from .datasources.mosaico import MONGO_URI
from .datasources.sitarweb import SQLSERVER_PARAMS, Radcom, Stel
from .datasources.smp import SMP
from .datasources.srd import SRD
from .datasources.telecom import Telecom
from .format import merge_on_frequency, LIMIT_FREQ

# %% ../nbs/04_estacoes.ipynb 4
load_dotenv(find_dotenv(), override=True)

# %% ../nbs/04_estacoes.ipynb 6
class Estacoes(Base):
    """Classe auxiliar para agregar os dados originários da Anatel"""

    def __init__(
        self,
        sql_params: dict = SQLSERVER_PARAMS,
        mongo_uri: str = MONGO_URI,
        limit: int = 0,
        parallel: bool = True,
    ):
        self.sql_params = sql_params
        self.mongo_uri = mongo_uri
        self.limit = limit
        self.parallel = parallel
        self.init_data_sources()

    @property
    def columns(self):
        return COLS_SRD

    def build_from_sources(self) -> pd.DataFrame:
        return self._format([s.df() for s in self.sources.values()])

    @property
    def stem(self):
        return "estacoes"

    @staticmethod
    def _update_source(class_instance):
        class_instance.update()
        class_instance.save()
        return class_instance

    def init_data_sources(self):
        self.sources = {
            "telecom": Telecom(self.mongo_uri, self.limit),
            "smp": SMP(self.mongo_uri, self.limit),
            "srd": SRD(self.mongo_uri, self.limit),
            # 'stel': Stel(self.sql_params),
            # 'radcom': Radcom(self.sql_params),
            "aero": Aero(),
        }

    def extraction(self) -> L:
        if self.parallel:
            sources = parallel(
                Estacoes._update_source,
                self.sources.values(),
                n_workers=len(self.sources),
                progress=True,
            )
        else:
            sources = L(self._update_source(s) for s in self.sources.values())
        return sources.attrgot("df")

    @staticmethod
    def verify_shapefile_folder():
        # Convert the file paths to Path objects
        shapefile_path = Path(IBGE_POLIGONO)
        parent_folder = shapefile_path.parent
        parent_folder.mkdir(exist_ok=True, parents=True)
        zip_file_path = parent_folder.with_suffix(".zip")

        # Check if all required files exist
        required_files = L(".cpg", ".dbf", ".prj", ".shx").map(
            shapefile_path.with_suffix
        )
        if not all(required_files.map(Path.is_file)):
            # shutil.rmtree(str(shapefile_path.parent), ignore_errors=True)
            parent_folder.ls().map(Path.unlink)
            # Download and unzip the zipped folder
            urllib.request.urlretrieve(MALHA_IBGE, zip_file_path)
            with ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(parent_folder)
            zip_file_path.unlink()

    def fill_nan_coordinates(
        self,
        df: pd.DataFrame,  # DataFrame com os dados da Anatel
    ) -> pd.DataFrame:  # DataFrame com as coordenadas validadas na base do IBGE
        """Valida as coordenadas consultado a Base Corporativa do IBGE, excluindo o que já está no cache na versão anterior"""

        municipios = pd.read_csv(
            IBGE_MUNICIPIOS,
            usecols=["Código_Município", "Latitude", "Longitude"],
            dtype="string[pyarrow]",
            dtype_backend="pyarrow",
        )

        df["Código_Município"] = df["Código_Município"].astype("string[pyarrow]")

        df = pd.merge(
            df,
            municipios,
            on="Código_Município",
            how="left",
            copy=False,
        )

        null_coords = df.Latitude_x.isna() | df.Longitude_x.isna()

        df.loc[null_coords, ["Latitude_x", "Longitude_x"]] = df.loc[
            null_coords, ["Latitude_y", "Longitude_y"]
        ]

        log = """[("Colunas", ["Latitude", "Longitude"]),
		           ("Processamento", "Coordenadas Ausentes. Inserido coordenadas do Município")]"""
        df = self.register_log(df, log, null_coords)

        df.rename(
            columns={
                "Latitude_x": "Latitude",
                "Longitude_x": "Longitude",
                "Latitude_y": "Latitude_ibge",
                "Longitude_y": "Longitude_ibge",
            },
            inplace=True,
        )

        return df

    def intersect_coordinates_on_poligon(
        self, df: pd.DataFrame, check_municipio: bool = True
    ):
        for column in ["Latitude", "Longitude"]:
            df[column] = pd.to_numeric(df[column], errors="coerce").astype("float")
        regions = gpd.read_file(IBGE_POLIGONO)

        # Convert pandas dataframe to geopandas df with geometry point given coordinates
        gdf_points = gpd.GeoDataFrame(
            df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude)
        )

        # Set the same coordinate reference system (CRS) as the regions shapefile
        gdf_points.crs = regions.crs

        # Spatial join points to the regions
        gdf = gpd.sjoin(gdf_points, regions, how="inner", predicate="within")

        if check_municipio:
            # Check correctness of Coordinates
            check_coords = gdf.Código_Município != gdf.CD_MUN

            log = """[("Colunas", ["Código_Município", "Município", "UF"]),
				  	 ("Processamento", "Informações substituídas  pela localização correta das coordenadas.")		      
				  """
            self.register_log(gdf, log, check_coords)

            gdf.drop(
                [
                    "Código_Município",
                    "Município",
                    "UF",
                    "geometry",
                    "AREA_KM2",
                    "index_right",
                ],
                axis=1,
                inplace=True,
            )

        gdf.rename(
            columns={
                "CD_MUN": "Código_Município",
                "NM_MUN": "Município",
                "SIGLA_UF": "UF",
            },
            inplace=True,
        )

        return gdf

    def validate_coordinates(
        self, df: pd.DataFrame, check_municipio: bool = True
    ) -> pd.DataFrame:
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

    @staticmethod
    def _simplify_sources(df):
        df["Fonte"] = df["Fonte"].str.replace(
            "ICAO-CANALIZACAO-VOR/ILS/DME | AISWEB-CANALIZACAO-VOR/ILS/DME",
            "CANALIZACAO-VOR/ILS/DME",
        )
        df["Fonte"] = df["Fonte"].str.replace(
            r"(ICAO-)?(AISWEB-)?CANALIZACAO-VOR/ILS/DME",
            "CANALIZACAO-VOR/ILS/DME",
            regex=True,
        )

        return df

    @staticmethod
    def _cast2float(column: pd.Series) -> pd.Series:
        return pd.to_numeric(
            column.fillna("-1"),
            downcast="float",
            errors="coerce",
            dtype_backend="pyarrow",
        )

    @staticmethod
    def _cast2int(column: pd.Series) -> pd.Series:
        return pd.to_numeric(
            column.fillna("0"),
            downcast="unsigned",
            errors="coerce",
            dtype_backend="pyarrow",
        )

    @staticmethod
    def _cast2str(column: pd.Series) -> pd.Series:
        column.replace("", "-1", inplace=True)
        return column.astype("string", copy=False).fillna("-1")

    @staticmethod
    def _cast2cat(column: pd.Series) -> pd.Series:
        column.replace("", "-1", inplace=True)
        return column.fillna("-1").astype("category", copy=False)

    @staticmethod
    def _remove_invalid_frequencies(df):
        df.sort_values(
            ["Frequência", "Latitude", "Longitude"], ignore_index=True, inplace=True
        )
        return df[df["Frequência"] <= LIMIT_FREQ]
        # TODO: save to discarded and log
        # log = f"""[("Colunas", "Frequência"),
        # 		   ("Processamento", "Frequência Inválida: Maior que {LIMIT_FREQ}")
        # 		  """
        # self.register_log(df, log, check_coords)

    @staticmethod
    def _format_types(df):
        df["Frequência"] = df["Frequência"].astype("double[pyarrow]")
        for col in FLOAT_COLUMNS:
            df[col] = Estacoes._cast2float(df[col])
        for col in INT_COLUMNS:
            df[col] = Estacoes._cast2int(df[col])
        for col in CAT_COLUMNS:
            df[col] = Estacoes._cast2cat(df[col])
        for col in STR_COLUMNS:
            df[col] = Estacoes._cast2str(df[col])
        return df

    def _format(
        self,
        dfs: List,  # List with the individual API sources
    ) -> pd.DataFrame:  # Processed DataFrame
        aero = dfs.pop()
        anatel = pd.concat(dfs, ignore_index=True)
        df = merge_on_frequency(anatel, aero)
        df = self.validate_coordinates(df)
        df = Estacoes._simplify_sources(df)
        df = Estacoes._format_types(df)
        df = Estacoes._remove_invalid_frequencies(df)
        return df.loc[:, self.columns]
