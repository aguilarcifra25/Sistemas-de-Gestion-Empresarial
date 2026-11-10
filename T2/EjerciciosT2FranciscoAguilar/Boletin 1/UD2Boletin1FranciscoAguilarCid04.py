numPalabras = 0
palabras = []

print('Bienvenido al programa de escribir palabras\n')

numPalabras = int(input('Indique el número de palabras ququiere escribir: '))

print()

for i in range(numPalabras):

    palabras.append(input('Escriba una palabra: '))


print()
print(palabras)

print('\n--- Gracias por usar este programa ---')