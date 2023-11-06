from extracao.datasources.smp import SMP
from pprint import pprint


if __name__ == "__main__":
    import time

    start = time.perf_counter()

    data = SMP(limit=50000)

    data.update()

    print("DATA")

    pprint(data.df.loc[data.df.Frequência.notna()].drop('Log', axis=1))

    print(150 * "=")

    print("Descartadas!")

    print(data.discarded)

    # display(data.Coords_Valida_IBGE.value_counts())

    data.save()

    print(f"Elapsed time: {time.perf_counter() - start} seconds")
