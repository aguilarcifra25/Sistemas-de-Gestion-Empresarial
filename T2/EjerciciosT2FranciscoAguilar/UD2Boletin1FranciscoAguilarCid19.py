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

        cantVendidaArt.append(int(input(f'Indica la cantidad vendida del artículo {i + 1} en la sucursal {j + 1}: ')))

    sucursales.append(cantVendidaArt.copy())
    cantVendidaArt.clear()

    j += 1

while exe is True:

    print('\nSeleccione una opción: \n')

    print('Pulse 1 - Ver cantidades totales de cada artículo')
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

            cantArtTotal = []

            for i in range(5):

                cantArt = 0

                for j in range(len(sucursales)):

                    cantArt += sucursales[j][i]

                cantArtTotal.append(cantArt)

            print('Las cantidades totales son:\n')

            for i in range(5):

                print(f'- Artículo {i + 1}: {cantArtTotal[i]}')

        case 2:

            cantSucursal2 = 0

            for i in range(5):

                cantSucursal2 += sucursales[1][i]

            print(f'La cantidad de artículos en la sucursal 2 es: {cantSucursal2}')

        case 3:

            print(f'La cantidad del artículo 3 en la sucursal 1 es: {sucursales[0][2]}')

        case 4:

            recaudaciones = []

            for j in range(len(sucursales)):

                recaudacion = 0

                for i in range(5):

                    recaudacion += sucursales[j][i] * preciosArt[i]

                recaudaciones.append(recaudacion)

            print('La recaudación total de cada sucursal es:\n')

            for j in range(len(recaudaciones)):

                print(f'- Sucursal {j + 1}: {recaudaciones[j]:.2f} €')

        case 5:

            recaudacionEmpresa = 0

            for j in range(len(sucursales)):

                for i in range(5):

                    recaudacionEmpresa += sucursales[j][i] * preciosArt[i]

            print(f'La recaudación total de la empresa es: {recaudacionEmpresa:.2f} €')

        case 6:

            recaudaciones = []

            for j in range(len(sucursales)):

                recaudacion = 0

                for i in range(5):

                    recaudacion += sucursales[j][i] * preciosArt[i]

                recaudaciones.append(recaudacion)

            mayorRecaudacion = recaudaciones[0]
            sucursalMayor = 0

            for j in range(len(recaudaciones)):

                if recaudaciones[j] > mayorRecaudacion:

                    mayorRecaudacion = recaudaciones[j]
                    sucursalMayor = j

            print(f'La sucursal de mayor recaudación es la {sucursalMayor + 1} con {mayorRecaudacion:.2f} €')

        case _:

            print('Opción no válida')

print('\n--- Gracias por usar este programa ---')