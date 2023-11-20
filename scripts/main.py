import json
import os
import shutil
import warnings
from datetime import datetime
import sys

import pandas as pd
import typer
from dotenv import find_dotenv, load_dotenv
from fastcore.xtras import Path

from extracao.estacoes import Estacoes

load_dotenv(find_dotenv(), override=True)
warnings.simplefilter('ignore')

SQLSERVER_PARAMS = dict(
	driver=os.environ.get('SQL_DRIVER'),
	server=os.environ.get('SQL_SERVER'),
	database=os.environ.get('SQL_DATABASE'),
	trusted_conn=True,
	mult_results=True,
	encrypt=False,
	timeout=int(os.environ.get('SQL_TIMEOUT')),
)

if sys.platform in ('linux', 'darwin', 'cygwin'):
	SQLSERVER_PARAMS.update(
		{
			'trusted_conn': False,
			'mult_results': False,
			'username': os.environ.get('USERNAME'),
			'password': os.environ.get('PASSWORD'),
		}
	)

MONGO_URI: str = os.environ.get('MONGO_URI')


def get_db(
	path: str = os.environ.get('DESTINATION'),  # Pasta onde salvar os arquivos",
	limit: int = 0,  # Número máximo de registros a serem extraídos da cada base MongoDB, 0: sem limite
	parallel: bool = True,  # Caso verdadeiro efetua as requisições de forma paralela em cada fonte de dados
) -> 'pd.DataFrame':  # Retorna o DataFrame com as bases da Anatel e da Aeronáutica
	"""Função para encapsular a instância e atualização dos dados"""
	data = Estacoes(SQLSERVER_PARAMS, MONGO_URI, limit, parallel)
	data.update()
	data.save()
	mod_times = {'ANATEL': datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
	mod_times['AERONAUTICA'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
	versiondb = json.loads((data.folder / 'VersionFile.json').read_text())
	mod_times['ReleaseDate'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
	versiondb['anateldb'].update(mod_times)
	json.dump(versiondb, (data.folder / 'VersionFile.json').open('w'))
	if path is not None:
		path = Path(path)
		path.mkdir(parents=True, exist_ok=True)
		print(f'Salvando dados em {path}')
		shutil.copytree(str(data.folder), str(path), dirs_exist_ok=True)
	return data


if __name__ == '__main__':
	import time

	start = time.perf_counter()

	typer.run(get_db)

	print(f'Elapsed time: {time.perf_counter() - start} seconds')
