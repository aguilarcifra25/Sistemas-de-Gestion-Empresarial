numPalabras1 = 0
numPalabras2 = 0
palabras1 = []
palabras2 = []

todasLasPalabras = []
soloPrimera = []
soloSegunda = []
enAmbas = []

print('Bienvenido al programa comparador de listas\n')

numPalabras1 = int(input('Indique el número de palabras de la primera lista: '))

print()


for i in range(numPalabras1):

    palabras1.append(input('Escriba una palabra de la primera lista: '))

print()

numPalabras2 = int(input('Indique el número de palabras de la segunda lista: '))


print()

for i in range(numPalabras2):

    palabras2.append(input('Escriba una palabra de la segunda lista: '))



for i in range(len(palabras1)):

    if palabras1[i] not in todasLasPalabras:

        todasLasPalabras.append(palabras1[i])

for i in range(len(palabras2)):

    if palabras2[i] not in todasLasPalabras:

        todasLasPalabras.append(palabras2[i])



for i in range(len(palabras1)):

    if palabras1[i] not in palabras2 and palabras1[i] not in soloPrimera:

        soloPrimera.append(palabras1[i])



for i in range(len(palabras2)):

    if palabras2[i] not in palabras1 and palabras2[i] not in soloSegunda:

        soloSegunda.append(palabras2[i])



for i in range(len(palabras1)):

    if palabras1[i] in palabras2 and palabras1[i] not in enAmbas:

        enAmbas.append(palabras1[i])


print('\nResultados:\n')
print(f'Palabras que aparecen en las dos listas: {todasLasPalabras}')
print(f'Palabras solo en la primera lista: {soloPrimera}')
print(f'Palabras solo en la segunda lista: {soloSegunda}')
print(f'Palabras que aparecen en ambas listas: {enAmbas}')

print('\n--- Gracias por usar este programa ---')