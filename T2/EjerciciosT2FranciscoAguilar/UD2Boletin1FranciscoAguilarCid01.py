print('Bienvenido al programa de los números negativos\n')


numList = []

rep = int(input('¿Cuántos números quiere tener? '))

for i in range(rep):

    numList.append(int(input('Indique un número: ')))

    if numList[i] < 0:

        numList[i] = 0

print()
print(numList)

print('\n--- Gracias por usar este programa ---')