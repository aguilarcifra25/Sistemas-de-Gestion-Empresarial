numPalabras = 0
palabras = []

palabraEliminar = ''

print('Bienvenido al programa de eliminar palabras\n')

numPalabras = int(input('Indique el número de palabras que quiere escribir: '))

print()

for i in range(numPalabras):

    palabras.append(input('Escriba una palabra: '))

print()
palabraEliminar = input('Indique la palabra a eliminar: ')

while palabraEliminar in palabras:

    palabras.remove(palabraEliminar)

print()
print(palabras)

print('\n--- Gracias por usar este programa ---')