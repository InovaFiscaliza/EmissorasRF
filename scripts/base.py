import os
import warnings
from dotenv import find_dotenv, load_dotenv

from extracao.estacoes import Estacoes
from pprint import pprint

load_dotenv(find_dotenv(), override=True)
warnings.simplefilter('ignore')

SQLSERVER_PARAMS = dict(
	driver='{ODBC Driver 17 for SQL Server}',
	server='ANATELBDRO05',
	database='SITARWEB',
	trusted_conn=False,
	mult_results=True,
	encrypt=False,
	username=os.environ['USERNAME'],
	password=os.environ['PASSWORD'],
	timeout=1000,
)


if __name__ == '__main__':
	import time

	start = time.perf_counter()

	data = Estacoes(sql_params=SQLSERVER_PARAMS, limit=100000)

	data.update()

	print('DATA')

	pprint(data.df)

	pprint(150 * '=')

	pprint(data.df.Fonte.value_counts())

	# print('DISCARDED!')

	# print(data.discarded[['Frequência', 'Entidade', 'Log']])

	pprint(data.df.info())

	# print(150 * '=')

	# pprint(data.df.Log.value_counts())

	print(150 * '=')

	data.save()

	print(f'Elapsed time: {time.perf_counter() - start} seconds')
