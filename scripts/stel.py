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


from extracao.datasources.sitarweb import Stel


if __name__ == '__main__':
	import time

	start = time.perf_counter()

	data = Stel()

	print(data.extraction())

	data.update()

	print(data.df)

	print(150 * '=')

	print(f'Elapsed time: {time.perf_counter() - start} seconds')
