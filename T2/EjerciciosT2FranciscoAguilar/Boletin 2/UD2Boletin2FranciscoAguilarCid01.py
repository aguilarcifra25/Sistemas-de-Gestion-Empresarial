'''
1. Dada la tupla temperaturas = (21, 24, 19, 30, 25, 28). Crear el código necesario para:

1. Mostrar el valor máximo y mínimo.
2. Calcular la temperatura media.
3. Convertir la tupla en lista, añadir una nueva temperatura y volver a convertir a tupla.
4. Comprobar si 30 está presente.
'''

exe = True
op = 0

temperaturas = (21, 24, 19, 30, 25, 28)

print('Bienvenido al gestor de temperaturas: ')

while exe is True:

    print()

    print('Pulse 1 - Mostrar el valor máximo y mínimo')
    print('Pulse 2 - Calcular la temperatura media')
    print('Pulse 3 - Convertir la tupla en lista, añadir una nueva temperatura y volver a convertir a tupla')
    print('Pulse 4 - Comprobar si 30 está presente')
    print('Pulse 0 - Cerrar el programa')

    print()

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1:

            print(f'Temperatura máxima: {max(temperaturas)}\nTemperatura mínima: {min(temperaturas)}')

        case 2:

            print(f'La media es de {sum(temperaturas) / len(temperaturas)}')

        case 3:

            temperaturas = list(temperaturas)

            temperaturas.append(99)

            tuple(temperaturas)

            print(temperaturas)

        case 4:

            print(30 in temperaturas)

        case _:

            print('ERROR - Seleccione una opción válida')

print('\n--- Gracias por usar este programa ---')