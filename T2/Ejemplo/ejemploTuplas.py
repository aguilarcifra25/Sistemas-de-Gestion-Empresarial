print('Bienvenido al programa para aprender sobre tuplas')

exe = True
exe3 = True

op = 0
op3 = 0

while exe is True:

    print('\nSeleccione una opción: \n')

    print('Pulse 1 - Crear tuplas')
    print('Pulse 2 - Convertir a tupla')
    print('Pulse 3 - Desempaquetado de tuplas')
    print('Pulse 4 - Tuplas vs listas')
    print('Pulse 0 - Cerrar programa\n')

    op = int(input(''))
    exe3 = True
    
    print()

    match op:

        case 0:

            exe = False

        case 1:

            print('''Podemos pensar en crear tuplas tal y como lo hacíamos con listas, pero usando paréntesis en lugar de corchetes:\n
            >>> empty_tuple = ()
            >>> one_item_tuple = ( Papá Noel ,)
            >>> tenerife_geoloc = (28.46824, -16.25462)
            >>> three_wise_men = ( Melchor , Gaspar , Baltasar )''')

        case 2:

            print('''Para convertir otros tipos de datos en una tupla podemos usar la función tuple():\n
            >>> shopping = [ Agua , Aceite , Arroz ]
            >>> tuple(shopping)
            ( Agua , Aceite , Arroz )''')

        case 3:

            while exe3 is True:
            
                print('\nSeleccione una opción: \n')
                
                print('Pulse 1 - Explicación general')
                print('Pulse 2 - Divmod()')
                print('Pulse 3 - Intercambio de valores')
                print('Pulse 4 - Desempaquetado extendido')
                print('Pulse 5 - Desempaquetado genérico')
                print('Pulse 0 - Volver al menú principal\n')

                op3 = int(input(''))

                print()

                match op3:

                    case 0:

                        exe3 = False

                    case 1:

                        print('''El desempaquetado es una característica de las tuplas que nos permite asignar una tupla a variables independientes:\n
                        three_wise_men = ( Melchor , Gaspar , Baltasar )
                        >>> king1, king2, king3 = three_wise_men
                        >>> king1
                        Melchor
                        >>> king2
                        Gaspar
                        >>> king3
                        Baltasar''')

                    case 2:

                        print('''Python proporciona la función «built-in» divmod() que devuelve el cociente y el resto de una división usando una única llamada. 
                        Lo interesante (para el caso que nos ocupa) es que se suele utilizar el desempaquetado de tuplas para obtener los valores:\n
                        >>> quotient, remainder = divmod(7, 3)
                        >>> quotient
                        2
                        >>> remainder
                        1''')

                    case 3:

                        print('''A través del desempaquetado de tuplas podemos llevar a cabo el intercambio de los valores de dos variables de manera directa:\n
                        >>> value1 = 40
                        >>> value2 = 20
                        >>> value1, value2 = value2, value1
                        >>> value1
                        20
                        >>> value2
                        40''')

                    case 4:

                        print('''No tenemos que ceñirnos a realizar desempaquetado uno a uno. También podemos extenderlo
                        e indicar ciertos «grupos» de elementos mediante el operador *. Veamos un ejemplo:\n
                        >>> ranking = ( G , A , R , Y , W )
                        >>> head, *body, tail = ranking
                        >>> head
                        G
                        >>> body
                        [ A , R , Y ]
                        >>> tail
                        W''')

                    case 5:

                        print('''El desempaquetado de tuplas es extensible a cualquier tipo de datos que sea iterable. Veamos algunos ejemplos de ello.\n
                        Sobre cadenas de texto:\n
                        >>> oxygen = O2
                        >>> first, last = oxygen
                        >>> first, last
                        ( O , 2 )
                        >>> text = Hello, World!
                        >>> head, *body, tail = text
                        >>> head, body, tail
                        ( H , [ e , l , l , o , , , , W , o , r , l , d ], ! )\n
                        Sobre listas:\n
                        >>> writer1, writer2, writer3 = [ Virginia Woolf , Jane Austen , Mary Shelley ]
                        >>> writer1, writer2, writer3
                        ( Virginia Woolf , Jane Austen , Mary Shelley )
                        >>> text = Hello, World!
                        >>> word1, word2 = text.split()
                        >>> word1, word2
                        ( Hello, , World! )''')

                    case _:

                        print('ERROR - Seleccione una opción disponible')

        case 4:

            print('''Aunque puedan parecer estructuras de datos muy similares, sabemos que las tuplas carecen de ciertas operaciones, especialmente las que 
            tienen que ver con la modificación de sus valores, ya que no son inmutables. Si las listas son más flexibles y potentes, ¿por qué íbamos a
            necesitar tuplas? Veamos 4 potenciales ventajas del uso de tuplas frente a las listas:\n
            1. Las tuplas ocupan menos espacio en memoria.
            2. En las tuplas existe protección frente a cambios indeseados.
            3. Las tuplas se pueden usar como claves de diccionarios (son «hashables»).
            4. Las namedtuples son una alternativa sencilla a los objetos.''')

        case _:

            print('ERROR - Seleccione una opción disponible')

print('\n--- Gracias por usar este programa ---')