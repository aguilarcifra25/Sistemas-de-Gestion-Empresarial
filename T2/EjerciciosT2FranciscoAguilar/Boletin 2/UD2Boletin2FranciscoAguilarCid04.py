'''
4. Si tenemos un diccionario para un inventario de un frutero inteligente, por ejemplo, inventario =
{"manzanas": 10, "naranjas": 5, "peras": 8}
Crear los siguientes apartados:
1. Mostrar todas las claves y valores.
2. Aumentar manzanas en 5.
3. Eliminar peras.
4. Calcular el total de frutas.

'''

exe = True
op = 0

inventario = {"manzanas": 10, "naranjas": 5, "peras": 8}

totalFrutas = 0

print('Bienvenido al programa del frutero inteligente')

while exe is True:

    print()

    print('Pulse 1 - Mostrar todas las claves y valores')
    print('Pulse 2 - Aumentar manzanas en 5')
    print('Pulse 3 - Eliminar peras')
    print('Pulse 4 - Calcular el total de frutas')
    print('Pulse 0 - Cerrar el programa')

    print()

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1:

            for clave in inventario:

                print(f'{clave}: {inventario[clave]}')

        case 2:

            inventario["manzanas"] += 5

            print(f'Ahora hay {inventario["manzanas"]} manzanas')

        case 3:

            del inventario["peras"]

            print('Las peras han sido eliminadas del inventario')

        case 4:

            totalFrutas = 0

            for clave in inventario:

                totalFrutas += inventario[clave]

            print(f'El total de frutas es: {totalFrutas}')

        case _:

            print('ERROR - Seleccione una opción válida')

print('\n--- Gracias por usar este programa ---')