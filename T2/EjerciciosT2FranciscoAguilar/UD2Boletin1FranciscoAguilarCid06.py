numPalabras = 0
palabras = []

palabraSustituta = ''
palabraSustituida = ''

print('Bienvenido al programa de contar palabras\n')

numPalabras = int(input('Indique el número de palabras quequiere escribir: '))

print()

for i in range(numPalabras):

    palabras.append(input('Escriba una palabra: '))

print()
palabraSustituta = input('Indique la palabra sustituta: ')
palabraSustituida = input('Indique la palabra sustituida: ')

for i in range(numPalabras):

    if palabraSustituida == palabras[i]:

        palabras[i] = palabraSustituta

print()
print(palabras)