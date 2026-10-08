import numpy as np

num = np.random.randint(10)
guess = 0

for i in range (0,3):

    guess = int(input('Di un número: '))

    if guess < num:

        print('Estoy pensando en un número mayor')

    elif guess > num:

        print('Estoy pensando en un número menor')

    elif guess == num:

        print('¡Has acertado!')

        i = 3

print(f'\nEl número era el {num}')