preciosArt = []
cantVendidaArt = []
sucursales = []
j = 0

exe = True
op = 0

print('Bienvenido al programa de información de artículos')

print('\nIndique el precio de los artículos:\n')

for i in range(5):

    preciosArt.append(float(input(f'Indica el precio del artículo {i + 1}: ')))

print('\nIndique la cantidad vendida de cada artículo en cada sucursal:\n')

while j < 4:

    for i in range(5):

        cantVendidaArt.append(int(input(f'Indica la cantidad vendida del artículo {i+1} en la sucursal {j + 1}: ')))

    sucursales.append(cantVendidaArt.copy())
    cantVendidaArt.clear()

    j += 1

while exe is True:

    print('\nSeleccione una opción: \n')

    print('Pulse 1 - Ver cantidades de cada artículo')
    print('Pulse 2 - Cantidad de artículos de la sucursal 2')
    print('Pulse 3 - Cantidad del artículo 3 en la sucursal 1')
    print('Pulse 4 - Recaudación total de cada sucursal')
    print('Pulse 5 - Recaudación total de la empresa')
    print('Pulse 6 - Sucursal de mayor recaudación')
    print('Pulse 0 - Cerrar programa\n')

    op = int(input(''))

    print()

    match op:

        case 0:

            exe = False

        case 1: 

            cantArt = 0

            cantArtTotal = []


            for j in range(5):

                for i in range(len(sucursales)):

                    cantArt += sucursales[j][i]

                cantArtTotal.append(cantArt)

            print('Las cantidades son:' + 
                  f'- Artículo 1: {cantArtTotal[0]}'
                  f'- Artículo 2: {cantArtTotal[1]}'
                  f'- Artículo 3: {cantArtTotal[2]}'
                  f'- Artículo 4: {cantArtTotal[3]}'
                  f'- Artículo 5: {cantArtTotal[4]}')








