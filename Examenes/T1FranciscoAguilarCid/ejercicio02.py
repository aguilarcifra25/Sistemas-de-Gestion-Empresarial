

print('Bienvenido al analizador de cadenas de texto')

exe = True
op = 0

frase = ''
contMayus = 0
contExclamacion = 0
longitud = 0
porcentajeMayus = 0

while exe:

    print('\nSeleccione una opción: ')

    print('Pulse 1 - Detector de entusiasmo y spam')
    print('Pulse 0 - Salir del programa\n')

    op = int(input(''))

    print('')

    match op:

        case 1:

            frase = input('Indique la frase/mensaje a analizar: ')

            for letra in frase:

                if letra.isupper():

                    contMayus += 1

                if letra == '!':

                    contExclamacion += 1

            longitud = len(frase)

            porcentajeMayus = (contMayus * 100) / longitud

            print('')

            if porcentajeMayus > 50 or contExclamacion > 3:

                print('ALERTA - El compañero está gritando o en modo pánico')

            else:

                print('Mensaje con nivel de estrés aceptable')

        case 0:

            exe = False

        case _:

            print('ERROR - Seleccione una opción válida')

print('\n--- Gracias por usar este programa ---')