# AUTOGENERATED! DO NOT EDIT! File to edit: ..\nbs\format.ipynb.

# %% auto 0
__all__ = ['scrape_dataframe', 'input_coordenates', 'parse_bw', 'optimize_floats', 'optimize_ints', 'optimize_objects',
           'df_optimize', 'format_types']

# %% ..\nbs\format.ipynb 2
import re
from typing import List, Iterable, Union
from pathlib import Path
from collections import OrderedDict
from decimal import Decimal

import pandas as pd
from unidecode import unidecode
from gazpacho import get, Soup
from fastcore.utils import listify
from rich.progress import track

from .constants import ENTIDADES, COL_PB, ESTACAO, BW, BW_pattern

# %% ..\nbs\format.ipynb 4
def scrape_dataframe(id_list: Iterable[str], #Lista de ids do Mosaico
) -> pd.DataFrame: # Dataframe com os dados raspados da página do Mosaico
    """Recebe uma lista de ids do Mosaico e retorna um dataframe com os dados raspados da página do MOSAICO"""
    df = pd.DataFrame()
    for id_ in track(id_list, description="Baixando informações complementares da Web"):
        html = get(ESTACAO.format(id_))
        df = df.append(
            pd.read_html(Soup(getattr(html, "text", "")).find("table").html)[0]
        )

    df.rename(
        columns={"NumFistel": "Fistel", "Num Serviço": "Num_Serviço"}, inplace=True
    )
    return df[
        [
            "Status",
            "Entidade",
            "Fistel",
            "Frequência",
            "Classe",
            "Num_Serviço",
            "Município",
            "UF",
        ]
    ]

# %% ..\nbs\format.ipynb 5
def input_coordenates(df: pd.DataFrame, # DataFrame a imputar coordenadas inválidas
                      pasta: Union[str, Path]) -> pd.DataFrame:
    """Imputa os registros com coordenadas ausentes (NA's) com as coordenadas do município"""
    municipios = Path(f"{pasta}/municípios.fth")
    if not municipios.exists():
        municipios = Path(f"{pasta}/municípios.xlsx")
        if not municipios.exists():
            raise FileNotFoundError(
                f"É necessario a tabela de municípios municípios.fth | municípios.xlsx na pasta {pasta}"
            )
        m = pd.read_excel(municipios, engine="openpyxl")
    else:
        m = pd.read_feather(municipios)
    m.loc[
        m.Município == "Sant'Ana do Livramento", "Município"
    ] = "Santana do Livramento"
    m["Município"] = m.Município.apply(unidecode).str.lower().str.replace("'", " ")
    m["UF"] = m.UF.str.lower()
    df["Coordenadas_do_Município"] = False
    df["Latitude"] = df.Latitude.str.replace(",", ".")
    df["Longitude"] = df.Longitude.str.replace(",", ".")
    df.loc[df["Município"] == "Poxoréo", "Município"] = "Poxoréu"
    df.loc[df["Município"] == "Couto de Magalhães", "Município"] = "Couto Magalhães"
    df["Município"] = df.Município.astype("string")
    criteria = (
        (df.Latitude == "")
        | (df.Latitude.isna())
        | (df.Longitude == "")
        | (df.Longitude.isna())
    ) & df.Município.isna()
    df = df[~criteria]
    for row in df[
        (
            (df.Latitude == "")
            | (df.Latitude.isna())
            | (df.Longitude == "")
            | (df.Longitude.isna())
        )
    ].itertuples():
        try:
            left = unidecode(row.Município).lower()
            m_coord = (
                m.loc[
                    (m.Município == left) & (m.UF == row.UF.lower()),
                    ["Latitude", "Longitude"],
                ]
                .values.flatten()
                .tolist()
            )
            df.loc[row.Index, "Latitude"] = m_coord[0]
            df.loc[row.Index, "Longitude"] = m_coord[1]
            df.loc[row.Index, "Coordenadas_do_Município"] = True
        except ValueError:
            print(left, row.UF, m_coord)
            continue
    return df

# %% ..\nbs\format.ipynb 6
def parse_bw(bw: str, #Largura de Banda codificada como string
) -> float: #Largura de Banda codificada como float
    """Parse the bandwidth string"""
    if match := re.match(BW_pattern, bw):
        multiplier = BW[match.group(2)]
        if mantissa := match.group(3):
            number = float(f"{match.group(1)}.{mantissa}")
        else:
            number = float(match.group(1))
        return multiplier * number
    return -1

# %% ..\nbs\format.ipynb 9
def optimize_floats(df: pd.DataFrame, # DataFrame a ser otimizado
exclude: Iterable[str] = None, # Colunas a serem excluidas da otimização
)->pd.DataFrame: # DataFrame com as colunas do tipo `float` otimizadas
    """Otimiza os floats do dataframe para reduzir o uso de memória"""
    floats = df.select_dtypes(include=["float64"]).columns.tolist()
    floats = [c for c in floats if c not in listify(exclude)]
    df[floats] = df[floats].apply(pd.to_numeric, downcast="float")
    return df

# %% ..\nbs\format.ipynb 10
def optimize_ints(df: pd.DataFrame, # Dataframe a ser otimizado
exclude: Iterable[str] = None, # Colunas a serem excluidas da otimização
)->pd.DataFrame: # DataFrame com as colunas do tipo `int` otimizadas
    """Otimiza os ints do dataframe para reduzir o uso de memória"""
    ints = df.select_dtypes(include=["int64"]).columns.tolist()
    ints = [c for c in ints if c not in listify(exclude)]
    df[ints] = df[ints].apply(pd.to_numeric, downcast="integer")
    return df

# %% ..\nbs\format.ipynb 11
def optimize_objects(
    df: pd.DataFrame, # DataFrame a ser otimizado
    datetime_features: Iterable[str] = None, # Colunas que serão convertidas para datetime
    exclude: Iterable[str] = None, # Colunas que não serão convertidas
) -> pd.DataFrame: # DataFrame com as colunas do tipo `object` otimizadas
    """Otimiza as colunas do tipo `object` no DataFrame para `category` ou `string` para reduzir a memória e tamanho de arquivo"""
    exclude = listify(exclude)
    datetime_features = listify(datetime_features)
    for col in df.select_dtypes(
        include=["object", "string", "category"]
    ).columns.tolist():
        if col not in datetime_features:
            if col in exclude:
                continue
            num_unique_values = len(df[col].unique())
            num_total_values = len(df[col])
            if float(num_unique_values) / num_total_values < 0.5:
                dtype = "category"
            else:
                dtype = "string"
            df[col] = df[col].astype(dtype)
        else:
            df[col] = pd.to_datetime(df[col]).dt.date
    return df


# %% ..\nbs\format.ipynb 12
def df_optimize(
    df: pd.DataFrame, # DataFrame a ser otimizado
    datetime_features: Iterable[str] = None, # Colunas que serão convertidas para datetime
    exclude: Iterable[str] = None, # Colunas que não serão convertidas
) -> pd.DataFrame: # DataFrame com as colunas com tipos de dados otimizados
    """Função que encapsula as anteriores para otimizar os tipos de dados e reduzir o tamanho do arquivo e uso de memória"""
    if datetime_features is None:
        datetime_features = []
    return optimize_floats(
        optimize_ints(optimize_objects(df, datetime_features, exclude), exclude),
        exclude,
    )

# %% ..\nbs\format.ipynb 13
def format_types(df: pd.DataFrame, # DataFrame a ser formatado
                 stem: str = None, # Identificador do arquivo para otimização específica
) -> pd.DataFrame:    # DataFrame formatado 

    """Convert the columns of a dataframe to optimized types"""
    if stem != 'radcom':
        df["Num_Serviço"] = df["Num_Serviço"].astype("category")
    if stem == "stel":
        df.loc[:, "Validade_RF"] = df.Validade_RF.astype("string").str.slice(0, 10)
        df.loc[df.Unidade == "kHz", "Frequência"] = df.loc[
            df.Unidade == "kHz", "Frequência"
        ].apply(lambda x: Decimal(x) / Decimal(1000))
        df.loc[df.Unidade == "GHz", "Frequência"] = df.loc[
            df.Unidade == "GHz", "Frequência"
        ].apply(lambda x: Decimal(x) * Decimal(1000))
        df.drop("Unidade", axis=1, inplace=True)
    elif stem == "radcom":
        a = df.Situação.isna()
        df.loc[a, "Classe"] = df.loc[a, "Fase"]
        df.loc[~a, "Classe"] = (
            df.loc[~a, "Fase"].astype("string")
            + "-"
            + df.loc[~a, "Situação"].astype("string")
        )
        df.loc[:, "Classe"] = df["Classe"].astype("category")
        df.drop(["Fase", "Situação"], axis=1, inplace=True)
    elif stem == 'base':
        df['Status'] = df['Status'].astype('category')
        df["BW(kHz)"] = df["BW(kHz)"].astype("float32")
    if stem in {'stel', 'base'}:
        df['Classe'] = df['Classe'].astype('category')
        df['Classe_Emissão'] = df['Classe_Emissão'].astype('category')
        df['Largura_Emissão'] = df['Largura_Emissão'].astype('category')

    df["Frequência"] = df["Frequência"].astype("string")
    df["Latitude"] = df["Latitude"].astype("float32")
    df["Longitude"] = df["Longitude"].astype("float32")
    df["Entidade"] = df["Entidade"].astype("string")
    df["Fistel"] = df["Fistel"].astype("string")
    df["Município"] = df["Município"].astype("category")
    df["UF"] = df["UF"].astype("category")
    df["CNPJ"] = df["CNPJ"].astype("string")
    df["Número_Estação"] = df["Número_Estação"].astype("string")

    return df
