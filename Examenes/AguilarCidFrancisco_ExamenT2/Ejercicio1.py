exe = True
op = 0

telefonos = {
    '123 45 67 89' : 'Mamá',
    '987 65 43 21' : 'Luisito'
}

historico = {}

print('Bienvenido a su agenda telefónica')

while exe is True:

    print('\nPulse 1 - Modificar un valor / Añadir número')
    print('Pulse 2 - Buscar número')
    print('Pulse 3 - Mostrar cuántas veces aparece un nombre en la agenda')
    print('Pulse 4 - Mostrar agenda completa')
    print('Pulse 5 - Borrar número')
    print('Pulse 6 - Ver histórico de borrados')
    print('Pulse 0 - Cerrar programa\n')

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1:

            print('Proporcione los datos necesarios. Si no tiene guardado el número proporcionado se añadirá a la agenda.\n')

            nuevoTel = input('Indique el número de teléfono: ')

            nuevoContacto = input('Indique el nombre del contacto: ')

            telefonos[nuevoTel] = nuevoContacto

            print('\nSe ha guardado el contacto con éxito.')

        case 2:

            buscarNum = input('Indique el número para realizar la búsqueda: ')

            print()

            if buscarNum in telefonos.keys():

                contacto = telefonos.get(buscarNum)

                print(f'Resultado:\n{buscarNum} --> {contacto}')

            else:

                print('Error - El número no se encuentraen la agenda')

        case 3:

            coincidencias = 0
            buscarContacto = input('Indique el nombre de la persona que busca: ')

            for contacto in telefonos.values():

                if contacto == buscarContacto:

                    coincidencias += 1

            print(f'\nEl contacto tiene un total de {coincidencias} coincidencia(s).')

        case 4:

            for num,contacto in telefonos.items():

                print(f'{num} --> {contacto}')

        case 5:

            telBorrar = input('Indique el número que quiere borrar: ')

            print()

            if telBorrar in telefonos:

                historico[telBorrar] = telefonos.get(telBorrar)

                telefonos.pop(telBorrar)

                print('El número se ha borrado con éxito')

            else:

                print('Error - No tiene ese número guardado')

        case 6:

            if len(historico) > 0:

                for num,contacto in historico.items():
                
                    print(f'{num} --> {contacto}')

            else:

                print('Nunca se ha borrado un número')

        case _:

            print('Error - Elija una opción válida')


print('\n--- Gracias por usar este programa ---')