# retotecnico-cobol

## Introduccion:

El reto tiene como proposito demostrar habilidades en procesamiento de datos, manejo de archivos y generación de reportes.
Esto consiste en procesar un archivo CSV con transacciones bancarias y generar un reporte :
    - Balance final (Creditos - debitos)
    - Transacciones de mayor monto
    - Contro de transacciones por tipo

## Instrucciones de Ejecucion:
     ### Requisitos
        - python 3 
        - no se requiere dependencias
     ### Ejecución
        - Clona repositorio     -> git clone https://github.com/GINO97/reporte-transacciones.git
        - Crea un archivo.csv 
        - Ejecuta el programa   -> python reporte_transacciones.py archivo.csv
            

## Enfoque y Solución:
    - Lectura de datos: Uso de csv.DictReader para manejar eficientemente los datos

    - Procesamiento 
        * Acumuladores separados para creditos y debitos
        * Comparacion para hallar el monto maximo
        * Contadores por tipo de transaccion
        * Manejo de errores: Validacion de archivo y formato de datos

## Estructura del Proyecto:
/retotecnico-cobol/
│
├── reporte_transacciones.py  # Script principal 
├── archivo.csv # Archivo CSV de ejemplo
├── README.md                 # Este archivo con documentacion
├──requirements.txt           # Version 3.13.1 py