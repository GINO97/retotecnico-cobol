import csv

def procesar_transacciones(archivo_csv):
    # Inicializar variables
    total_credito = 0.0
    total_debito = 0.0
    max_monto = 0.0
    id_max_monto = None # id no debe tener valor al inicio
    cont_credito = 0
    cont_debito = 0

    # Leer el archivo CSV
    with open(archivo_csv, mode='r',  encoding='latin-1') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            monto = float(row['monto']) # fila x fila va almacenando el valor de la columna monto en la variable "monto"
            
            if row['tipo'] == 'Crédito':    #en la columna "tipo" se va hacer el conteo y la sumatoria  por cada tipo de transaccion credito/debito
                total_credito += monto
                cont_credito += 1
            elif row['tipo'] == 'Débito':
                total_debito += monto
                cont_debito += 1
            
    # Verificar transacción con mayor monto
            if monto > max_monto:
                max_monto = monto
                id_max_monto = row['id']

    # Calculo de  balance final
    balance_final = total_credito - total_debito

    # Generar reporte en  CLI
    print("\nReporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance_final:.2f}")
    print(f"Transacción de Mayor Monto: ID {id_max_monto} - {max_monto:.2f}")
    print(f"Conteo de Transacciones: Crédito: {cont_credito} Débito: {cont_debito}\n")

""" ------------------------------------------------------------------------"""
#Colab
archivo = '/content/retotecnico-cobol/archivo.csv'
# VSC 
# archivo = r'C:\Users\tu_user\Documents\python_dev\env\archivo.csv'

try:
  procesar_transacciones(archivo)
except FileNotFoundError:
  print(f"Error: El archivo '{archivo}' no fue encontrado.")
except Exception as e:
  print(f"Ocurrió un error: {e}")
