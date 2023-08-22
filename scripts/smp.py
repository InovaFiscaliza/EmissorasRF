import sys
from pathlib import Path

sys.path.insert(0, str(Path().cwd()))


import os
from fastcore.xtras import Path
from time import perf_counter
import pandas as pd
from pymongo import MongoClient
from dotenv import find_dotenv, load_dotenv
from ydata_profiling import ProfileReport

start = perf_counter()

load_dotenv(find_dotenv())
uri = os.environ["MONGO_URI"]
mongo_client = MongoClient(uri)
mongo_client.server_info()

database = mongo_client["sms"]

# for c in database.list_collection_names():
#     pprint(c)
#     pprint(database[c].find_one())
#     pprint(20*'=')

MONGO_SMP = {
    "$and": [
        # {"DataExclusao": None},
        {"DataValidade": {"$nin": ["", None]}},
        {"Status.state": "LIC-LIC-01"},
        {"NumServico": "010"},
        # {"FreqInicialMHz": {"$nin": [None, "", 0]}},
        # {"FreqCentralMHz": {"$nin": [None, "", 0]}},
        # {"FreqFinalMHz": {"$nin": [None, "", 0]}},
        {"FreqTxMHz": {"$nin": [None, "", 0]}},
        {"FreqRxMHz": {"$nin": [None, "", 0]}},
    ]
}

COLS_SMP = {
    "NumAto": "Num_Ato",
    "NumFistel": "Fistel",
    "NomeEntidade": "Entidade",
    "SiglaUf": "UF",
    "NumEstacao": "Número_Estação",
    "CodMunicipio": "Código_Município",
    "DataValidade": "Validade_RF",
    "FreqInicialMHz": "Frequência_Inicial",
    "FreqCentralMHz": "Frequência_Central",
    "FreqTxMHz": "Frequência_Transmissão",
    "FreqRxMHz": "Frequência_Recepção",
    "FreqFinalMHz": "Frequência_Final",
    "formId": "Tipo_Estação",
    "Tecnologia": "Tecnologia",
    "Latitude": "Latitude",
    "Longitude": "Longitude",
    "DesignacaoEmissao": "Designacao_Emissão",
    "PotenciaTransmissorWatts": "Potência(W)",
    "CodTipoAntena": "Cod_TipoAntena",
    "Polarizacao": "Polarização",
    "RaioAntena": "Raio_Antena",
    "GanhoAntena": "Ganho_Antena",
    "FrenteCostaAntena": "FC_Antena",
    "AnguloMeiaPotenciaAntena": "Ang_MP_Antena",
    "AnguloElevacao": "Ângulo_Elevação",
    "Azimute": "Azimute",
    "AlturaAntena": "Altura_Antena",
    "PerdasAcessorias": "Perdas_Acessorias",
}

DTYPE_SMP = {
    "NumAto": "category",
    "NumFistel": "category",
    "NomeEntidade": "category",
    "SiglaUf": "category",
    "NumEstacao": "string",
    "CodMunicipio": "category",
    "DataValidade": "category",
    "FreqInicialMHz": "category",
    "FreqCentralMHz": "category",
    "FreqFinalMHz": "category",
    "FreqTxMHz": "category",
    "FreqRxMHz": "category",
    "formId": "category",
    "Tecnologia": "category",
    "Latitude": "float",
    "Longitude": "float",
    "DesignacaoEmissao": "category",
    "PotenciaTransmissorWatts": "float",
    "CodTipoAntena": "category",
    "Polarizacao": "category",
    "RaioAntena": "float",
    "GanhoAntena": "float",
    "FrenteCostaAntena": "float",
    "AnguloMeiaPotenciaAntena": "float",
    "AnguloElevacao": "float",
    "Azimute": "float",
    "AlturaAntena": "float",
    "PerdasAcessorias": "float",
}


collection = database["licenciamento"]

query = collection.find(MONGO_SMP, projection={k: 1.0 for k in COLS_SMP}, limit=0)

df = pd.DataFrame(list(query))  # , columns=COLS_SMP.keys())
df.drop(columns=["_id"], inplace=True)

# for k, v in DTYPE_SMP.items():
#     if "float" in v:
#         df[k] = pd.to_numeric(df[k], errors="coerce")
#     try:
#         df[k] = df[k].astype(v)
#     except Exception as e:
#         print(e)
#         print(k)

dados = Path(__file__).resolve().parent.parent / "dados"
dados.mkdir(parents=True, exist_ok=True)

df.astype("string").to_parquet(
    f"{dados}/smp_formated.parquet.gzip",
    compression="gzip",
    index=False,
)

for k, v in DTYPE_SMP.items():
    if v == "float":
        df[k] = df[k].str.replace(",", ".").str.extract(r"([\d*\.?\d*])")
        df.loc[df[k] == ".", k] = pd.NA

df = df.astype(DTYPE_SMP)

profile = ProfileReport(df, minimal=True, title="Entidades SMP")

profile.to_file(f"{dados}/relatorio_smp.html")

print(f"Total time (minutes): {(perf_counter() - start)/60:.2f}")
