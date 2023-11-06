from extracao.anatel import Outorgadas
from pprint import pprint


if __name__ == "__main__":
    import time

    start = time.perf_counter()

    data = Outorgadas()

    data.update()

    print("DATA")

    pprint(data.df)

    # print(150 * "=")

    # print("Coordenadas!")

    # display(data.Coords_Valida_IBGE.value_counts())

    data.save()

    print(f"Elapsed time: {time.perf_counter() - start} seconds")
