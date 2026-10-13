print('Bienvenido a su calculadora')

exe = True

while exe:

    print('\nIndique una opción: ')

    print('Pulse 1 - Sumar')
    print('Pulse 2 - Restar')
    print('Pulse 3 - Multiplicar')
    print('Pulse 4 - Dividir')
    print('Pulse 0 - Cerrar programa')

    op = int(input('\n'))

    match op:

        case 1:

            num1 = float(input('Indique un número: '))

            num2 = float(input('Indique otro número: '))

            print(f'El resultado es {num1 + num2}')

        case 2:

            num1 = float(input('Indique un número: '))
            
            num2 = float(input('Indique otro número: '))
            
            print(f'El resultado es {num1 - num2}')

        case 3:
        
            num1 = float(input('Indique un número: '))
                    
            num2 = float(input('Indique otro número: '))
                    
            print(f'El resultado es {num1 * num2}')

        case 4:
        
            num1 = float(input('Indique un número: '))
                    
            num2 = float(input('Indique otro número: '))
                    
            print(f'El resultado es {num1 / num2}')

        case 0:

            exe = False

        case _:

            print('Introduzca una opción válida')

print('\n-- Gracias por usar este programa --\n')