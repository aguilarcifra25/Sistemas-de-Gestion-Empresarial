import numpy

jugar = 'S'
score = 0
pcScore = 0

print('Juguemos piedra papel tijeras')

while jugar == 'S':

    pcOpt = numpy.random.randint(3)
    opt = int(input('Elige 1 para piedra, 2 para papel y 3 para tijeras: '))

    match opt:

        case 1:

            match pcOpt:

                case 1:

                    print('¡Piedra vs piedra! Tenemos un empate')

                case 2:

                    print('¡Piedra vs papel! Me llevo esta ronda')
                    pcScore += 1

                case 3:

                    print('¡Piedra vs tijeras! Te llevas esta ronda')
                    score += 1

        case 2:

             match pcOpt:
            
                            case 1:
            
                                print('Papel vs piedra! Te llevas esta ronda')
                                score += 1

                            case 2:
            
                                print('¡Papel vs papel! Tenemos un empate')
            
                            case 3:
            
                                print('¡Papel vs tijeras! Me levo esta ronda')
                                pcScore += 1

        case 3:

               match pcOpt:
              
                              case 1:
              
                                    print('¡Tijeras vs piedra! Me llevo esta ronda')
                                    pcScore += 1

                              case 2:
              
                                    print('¡Tijeras vs papel! Te llevas esta ronda')
                                    score += 1
              
                              case 3:
              
                                    print('¡Tijeras vs tijeras! Tenemos un empate')

        case _:

                print('Debes introducir uno de los valores indicados.')


    print(f'La puntuación actual es: Tu -> {score}  PC -> {pcScore}')

    jugar = input('Presiona S para seguir jugando y N para dejar de jugar: ')



