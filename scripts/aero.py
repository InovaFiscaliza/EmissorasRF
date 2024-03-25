from extracao.datasources.aeronautica import Aero


if __name__ == '__main__':
	import time

	start = time.perf_counter()

	data = Aero()

	data.update()

	print(150 * '=')

	print(data.df.Fonte.value_counts())

	# print("DISCARDED!")

	# print(data.discarded[["Frequência", "Entidade", "Log"]])

	print(150 * '=')

	print(f'Elapsed time: {time.perf_counter() - start} seconds')
