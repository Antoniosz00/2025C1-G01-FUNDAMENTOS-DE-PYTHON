"""
Autor: Antonio Sánchez
Fecha: 2025-04-29
Versión: 0.2
Sistema de análisis de reservas Rent a Car
"""

import pandas as pd
import os


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input('\nPresione Enter para continuar...')

def cargar_datos(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo, sep=';', encoding='utf-8')
        df["Días"] = pd.to_numeric(df["Días"], errors="coerce")
        return df
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None

def mostrar_paises(df):
    print("\nPaíses más frecuentes:")
    for pais, cantidad in df["País"].value_counts().head().items():
        print(f"{pais}: {cantidad}")

def mostrar_vuelos(df):
    print("\nNúmeros de vuelo más frecuentes:")
    for vuelo, cantidad in df["Vuelo"].value_counts().head().items():
        print(f"{vuelo}: {cantidad}")

def mostrar_carros(df):
    print("\nModelos de vehículo más rentados:")
    for carro, cantidad in df["Carro"].value_counts().head().items():
        print(f"{carro}: {cantidad}")

def mostrar_promedio_dias(df):
    dias_validos = df["Días"].dropna()
    promedio = dias_validos.mean()
    print(f"\nPromedio de duración de la renta: {promedio:.2f} días (basado en {len(dias_validos)} reservas válidas)")

# Menú principal
def menu():
    datos = cargar_datos("reservas.csv")
    if datos is None:
        print("No se pudieron cargar los datos.")
        return

    while True:
        limpiar_pantalla()
        print("\n--- Análisis de Reservas ---")
        print("1. Países más frecuentes")
        print("2. Números de vuelo más frecuentes")
        print("3. Modelos de vehículo más rentados")
        print("4. Promedio de duración de la renta")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_paises(datos)
            pausar()
        elif opcion == "2":
            mostrar_vuelos(datos)
            pausar()
        elif opcion == "3":
            mostrar_carros(datos)
            pausar()
        elif opcion == "4":
            mostrar_promedio_dias(datos)
            pausar()
        elif opcion == "5":
            print("Gracias por usar el sistema.")
            pausar()
            break
        else:
            print("Opción no válida.")
            pausar()

# Iniciar sistema
if __name__ == '__main__':
    print("Bienvenido al sistema de análisis de reservas Rent a Car")
    menu()