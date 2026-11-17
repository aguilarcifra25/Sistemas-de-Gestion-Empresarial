import random

velocidades = []

exe = True
op = 0

for i in range(8):

    velocidades.append(round(random.uniform(10.0, 45.0),2))

print('Bienvenido a su sistema de control')

while exe is True:

    print('\nPulse 1 - Ver velocidades')
    print('Pulse 2 - Mostrar tres primeras velocidades registradas')
    print('Pulse 3 - Multar a todas las velocidades superiores a 25 km/h')
    print('Pulse 4 - Añadir velocidad manualmente')
    print('Pulse 0 - Cerrar programa\n')

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1:

            print(velocidades)

        case 2:

            print(f'Primeras tres velocidades registradas:\n{velocidades[:3]}')

        case 3:

            multas = 0

            for i in range(len(velocidades)):

                if type(velocidades[i]) == float and velocidades[i] > 25.0:

                    velocidades[i] = 'MULTADO'
                    multas += 1

            print(f'Se han registrado un total de {multas} multas nuevas.')
            
        case 4:

            pos = int(input('Indique la posición del registro donde quiere añadir la nueva velocidad: '))

            vel = float(input('Indique la nueva velocidad a añadir: '))

            velocidades.insert(pos - 1, vel)

            print('\nLa nueva velocidad se ha añadido al registro.')

        case _:

            print('Error - Elija una opción disponible')

print('--- Gracias por usar este programa ---')