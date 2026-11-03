numPalabras = 0
palabras = []

palabraSustituida = ''
palabraSustituta = ''

print('Bienvenido al programa de sustituir palabras\n')

numPalabras = int(input('Indique el número de palabras que quiere escribir: '))

print()

for i in range(numPalabras):

    palabras.append(input('Escriba una palabra: '))

print()
palabraSustituida = input('Indique la palabra a sustituir: ')
palabraSustituta = input('Indique la palabra sustituta: ')

for i in range(numPalabras):

    if palabras[i] == palabraSustituida:

        palabras[i] = palabraSustituta

print()
print(palabras)

print('\n--- Gracias por usar este programa ---')