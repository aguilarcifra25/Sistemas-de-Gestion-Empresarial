'''
6. Crea un programa que lea de un fichero y tenga las siguientes funcionalidades en un menú:
- La palabra de mayor longitud.
- Las veces que aparece una palabra.
- Lea una línea aleatoria del fichero.
- Dos funcionalidades más inventadas por tí.
'''

import random

op = 0
exe = True

print('Bienvenido, este programa lee permite tomar las siguientees acciones sobre un fichero')

while exe is True:

    print('\nPulse 1 - Busca la palabra de mayor longitud')
    print('Pulse 2 - Busca las veces que aparece una palabra')
    print('Pulse 3 - Lee una línea aleatoria del fichero')
    print('Pulse 4 - Busca la palabra de menor longitud')
    print('Pulse 5 - Imprime el fichero')
    print('Pulse 0 - Cerrar el programa\n')

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1:

            f = open('Ej6/fichero.txt')

            masLarga = ''
            listaMasLargas = []

            for line in f.read().split():

                if len(line) > len(masLarga):

                    listaMasLargas.clear()

                    masLarga = line

                if len(line) == len(masLarga):

                    listaMasLargas.append(line)


            print(f'Palabra(s) más larga(s): {listaMasLargas}')

            f.close()

        case 2:

            f = open('Ej6/fichero.txt')

            palabraBuscada = input('Indica la palabra que quieres buscar: ')

            print(f'\nLa palabra sale {f.read().split().count(palabraBuscada)} veces.')

            f.close()

        case 3:

            f = open('Ej6/fichero.txt')

            cantLineas = len(f.readlines())

            f.seek(0)

            print(f.readlines()[random.randint(0, cantLineas - 1)])

            f.close()

        case 4:

            f = open('Ej6/fichero.txt')
            
            masCorta = f.read().split()
            listaMasCortas = []

            f.seek(0)

            for line in f.read().split():

                if len(line) < len(masCorta):

                    listaMasCortas.clear()

                    masCorta = line

                if len(line) == len(masCorta):

                    listaMasCortas.append(line)


            print(f'Palabra(s) más corta(s): {listaMasCortas}')

            f.close()

        case 5:

            f = open('Ej6/fichero.txt')

            print(f.read())

        case _:

            print('ERROR - Selecciona una opción válida')


print('----- Gracias por usar este programa -----')