from extracao.datasources.smp import SMP
from pprint import pprint


if __name__ == '__main__':
	import time

	start = time.perf_counter()

	data = SMP(limit=100000)

	data.update()

	print(data.df)

	print(150 * '=')

	# print("DISCARDED!")

	# print(data.discarded[["Frequência", "Entidade", "Log"]])

	print(150 * '=')

	print(f'Elapsed time: {time.perf_counter() - start} seconds')
