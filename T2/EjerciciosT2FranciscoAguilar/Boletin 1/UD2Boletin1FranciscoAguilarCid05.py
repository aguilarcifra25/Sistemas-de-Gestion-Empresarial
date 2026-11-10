numPalabras = 0
palabras = []

checkPalabra = ''
contCheckPalabra = 0

print('Bienvenido al programa de contar palabras\n')

numPalabras = int(input('Indique el número de palabras ququiere escribir: '))

print()

for i in range(numPalabras):

    palabras.append(input('Escriba una palabra: '))

print()
checkPalabra = input('Indique la palabra a comprobar: ')

for i in range (numPalabras):

    if palabras[i] == checkPalabra:

        contCheckPalabra += 1

print(f'\nSu palabra aparece {contCheckPalabra} veces')

print('\n--- Gracias por usar este programa ---')