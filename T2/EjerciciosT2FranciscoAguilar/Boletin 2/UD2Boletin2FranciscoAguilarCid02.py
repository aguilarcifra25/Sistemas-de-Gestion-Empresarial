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

productoBuscar = ''
productoNuevo = ''
posicion = 0
listaProductos = []

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

            productoBuscar = input('Indique el producto que quiere contar: ')

            print(f'El producto {productoBuscar} aparece {productos.count(productoBuscar)} veces')

        case 3:

            print(f'Productos actuales: {productos}\n')

            posicion = int(input(f'Indique la posición del producto a modificar (1 - {len(productos)}): '))

            if posicion >= 1 and posicion <= len(productos):

                productoNuevo = input('Indique el nuevo producto: ')

                listaProductos = list(productos)
                listaProductos[posicion - 1] = productoNuevo
                productos = tuple(listaProductos)

                print(f'\nTupla modificada: {productos}')

            else:

                print('ERROR - Posición no válida')

        case 4:

            productoNuevo = input('Indique el producto que quiere añadir: ')

            productos = productos + (productoNuevo,)

            print(f'\nTupla actualizada: {productos}')

        case _:

            print('ERROR - Seleccione una opción válida')

print('\n--- Gracias por usar este programa ---')