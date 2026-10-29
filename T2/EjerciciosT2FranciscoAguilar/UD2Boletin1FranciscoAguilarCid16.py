'''Queremos desarrollar un pequeño programa que ayude a un técnico meteorológico (mi amigo Nico es
meteorólogo) a analizar las temperaturas registradas durante una semana en su estación de trabajo.
Rellenar la lista con temperaturas generadas de forma aleatoria entre dos límites leídos por teclado. Pueden
tener decimales.
A partir de esa lista, el programa debe:
Mostrar todas las temperaturas introducidas.
Calcular y mostrar la temperatura media.
Mostrar la temperatura máxima y mínima junto con el día en que ocurrieron (día 1, día 2, no usar fechas).
Ordena la lista de mayor a menor temperatura.
Mostrar cuántos días tuvieron temperaturas por encima de la media.
Crear una nueva lista solo con las temperaturas superiores a la media.'''

import numpy

op = 0
exe = True

temps = []
tempMax = 0
tempMin = 0
cantTemp = 7

tempMedia = 0
sumaTemps = 0

tempMaxGen = 0
tempMinGen = 0
diaMax = []
diaMin = []

diasSupMedia = 0

tempsSupMedia = []

print('Bienvenido a su aistente metereológico\n')

print('Para generar los valores de prueba se necesitan dos temperaturas.')
tempMin = float(input('Indique la temperatura mínima: '))
tempMax = float(input('Indique la temperatura máxima: ')) + 1

for i in range(7):

    temps.append(round(numpy.random.uniform(tempMin,tempMax),2))

while exe is True:

    print('\nSeleccione una opción:\n')
    print('Pulse 1 - Mostrar temperaturas del sistema')
    print('Pulse 2 - Mostrar temperatura media')
    print('Pulse 3 - Mostrar días de temperaturas máx y mín')
    print('Pulse 4 - Ordenar las temperaturas de mayor a menor')
    print('Pulse 5 - Mostrar cantidad de días con temperatura superior a la media')
    print('Pulse 6 - Crear una nueva lista con las temperaturas superiores a la media')
    print('Pulse 0 - Cerrar programa\n')

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1:

            print(temps)

        case 2:

            sumaTemps = 0

            for i in range(len(temps)):

                sumaTemps = sumaTemps + temps[i]

            tempMedia = sumaTemps/len(temps)

            print(f'La temperatura media es de {tempMedia}')

        case 3: 

            tempMaxGen = temps[i]
            tempMinGen = temps[i]

            for i in range(len(temps)):

                if temps[i] > tempMaxGen:

                    tempMaxGen = temps[i]
                    

                if temps[i] < tempMinGen:

                    tempMinGen = temps[i]

            for i in range(len(temps)):

                if temps[i] == tempMaxGen:

                    diaMax.append(i+1)

                if temps[i] == tempMinGen:
                
                    diaMin.append(i+1)

            print(f'La temperatura máxima fue de {tempMaxGen} el dia(s) {diaMax} de la semana y la mínima de {tempMinGen} el dia(s) {diaMin} de la semana.')

        case 4:

            print(sorted(temps))

        case 5:

            diasSupMedia = 0

            for i in range(len(temps)):

                if temps[i] > tempMedia:

                    diasSupMedia += 1

            print(f'Hay {diasSupMedia} dia(s) que superan la temperatura media')

        case 6:

            tempsSupMedia.clear()

            for i in range(len(temps)):
            
                if temps[i] > tempMedia:

                    tempsSupMedia.append(temps[i])

            print(tempsSupMedia)

        case _: 

            print('Introduzca una opción válida')

print('\n----- Gracias por usar este programa -----')