def ingresar_ventas(lista_ventas):
    while True:
        try:
            curso = input("Ingrese el nombre del curso: ").upper()
            cantidad = int(input("Ingrese la cantidad de cursos vendidos: "))
            fecha = input("Ingrese la fecha de la venta (AAAA-MM-DD): ")
            precio = float(input("Ingrese el precio del curso: "))
            cliente = input("Ingrese el nombre del cliente: ").upper()
        except ValueError:
            print("Entradas no válidas, por favor intente otra vez.")
            continue

        venta = {
            "curso": curso,
            "cantidad": cantidad,
            "precio": precio,
            "fecha": fecha,
            "cliente": cliente,
        }
        lista_ventas.append(venta)

        continuar = input("¿Desea ingresar otra venta? (s/n): ").lower()
        if continuar == "s":
            print("--- Ingresando otra venta ---")
        elif continuar == "n":
            break
        else:
            print("Opción no válida")