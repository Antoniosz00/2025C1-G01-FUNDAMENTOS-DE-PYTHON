"""
Autor: Antonio Sánchez
Fecha: 23/4/2025
Versión: 0.1
Sistema de Gestión de Ventas 
"""

import os
from modulo import ingresar_ventas

    

def limpiar_pantalla():
    """Limpia la pantalla de la terminal en ejecución"""
    os.system("cls" if os.name == "nt" else "clear")
    

def pausar():
    input("\n Presione enter para continuar")

#Menú Principal
def menu():
    ventas = []
    while True: 
        print("\n---- Menú Principal ----")
        print("1. Ingresar Ventas de cursos UMCA")
        print("2. Guardar datos en un archivo CSV")
        print("3. Analizar las ventas")
        print("4. Salir")
        opcion = input("Ingrese una Opcion: ")
        
        if opcion == "1" :
            print("\n---- Ingreso de Ventas de Cursos----")
            ingresar_ventas(ventas)
            pausar()
        elif opcion == "2":
            print("\n----Guardar Ventas----")
            pausar()
        elif opcion == "3":
            print("\n---- Análisis de Ventas----")
            pausar()
        elif opcion == "4":
            print("\n Gracias por usar el sistema. Hasta pronto")  
            pausar()
            break # Con el break se cierra el sistema del ciclo while
        else:
            print("Opcion no valida. Intente Nuevamente una opcion.")          



#Ejecución del sistema si solo si el archivo es el main
if __name__ == "__main__" :
    print ("Bienvenido al sistema de gestión de Ventas")
    menu()
    
    