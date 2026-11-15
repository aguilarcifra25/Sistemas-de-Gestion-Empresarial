'''
Si tenemos los dos conjuntos de alumnos siguientes:
claseA = {"Ana", "Luis", "Pedro"}
claseB = {"María", "Luis", "Sofía"}
Apartados
1. Mostrar los alumnos de ambas clases (unión).
2. Mostrar los alumnos comunes (intersección).
3. Mostrar alumnos solo de claseA.
4. Añadir “Carlos” a claseB
'''

exe = True
op = 0

claseA = {"Ana", "Luis", "Pedro"}
claseB = {"María", "Luis", "Sofía"}

print('Bienvenido al programa de las clases\n')

while exe is True:

    print('\nPulse 1 - Mostrar los alumnos de ambas clases (unión)')
    print('Pulse 2 - Mostrar los alumnos de comunes (intersección)')
    print('Pulse 3 - Mostrar alumnos solo de clase A')
    print('Pulse 4 - Añadir "Carlos" a clase B')
    print('Pulse 0 - Cerrar programa\n')

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1:

            print(claseA.union(claseB))

        case 2:

           print(claseA.intersection(claseB))

        case 3:

            print(claseA)

        case 4:

            claseB.add('Carlos')

            print(claseB)

        case _:

            print('ERROR - Seleccione una opción válida')

print('--- Gracias por usar este programa ---')