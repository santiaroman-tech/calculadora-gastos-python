import os
os.system("cls")

import functions

from functions import *

def main():

    print("     CALCULADORA DE GASTOS      ")

    try:
        gasto1 = float(input("Ingrese el primer gasto: "))
        gasto2 = float(input("Ingrese el segundo gasto: "))
        gasto3 = float(input("Ingrese el tercer gasto: "))
    except ValueError:
        print("\nError: Por favor, ingrese solo números válidos.")
        return

    total = calcular_total(gasto1, gasto2, gasto3)
    promedio = calcular_promedio(total, 3)
    clasificacion = clasificar_gasto(total)
    print("           RESULTADOS           ")
    print(f"Total de gastos: ${total}")
    print(f"Promedio de gastos: ${promedio}")
    print(f"Clasificación: {clasificacion}")

if __name__ == "__main__":
    main()

