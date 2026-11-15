'''
Voy a alquilar una habitación de mi casa a modo de apartamento turístico y necesito un programa para gestionar lo
recaudado. Se debe usar una lista como estructura principal para guardar los datos (si hace falta alguna tupla se puede
usar). Como no hemos dado todavía objetos, lo haremos con una lista de flotantes, que será lo recaudado cada día que lo
alquilo.
El programa puede empezar creando una lista directamente con datos y luego poder hacer lo siguiente mediante un menú
en la clase Principal y debe mostrar en la misma
• Agregar una nueva recaudación.
• Poner a cero una recaudación (se me ha ido el cliente sin pagar).
• Imprimir toda la lista, es decir, mostrar todos los datos de todas las recaudaciones en bonito.
• Buscar el día en que más he ganado y decir cuántos días he ganado esa cantidad.
• Sumar una cantidad a un día como gasto extra.
• Calcular cuánto he recaudado en todas las recaudaciones.
• Ordenar la lista de mayor a menor.
• Calcular la media diaria.
• Calcular el porcentaje de días al mes (suponiendo 30 días) en que he tenido la habitación alquilada.
• Dividir la lista en dos nuevas listas. Una de ellas debe ser la que tenga las 5 menores recaudaciones, la otra las restantes.
'''
import random

exe = True
op = 0

recaudaciones = []

for i in range(29):

    recaudaciones.append(round(random.uniform(0.0,200.0),2))

print('Bienvenido a tu programa de recaudación')

while exe is True:

    print('\nSeleccione una opción:\n')
    print('Pulse 1 - Agregar nueva recaudación')
    print('Pulse 2 - Poner a 0 una recaudación')
    print('Pulse 3 - Imprimir recaudaciones')
    print('Pulse 4 - Buscar día de más beneficio')
    print('Pulse 5 - Sumar gasto extra a un día concreto')
    print('Pulse 6 - Calcular recaudación total')
    print('Pulse 7 - Ordenar lista de mayor a menor')
    print('Pulse 8 - Calcular media diaria')
    print('Pulse 9 - Calcular porcentaje de días al mes con la habitación alquilada')
    print('Pulse 10 -Dividir la lista sacando las 5 menores recaudaciones')
    print('Pulse 0 - Cerrar programa\n')

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1:

            newRecaudacion = float(input('Indique la cantidad a sumar: '))

            recaudaciones.append(newRecaudacion)

        case 2:

            pos = int(input('Indique que recaudación quiere poner a 0 (su posición)'))

            recaudaciones[pos-1] = 0

        case 3:

            print(recaudaciones)

        case 4:

            maxRecaudado = max(recaudaciones)
            diasMaxRecaudado = []

            for i in range(len(recaudaciones)):

                if maxRecaudado == recaudaciones[i]:

                    diasMaxRecaudado.append(i + 1)

            print(f'Estos fueron los día(s) de mayor recaudación: {diasMaxRecaudado}')

        case 5:

            dia = int(input('Indique el día al que sumar el gasto: '))
            print()

            gasto = float(input('¿De cuánto es el gasto? '))

            recaudaciones[dia - 1] = recaudaciones[dia - 1] - gasto

        case 6:

            print(f'La recaudación total es de {sum(recaudaciones)}')

        case 7:

            recaudaciones = sorted(recaudaciones, reverse=True)

            print(recaudaciones)

        case 8:

            media = sum(recaudaciones)/len(recaudaciones)

            print(f'La media diaria es de {media:.2f}')

        case 9:

            diasSinRecaudar = 0

            for i in recaudaciones:

                if i == 0:

                    diasSinRecaudar += 1

            porcentajeDias = ((len(recaudaciones) - diasSinRecaudar) * 100) / 30

            print(f'El porcentaje de días con la habitación alquilada es del {porcentajeDias:.2f}%')

        case 10:

            menorRecaudaciones = sorted(recaudaciones)

            recaudaciones = menorRecaudaciones[5:]

            menorRecaudaciones = menorRecaudaciones[:5]

            print(f'Menor recaudaciones: {menorRecaudaciones}')
            print(f'Recaudaciones: {recaudaciones}')

        case _:

            print('ERROR - Seleccione una opción válida')

print('--- Gracias por usar este programa ---')