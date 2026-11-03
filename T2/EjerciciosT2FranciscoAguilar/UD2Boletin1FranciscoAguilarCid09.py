numPalabras = 0
palabras = []
palabrasInvertidas = []

print('Bienvenido al programa de invertir listas de palabras\n')

numPalabras = int(input('Indique el número de palabras que quiere escribir: '))

print()

for i in range(numPalabras):

    palabras.append(input('Escriba una palabra: '))

for i in range(len(palabras) - 1, -1, -1):

    palabrasInvertidas.append(palabras[i])

print()
print(f'Lista original: {palabras}')
print(f'Lista invertida: {palabrasInvertidas}')

print('\n--- Gracias por usar este programa ---')