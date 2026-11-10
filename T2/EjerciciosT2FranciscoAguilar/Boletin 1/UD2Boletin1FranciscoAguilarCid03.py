notas = []
sumaNotas = 0
mediaNotas = 0
notaMasAlta = 0
notaMasBaja = 11
numSuspensos = 0

print('Bienvenido al programa de las notas\n')


for i in range (9):

    notas.append(int(input('Indique la siguiente nota: ')))


for i in range(len(notas)):

    sumaNotas = sumaNotas + notas[i]

    if notas[i] > notaMasAlta:

        notaMasAlta = notas[i]

    if notas[i] < notaMasBaja:
    
        notaMasBaja = notas[i]

    if notas[i] < 5:

        numSuspensos += 1

mediaNotas = sumaNotas / len(notas)

print('\n')

print(f'Nota media: {mediaNotas}')
print(f'Nota más alta: {notaMasAlta}')
print(f'Nota más baja: {notaMasBaja}')
print(f'Número de suspensos: {numSuspensos}')

print('\n--- Gracias por usar este programa ---')