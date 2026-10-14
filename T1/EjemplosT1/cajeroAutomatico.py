print('\nBienvenido a su cajero automático\n')

saldo = 350.0
precioEntrada = 300.0
exe = True

while exe == True:

    print('\nSeleccione una opción:\n')

    print('Pulse 1 - Ver saldo')
    print('Pulse 2 - Retirar dinero')
    print('Pulse 3 - Comprar entradas')
    print('Pulse 4 - Ingresar dinero')
    print('Pulse 0 - Cerrar sesión\n')

    op = int(input(''))

    print('')

    match op:

        case 0:

            exe = False

        case 1:

            print(f'Su saldo es de {saldo}€.')

        case 2:

            dinero = float(input('Indique el dinero a retirar: '))

            print('')

            if saldo < dinero:

                print('Error - No se dispone de suficiente saldo')

            else:

                saldo = saldo - dinero

                print('El dinero ha sido retirado con éxito.')

        case 3:

            cant = int(input(f'Las entradas tienen un valor de {precioEntrada}€. Indique cuántas quiere comprar:'))

            totalEntradas = cant * precioEntrada

            print('')

            if totalEntradas > saldo:

                print('Error - No se dispone de suficiente saldo')

            else:

                saldo = saldo - totalEntradas

                print('Entradas compradas con éxito')

        case 4:

            dinero = float(input('Indique el dinero a ingresar: '))

            print('')

            saldo = saldo + dinero

            print('Dinero ingresado con éxito')

        case _:

            print('Error - Seleccione una opción válida')        

print('\n--- Gracias por usar nuestro banco ---\n')