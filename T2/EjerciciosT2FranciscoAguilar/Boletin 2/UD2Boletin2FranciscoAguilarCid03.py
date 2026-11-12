'''
3. Crear un diccionario que tenga como claves el dni de un estudiante y como valor la nota media de su
expediente. La nota media se generará de manera aleatoria entre 1 y 10.
Escribir el código necesario en un menú para hacer los siguiente:
a) Mostrar los datos.
b) Modificar la nota.
c) Añadir un nuevo estudiante.
d) Crear un nuevo diccionario (no modificar el original) solo con los estudiantes que tienen nota media
mayor a un valor dado por teclado (por ejemplo, para comprobar que pueden entrar en un ciclo según esa
nota de corte).
'''

import random

exe = True
op = 0

estudiantes = {}
dnis = ['12345678A', '23456789B', '34567890C', '45678901D', '56789012E']

estudiantesAdmitidos = {}

dni = ''
nuevaNota = 0.0
notaCorte = 0.0

for i in range(len(dnis)):

    estudiantes[dnis[i]] = round(random.uniform(1, 10), 2)

print('Bienvenido al programa de notas medias de estudiantes')

while exe is True:

    print()

    print('Pulse 1 - Mostrar los datos')
    print('Pulse 2 - Modificar la nota')
    print('Pulse 3 - Añadir un nuevo estudiante')
    print('Pulse 4 - Crear un diccionario con los estudiantes por encima de una nota de corte')
    print('Pulse 0 - Cerrar el programa')

    print()

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1:

            print(estudiantes)

        case 2:

            dni = input('Indique el DNI del estudiante: ')

            if dni in estudiantes:

                nuevaNota = float(input('Indique la nueva nota media (1 - 10): '))

                if nuevaNota >= 1 and nuevaNota <= 10:

                    estudiantes[dni] = nuevaNota

                    print(f'\nNota modificada: DNI {dni} - Nota media: {estudiantes[dni]}')

                else:

                    print('ERROR - La nota debe estar entre 1 y 10')

            else:

                print('ERROR - No existe ningún estudiante con ese DNI')

        case 3:

            dni = input('Indique el DNI del nuevo estudiante: ')

            if dni in estudiantes:

                print('ERROR - Ya existe un estudiante con ese DNI')

            else:

                estudiantes[dni] = round(random.uniform(1, 10), 2)

                print(f'\nEstudiante añadido: DNI {dni} - Nota media: {estudiantes[dni]}')

        case 4:

            notaCorte = float(input('Indique la nota de corte: '))

            estudiantesAdmitidos = {}

            for clave in estudiantes:

                if estudiantes[clave] > notaCorte:

                    estudiantesAdmitidos[clave] = estudiantes[clave]

            print()

            if len(estudiantesAdmitidos) == 0:

                print('Ningún estudiante supera la nota de corte')

            else:

                print(f'Estudiantes con nota media mayor que {notaCorte}:\n')

                for clave in estudiantesAdmitidos:

                    print(f'DNI: {clave} - Nota media: {estudiantesAdmitidos[clave]}')

        case _:

            print('ERROR - Seleccione una opción válida')

print('\n--- Gracias por usar este programa ---')