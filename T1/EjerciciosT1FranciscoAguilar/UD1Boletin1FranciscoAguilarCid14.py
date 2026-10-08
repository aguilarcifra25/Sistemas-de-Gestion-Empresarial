piso = '*'

print('Bienvenido al generador de triángulos\n')

num = int(input('Introduce un número:'))

for i in range(num):

    print(piso)

    piso = piso + '*'

for i in range(num -1, 0, -1):

    print('*' * i)
