from extracao.datasources.srd import SRD

if __name__ == '__main__':
	import time

	start = time.perf_counter()

	data = SRD()

	data.update()

	print('DATA')

	print(data.df.iloc[:, -10:])

	print(150 * '=')

	print(f'Elapsed time: {time.perf_counter() - start} seconds')
