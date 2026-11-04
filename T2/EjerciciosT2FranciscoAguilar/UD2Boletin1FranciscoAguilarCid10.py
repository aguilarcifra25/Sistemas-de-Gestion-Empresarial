numPalabras = 0
palabras = []
palabrasUnicas = []

print('Bienvenido al programa de eliminar palabras repetidas\n')

numPalabras = int(input('Indique el número de palabras de la lista: '))

print()

for i in range(numPalabras):

    palabras.append(input('Escriba una palabra: '))

print('\nLista original:')
print(palabras)

for i in range(len(palabras)):

    if palabras[i] not in palabrasUnicas:

        palabrasUnicas.append(palabras[i])

palabras = palabrasUnicas

print('\nLista sin elementos repetidos:')
print(palabras)

print('\n--- Gracias por usar este programa ---')