'''
2. Dada la tupla productos = ("pan", "leche", "huevos", "queso")

1. Mostrar el primer y último elemento.
2. Contar cuántas veces aparece un producto (elige uno).
3. Convertir a lista, modificar un elemento y volver a tupla.
4. Añadir un nuevo producto (tupla concatenada).

'''

exe = True
op = 0

productos = ("pan", "leche", "huevos", "queso")

print('Bienvenido al programa de los productos')

while exe is True:

    print()
    
    print('Pulse 1 - Mostrar el primer y último elemento')
    print('Pulse 2 - Contar cuántas veces aparece un producto (elige uno)')
    print('Pulse 3 - Convertir a lista, modificar un elemento y volver a tupla')
    print('Pulse 4 - Añadir un nuevo producto (tupla concatenada)')
    print('Pulse 0 - Cerrar el programa')

    print()

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1:

            print(f'Primer producto: {productos[0]}\nÚltimo producto: {productos[len(productos) - 1]}')

        case 2:
        
            print()

        case 3:
        
            print()

        case 4:
        
            print()

        case _:

            print('ERROR - Seleccione una opción válida')





