numPalabras1 = 0
numPalabras2 = 0
palabras1 = []
palabras2 = []

print('Bienvenido al programa de eliminar palabras de dos listas\n')

numPalabras1 = int(input('Indique el número de palabras de la primera lista: '))

print()

for i in range(numPalabras1):

    palabras1.append(input('Escriba una palabra de la primera lista: '))

print()
numPalabras2 = int(input('Indique el número de palabras de la segunda lista: '))

print()

for i in range(numPalabras2):

    palabras2.append(input('Escriba una palabra de la segunda lista: '))

for i in range(len(palabras2)):

    while palabras2[i] in palabras1:

        palabras1.remove(palabras2[i])

print()
print(palabras1)

print('\n--- Gracias por usar este programa ---')