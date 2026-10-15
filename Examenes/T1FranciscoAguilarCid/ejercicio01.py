exe = True
op = 0

dinero = 0.0
cantDiaria = 1.0
totalSemana = 0.0
dineroFinal = 0.0

cantCafes = 0

print('Bienvenido a su gestor de finanzas y supervivencia básica')

while exe:

    print('\nSeleccione una opción: \n')

    print('Pulse 1 - Calculadora de presupuesto de supervivencia semanal')
    print('Pulse 2 - Diagnóstico cafetería')
    print('Pulse 0 - Cerrar programa\n')

    op = int(input(''))

    print('')

    match op:

        case 1:

            dinero = float(input('Indique cuánto dinero a la semana tiene para gastar en cafetería: '))

            print('\nA continuación introduzca sus gastos diarios (introduzca un valor negativo para terminar esta operación.)\n')

            while cantDiaria > 0:

                cantDiaria = float(input('Introduzca una cantidad: '))

                if cantDiaria > 0:

                    totalSemana = totalSemana + cantDiaria

            dineroFinal = dinero - totalSemana

            print('')

            if  dineroFinal > 0:

                print(f'Su gasto total es de {totalSemana}, sobrando un total de {dineroFinal} del presupuesto inicial.')
            
            else:

                print(f'ALERTA - El balance final es de {dineroFinal}, debe reducir sus gastos actuales ({totalSemana})')

        case 2:

            cantCafes = int(input('Indique cuántas taza de café ha tomado hoy: '))

            print('\nSu categoría es:')

            if cantCafes >= 0 and cantCafes <= 1:

                print('Modo Zombi')

            elif cantCafes > 1 and cantCafes < 5:

                print('Rendimiento óptimo')

            else: 

                print('Viendo el código en 4D / Taquicardia')


            print('')

            for i in range(cantCafes):

                print('¡Atacao!')

        case 0:

            exe = False

        case _:

            print('ERROR - Seleccione una opción válida')


print('\n--- Gracias por usar este programa ---')