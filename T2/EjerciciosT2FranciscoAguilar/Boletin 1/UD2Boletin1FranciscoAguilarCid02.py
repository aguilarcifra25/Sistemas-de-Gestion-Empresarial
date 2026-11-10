print('Bienvenido al programa para aprender sobre listas')

numList = [1,2,3,4,5,6,7,8,9,10]

exe = True
exe3 = True

op = 0
op3 = 0

while exe is True:

    print('\nSeleccione una opción: \n')

    print('Pulse 1 - Crear listas')
    print('Pulse 2 - Conversión de listas')
    print('Pulse 3 - Operaciones con listas')
    print('Pulse 0 - Cerrar programa\n')

    op = int(input(''))
    exe3 = True
    
    print()

    match op:

        case 0:

            exe = False

        case 1:

            print('Podemos crear una lista de las formas:\n\nlista = [];\nnumList = [1,2,3,4,5,6,7,8,9,10];\nlanguages = [ \'Python\', \'Ruby\' , \'Javascript\' ];\n' \
            'data = [ \'Tenerife\' , { \'cielo\' : \'limpio\' , \'temp\' : 24}, 3718, (28.2933947, -16.5226597)] ')

        case 2:

            print('Podemos convertir distintos elementos a una lista:\n\nVacío -> list() -> [];\nStrings -> list(\'Python\') -> [ \'P\' , \'y\' , \'t\', \'h\' , \'o\' , \'n\' ];\n' \
            'Rangos -> list(range(10)) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')

        case 3:

            while exe3 is True:

                print('\nSeleccione una opción: \n')
                
                print('Pulse 1 - Obtener elementos')
                print('Pulse 2 - Trocear')
                print('Pulse 3 - Invertir')
                print('Pulse 4 - Añadir al final')
                print('Pulse 5 - Añadir en cualquier posición')
                print('Pulse 6 - Combinar')
                print('Pulse 7 - Modificar')
                print('Pulse 8 - Borrar')
                print('Pulse 9 - Buscar')
                print('Pulse 10 - Ordenar')
                print('Pulse 0 - Volver al menú principal\n')

                op3 = int(input(''))

                print()

                match op3:

                    case 0:

                        exe3 = False

                    case 1:

                        print('Podemos obtener un elemento de una lista a través del índice (lugar) que ocupa -> shopping = [ Agua , Huevos , Aceite ] :\n\n' \
                        'shopping[0] -> Agua;\n' \
                        'shopping[-1] -> Aceite')

                    case 2:

                        print('Podemos trocear una lista igual que haciamos con las cadenas -> shopping = [ Agua , Huevos , Aceite , Sal , Limón ]:\n\n' \
                        'shopping[0:3] -> [ Agua , Huevos , Aceite ]')

                    case 3:

                        print('Podemos invertir la lista de dos formas -> shopping = [ Agua , Huevos , Aceite , Sal , Limón ]:\n\n' \
                        'list(reversed(shopping)) -> [ Limón , Sal , Aceite , Huevos , Agua ] (Esto NO modifica la lista)\n' \
                        'shopping.reverse() -> [ Limón , Sal , Aceite , Huevos , Agua ] (Esto SI modifica la lista)')

                    case 4:

                        print('Podemos agregar un elemento al final con append -> shopping = [ Agua , Huevos , Aceite ] :\n\n' \
                        'shopping.append( Atún ) -> [ Agua , Huevos , Aceite , Atún ]')

                    case 5:

                        print('Podemos agregar un elemento encualquier posición con el uso de insert -> shopping = [ Agua , Huevos , Aceite ] :\n\n' \
                        'shopping.insert(1, Jamón ) -> [ Agua , Jamón , Huevos , Aceite ]')

                    case 6:

                        print('Podemos combinar listas con + y += -> shopping = [ Agua , Huevos , Aceite ]  fruitshop = [ Naranja , Manzana , Piña ] : \n\n' \
                        'shopping.extend(fruitshop) -> [ Agua , Huevos , Aceite , Naranja , Manzana , Piña ]')

                    case 7:

                        print('Del mismo modo que se accede a un elemento utilizando su índice, también podemos modificarlo -> shopping = [ Agua , Huevos , Aceite ] : \n\n' \
                        'shopping[0] = Jugo -> [ Jugo , Huevos , Aceite ]')

                    case 8:

                        print('Podemos hacer borrados por índice, valor, rango o de forma completa -> shopping = [ Agua , Huevos , Aceite , Sal , Limón ] : \n\n' \
                        'Por su índice: shopping.pop() #Dentro podemos poner un indice concreto -> [ Agua , Huevos , Aceite , Sal ]\n' \
                        'Por su valor: shopping.remove( Sal ) -> [ Agua , Huevos , Aceite , Limón ]\n' \
                        'Por rango: shopping[1:4] = [] -> [ Agua , Limón ]\n' \
                        'Completo: shopping.clear() ó shopping = []')

                    case 9:

                        print('Podemos buscar un elemento para saber su posición -> shopping = [ Agua , Huevos , Aceite , Sal , Limón ] : \n\n' \
                        'shopping.index( Huevos ) -> 1')

                    case 10:

                        print('Podemos ordenar una lista con el metodo sorted -> shopping = [ Agua , Huevos , Aceite , Sal , Limón ] : \n\n' \
                        'sorted(shopping) -> [ Aceite , Agua , Huevos , Limón , Sal ]')
                    
        case _:

            print('ERROR - Seleccione una opción')


print('\n--- Gracias por usar este programa ---')