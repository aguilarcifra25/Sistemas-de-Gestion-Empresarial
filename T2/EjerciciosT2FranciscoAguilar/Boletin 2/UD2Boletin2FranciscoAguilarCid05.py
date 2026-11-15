'''
Crea un conjunto de números enteros leyendo por teclado. Se podrá hacer lo siguiente:
1. Añadir el número 15.
2. Eliminar el número 9.
3. Calcular la cantidad de elementos.
4. Comprobar si 6 está en el conjunto
'''

exe = True
op = 0

conjunto = set()

print('Bienvenido al programa de los números enteros')

print('\nEn primer lugar indique cuántos números enteros quiere meter:')
cant = int(input(''))

print()

for i in range(cant):

    conjunto.add(int(input('Indique el siguiente número entero: ')))


while exe is True:

    print('\nPulse 1 - Añadir el 15')
    print('Pulse 2 - Eliminar el 9')
    print('Pulse 3 - Calcular cantidad de elementos')
    print('Pulse 4 - Comprobar si el 6 está en el conjunto')
    print('Pulse 0 - Cerrar programa')

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1:

            conjunto.add(15)

            print(conjunto)

        case 2:

            if 9 in conjunto:

                conjunto.remove(9)

            print(conjunto)

        case 3:

            print(f'El conjunto tiene {len(conjunto)} elementos.')

        case 4:

            if 6 in conjunto:

                print('El 6 está en el conjunto')

            else:

                print('El 6 no está en el conjunto')

        case _:

            print('ERROR - Elige una opción válida')

print('--- Gracias por usar este programa ---')