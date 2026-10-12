# EJERCICIO 3 DICCIONARIOS: inventario de componentes de un robot :D

# clave = nombre del componente, valor = cantidad, como el intercambio equivalente de Fullmetal Alchemist :D
inventario = {"motor": 4, "sensor": 10, "led": 25}

opcion = 0

# el menu se repite hasta que el usuario elija la opcion 5
while opcion != 5:
    print("\n===== INVENTARIO =====")
    print("1. Ver inventario")
    print("2. Agregar componente")
    print("3. Eliminar componente")
    print("4. Total de piezas")
    print("5. Salir")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        # items nos da la clave y el valor al mismo tiempo :D
        for componente, cantidad in inventario.items():
            print(componente, "->", cantidad)

    elif opcion == 2:
        nombre = input("Nombre del componente: ")
        cantidad = int(input("Cantidad a agregar: "))

        # in revisa si la clave ya existe en el diccionario xd
        if nombre in inventario:
            inventario[nombre] = inventario[nombre] + cantidad   # si existe, sumamos
        else:
            inventario[nombre] = cantidad                        # si no existe, lo creamos

        print("Listo, inventario actualizado xd")

    elif opcion == 3:
        nombre = input("Componente a eliminar: ")

        if nombre in inventario:
            del inventario[nombre]   # del lo borra como si su nombre estuviera en el Death Note de Light :-v
            print("Componente eliminado")
        else:
            print("Ese componente no existe")   # ni Ryuk lo encuentra xd

    elif opcion == 4:
        total = 0
        # values nos da solo las cantidades, como contar las Gemas del Infinito :D
        for cantidad in inventario.values():
            total = total + cantidad
        print("Total de piezas:", total)

    elif opcion == 5:
        print("Hasta luego, Avengers Assemble otra vez cuando quieras :D")

    else:
        print("Opcion no valida, intenta de nuevo xd")