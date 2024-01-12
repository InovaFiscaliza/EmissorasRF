from extracao.datasources.telecom import Telecom

if __name__ == '__main__':
	import time

	start = time.perf_counter()

	data = Telecom()

	print(data.extraction())

	data.update()

	print(data.df)

	print(150 * '=')

	print(f'Elapsed time: {time.perf_counter() - start} seconds')
