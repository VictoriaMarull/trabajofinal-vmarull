import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd

from supermercado import (
    calcular_importe,
    debe_intercambiar,
    ordenar_burbuja,
    guardar_csv,
    leer_csv,
    ordenar_archivo
)


def test_calcular_importe():
    resultado = calcular_importe(3, 150)
    assert resultado == 450


def test_debe_intercambiar_por_sucursal():
    fila_1 = ["SUC09", "P100", "2025-02-04", "PROV01", "10", "100"]
    fila_2 = ["SUC08", "P100", "2025-02-04", "PROV01", "10", "100"]

    assert debe_intercambiar(fila_1, fila_2) == True


def test_debe_intercambiar_por_fecha():
    fila_1 = ["SUC08", "P100", "2025-04-10", "PROV01", "10", "100"]
    fila_2 = ["SUC08", "P100", "2025-02-04", "PROV01", "10", "100"]

    assert debe_intercambiar(fila_1, fila_2) == True


def test_ordenar_burbuja():
    filas = [
        ["SUC08", "P100", "2025-04-10", "PROV09", "58", "252.38"],
        ["SUC08", "P100", "2025-02-04", "PROV08", "55", "266.91"],
        ["SUC08", "P100", "2025-03-03", "PROV01", "54", "254.80"]
    ]

    filas_ordenadas = ordenar_burbuja(filas)

    assert filas_ordenadas[0][2] == "2025-02-04"
    assert filas_ordenadas[1][2] == "2025-03-03"
    assert filas_ordenadas[2][2] == "2025-04-10"


def test_guardar_y_leer_csv(tmp_path):
    archivo = tmp_path / "compras_prueba.csv"

    encabezado = ["PRSUC", "PRCOD", "PRFEC", "PRPROV", "PRCANT", "PRPRE"]
    filas = [
        ["SUC08", "P100", "2025-02-04", "PROV08", "55", "266.91"]
    ]

    guardar_csv(archivo, encabezado, filas)

    encabezado_leido, filas_leidas = leer_csv(archivo)

    assert encabezado_leido == encabezado
    assert filas_leidas == filas


def test_ordenar_archivo_crea_csv_ordenado(tmp_path):
    archivo_entrada = tmp_path / "entrada.csv"
    archivo_salida = tmp_path / "salida.csv"

    archivo_entrada.write_text(
        "PRSUC,PRCOD,PRFEC,PRPROV,PRCANT,PRPRE\n"
        "SUC08,P100,2025-04-10,PROV09,58,252.38\n"
        "SUC08,P100,2025-02-04,PROV08,55,266.91\n"
        "SUC08,P100,2025-03-03,PROV01,54,254.80\n"
    )

    ordenar_archivo(archivo_entrada, archivo_salida)

    df = pd.read_csv(archivo_salida)

    assert archivo_salida.exists()
    assert list(df["PRFEC"]) == [
        "2025-02-04",
        "2025-03-03",
        "2025-04-10"
    ]