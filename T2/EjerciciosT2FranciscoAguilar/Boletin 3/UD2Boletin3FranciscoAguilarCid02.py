'''
Estoy dando clases de inglés para el B2 y me gustaría que me ayudarais a crear un diccionario para ver cómo
se dicen palabras con significado “raro” españolas en inglés. Se hará todo en el mismo archivo, no se crean
clases. Por ejemplo, “Cabeza: (en el sur de España) amigo/colega”, aro: sí, de acuerdo. Consideraremos que
no se repiten palabras con el mismo nombre, es decir, que la palabra “take” no aparece dos veces en el
diccionario y que, si tiene varios significados, estos pueden ir en el mismo String “significado”, por ejemplo,
for---->por, para, durante.
Se debe utilizar un diccionario que se puede instanciar con algunos elementos de inicio y un menú para cada
uno de las siguientes funcionalidades:
• Agregar una nueva palabra por teclado.
• Imprimir el diccionario completo “en bonito”.
• Buscar una palabra por nombre y mostrar su significado evitando que salta un error si la palabra no se
encuentra.
• Modificar una palabra, modificando únicamente el significado de esta por otro nuevo, leído por
teclado.
• Pedir al usuario sus dos palabras favoritas con los significados y combinar este con el ya creado
modificando el original.
• Borrar una palabra (ustedes decidís la mejor forma).
• Ordenar el diccionario por orden alfabético.
'''

exe = True
op = 0

diccionario = {
    "variable": "A box where we store data to use later in the program.",
    "loop": "An instruction to repeat a task automatically multiple times.",
    "function": "A small block of code that performs a specific task and can be reused.",
    "class": "A blueprint or template used to create objects with shared properties and actions.",
    "database": "An organized place to store large amounts of information securely."
}

print('Bienvenido a tu diccionario\n')

while exe is True:

    print('\nSeleccione una opción:\n')
    print('Pulse 1 - Agregar una nueva palabra')
    print('Pulse 2 - Imprimir el diccionario completo "en bonito"')
    print('Pulse 3 - Buscar una palabra por nombre y ver su significado')
    print('Pulse 4 - Modificar el significado de una palabra')
    print('Pulse 5 - Combinar palabras favoritas con el diccionario')
    print('Pulse 6 - Borrar una palabra')
    print('Pulse 7 - Ordenar el diccionario por orden alfabético')
    print('Pulse 0 - Cerrar programa\n')

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1:

            palabra = input('Indica la palabra: ')
            significado = input('Indica su significado: ')

            diccionario[palabra] = significado

        case 2:

            for palabra, significado in diccionario.items():

                print(palabra, '-->', significado)

        case 3:

            busqueda = input('Indica la palabra que buscas: ')

            print()

            if busqueda in diccionario.keys():

                print(f'{busqueda} --> {diccionario.get(busqueda)}')

            else:

                print('No hay registros de esa palabra')

        case 4:

            palabra = input('Indica la palabra que quieres cambiar: ')

            if palabra in diccionario.keys():

                significado = input('Indica su nuevo significado: ')

                diccionario[palabra] = significado

            else:

                print('No hay registros de esa palabra')

        case 5:

            favoritas = {}

            for i in range(2):

                palabra = input('Indica una de tus palabras favoritas: ')
                significado = input('Indica su significado: ')

                favoritas[palabra] = significado

            diccionario.update(favoritas)
                
        case 6:

            palabra = input('Indique la palabra a borrar: ')

            if palabra in diccionario.keys():

                diccionario.pop(palabra)

            else:

                print('No hay registros de esa palabra')

        case 7:

            diccionario = dict(sorted(diccionario.items()))

        case _:

            print('ERROR - Seleccione una opción válida')

print('--- Gracias por usar este programa ---')