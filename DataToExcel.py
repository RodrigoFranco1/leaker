"""
DataToExcel.py
Realiza una búsqueda en la API de DeHashed.

Autor: Rodrigo Y. Franco Benavides
Versión: 1.0
Lindekin: @rodrigofrancob
Telegram: @Gh0st_x3
"""

import pandas as pd
import sys

def process_text_file(file_path):
    records = []
    current_record = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Registro"):
                if current_record:
                    records.append(current_record)
                current_record = {}
            else:
                key_value = line.split(":", 1)
                if len(key_value) == 2:
                    key, value = key_value
                    current_record[key.strip()] = value.strip()
    
    if current_record:
        records.append(current_record)

    return pd.DataFrame(records)

def main():
    if len(sys.argv) != 2:
        print("Uso: python DataToExcel.py <archivo.txt>")
        print("Ejemplo: python DataToExcel.py datos.txt")
        print("El script convierte un archivo de texto con el formato específico de leaker.py a un archivo Excel ordenado por columnas.")
        sys.exit(1)

    text_file = sys.argv[1]
    df = process_text_file(text_file)

    excel_file = text_file.replace('.txt', '.xlsx')
    df.to_excel(excel_file, index=False)
    print(f"Archivo Excel generado: {excel_file}")

if __name__ == "__main__":
    main()
