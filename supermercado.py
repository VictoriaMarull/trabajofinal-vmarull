import csv
import pandas as pd


# FUNCIONES GENERALES

def calcular_importe(cantidad, precio):
    return cantidad * precio


# LECTURA Y ESCRITURA DE ARCHIVOS

def leer_csv(nombre_archivo):
    archivo = open(nombre_archivo, "r", newline="")
    lector = csv.reader(archivo)

    encabezado = next(lector)

    filas = []
    for fila in lector:
        filas.append(fila)

    archivo.close()

    return encabezado, filas


def guardar_csv(nombre_archivo, encabezado, filas):
    archivo = open(nombre_archivo, "w", newline="")
    escritor = csv.writer(archivo)

    escritor.writerow(encabezado)

    for fila in filas:
        escritor.writerow(fila)

    archivo.close()


def leer_compras(nombre_archivo):
    return pd.read_csv(nombre_archivo)


# ORDENAMIENTO BURBUJA

def debe_intercambiar(f1, f2):
    if f1[0] > f2[0]:
        return True

    elif f1[0] == f2[0]:
        if f1[1] > f2[1]:
            return True

        elif f1[1] == f2[1]:
            if f1[2] > f2[2]:
                return True

            elif f1[2] == f2[2]:
                if f1[3] > f2[3]:
                    return True

                elif f1[3] == f2[3]:
                    if int(f1[4]) > int(f2[4]):
                        return True

                    elif int(f1[4]) == int(f2[4]):
                        if float(f1[5]) > float(f2[5]):
                            return True

    return False


def ordenar_burbuja(filas):
    n = len(filas)

    for i in range(n - 1):
        hubo_intercambio = False

        for j in range(n - 1 - i):
            if debe_intercambiar(filas[j], filas[j + 1]):
                aux = filas[j]
                filas[j] = filas[j + 1]
                filas[j + 1] = aux
                hubo_intercambio = True

        if hubo_intercambio == False:
            break

    return filas


def ordenar_archivo(archivo_entrada, archivo_salida):
    encabezado, filas = leer_csv(archivo_entrada)
    filas_ordenadas = ordenar_burbuja(filas)
    guardar_csv(archivo_salida, encabezado, filas_ordenadas)


# ANÁLISIS DE DATOS

def mostrar_totales_por_producto(df):
    i = 0

    while i < len(df):
        suc = df["PRSUC"][i]
        prod = df["PRCOD"][i]

        total_unidades = 0
        total_importe = 0

        while i < len(df) and df["PRSUC"][i] == suc and df["PRCOD"][i] == prod:
            total_unidades += df["PRCANT"][i]
            total_importe += calcular_importe(df["PRCANT"][i], df["PRPRE"][i])
            i += 1

        print("Sucursal:", suc, "| Producto:", prod, "| Unidades:", total_unidades, "| Total $:", total_importe)


def mostrar_totales_por_sucursal(df):
    i = 0

    while i < len(df):
        suc = df["PRSUC"][i]

        total_sucursal = 0
        mayor_producto = ""
        mayor_importe = 0
        menor_producto = ""
        menor_importe = 999999999

        while i < len(df) and df["PRSUC"][i] == suc:
            prod = df["PRCOD"][i]

            total_unidades = 0
            total_importe = 0

            while i < len(df) and df["PRSUC"][i] == suc and df["PRCOD"][i] == prod:
                total_unidades += df["PRCANT"][i]
                total_importe += calcular_importe(df["PRCANT"][i], df["PRPRE"][i])
                i += 1

            total_sucursal += total_unidades

            if total_importe > mayor_importe:
                mayor_importe = total_importe
                mayor_producto = prod

            if total_importe < menor_importe:
                menor_importe = total_importe
                menor_producto = prod

        print("Sucursal:", suc)
        print("Total unidades:", total_sucursal)
        print("Mayor producto:", mayor_producto, "| Importe:", mayor_importe)
        print("Menor producto:", menor_producto, "| Importe:", menor_importe)
        print("")


def mostrar_totales_generales(df):
    i = 0
    cantidad_sucursales = 0
    total_general = 0

    while i < len(df):
        suc = df["PRSUC"][i]
        cantidad_sucursales += 1

        while i < len(df) and df["PRSUC"][i] == suc:
            total_general += calcular_importe(df["PRCANT"][i], df["PRPRE"][i])
            i += 1

    print("Cantidad de sucursales:", cantidad_sucursales)
    print("Total general $:", total_general)


def ejecutar_programa():
    archivo_entrada = "COMPRAS_supermercado_desordenado_solo_sucursal.csv"
    archivo_salida = "COMPRAS_supermercado_ordenado.csv"

    print("Cargando archivo...")
    ordenar_archivo(archivo_entrada, archivo_salida)
    print("Archivo ordenado guardado.")
    print("")

    df = leer_compras(archivo_salida)

    print("CORTE POR PRODUCTO")
    print("")
    mostrar_totales_por_producto(df)
    print("")

    print("CORTE POR SUCURSAL")
    print("")
    mostrar_totales_por_sucursal(df)

    print("TOTALES GENERALES")
    print("")
    mostrar_totales_generales(df)