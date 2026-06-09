# Trabajo Final Integrador

Sistema de procesamiento de compras de supermercado desarrollado en Python.

## Objetivo

Procesar un archivo de compras de supermercado mediante técnicas de ordenamiento y corte de control, obteniendo información consolidada por producto, sucursal y totales generales.

## Funcionalidades

* Lectura de archivos CSV.
* Ordenamiento de registros mediante método burbuja.
* Generación de archivo ordenado.
* Cálculo de importes y totales.
* Corte de control por producto.
* Corte de control por sucursal.
* Obtención de totales generales.
* Pruebas unitarias automatizadas con Pytest.
* Pipeline de Integración Continua mediante GitHub Actions.

## Estructura del Proyecto

```text
trabajofinal-vmarull/
│
├── main.py
├── supermercado.py
├── requirements.txt
├── README.md
├── COMPRAS_supermercado_desordenado_solo_sucursal.csv
├── COMPRAS_supermercado_ordenado.csv
│
└── tests/
    └── test_supermercado.py
```

## Instalación

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Ejecutar el programa:

```bash
python3 main.py
```

## Tests

Ejecutar las pruebas unitarias:

```bash
pytest -v
```

## Integración Continua

El proyecto incorpora GitHub Actions para ejecutar automáticamente las pruebas unitarias ante cada push y pull request, permitiendo validar el correcto funcionamiento del sistema en cada cambio realizado.

## Tecnologías utilizadas

* Python 3.12
* Pandas
* Pytest
* Git
* GitHub
* GitHub Actions

```
```
