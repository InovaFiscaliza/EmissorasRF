SELECT mun.NO_MUNICIPIO, mun.NU_LONGITUDE, mun.NU_LATITUDE, CONVERT(
        int, (
            mun.GE_POLIGONO.STIntersects (
                geometry::STGeomFromText (
                    'POINT(-46.7899 -23.5317)', mun.GE_POLIGONO.STSrid
                )
            )
        )
    ) AS COORD_VALIDA
from CORPORATIVO.dbo.TB_IBGE_MUNICIPIO mun
WHERE
    MUN.CO_MUNICIPIO = '3534401'