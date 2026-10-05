numeros = []

opt = 'S'

while opt == 'S':

    numeros.append(int(input('Añade un número: ')))

    opt = input('¿Quiere añadir otro número? (S/N): ')

print(numeros)