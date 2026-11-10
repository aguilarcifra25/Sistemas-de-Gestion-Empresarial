palabra = ""
palabraInvertida = ""

print('Bienvenido al comprobador de palíndromos\n')

palabra = input('Escriba una palabra: ')

palabra = palabra.lower()

for i in range(len(palabra) - 1, -1, -1):

    palabraInvertida += palabra[i]

print()

if palabra == palabraInvertida:

    print(f'La palabra "{palabra}" es un palíndromo.')

else:

    print(f'La palabra "{palabra}" es un palíndromo.')


print('\n--- Gracias por usar este programa ---')