numPalabras = 0
palabras = []

print('Bienvenido al programa para ordenar listas de palabras\n')

numPalabras = int(input('Indique el número de palabras de la lista: '))

print()

for i in range(numPalabras):

    palabras.append(input('Escriba una palabra: '))

palabras.sort()

print('\nLista de palabras ordenada alfabéticamente:')
print(palabras)

print('\n--- Gracias por usar este programa ---')