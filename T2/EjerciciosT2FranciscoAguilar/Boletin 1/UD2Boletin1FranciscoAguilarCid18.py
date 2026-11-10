numConductores = 0
nombre = []
kms = []
total_kms = []

print('Bienvenido al registro de transporte\n')

numConductores = int(input('Indique el número de conductores: '))

print()

for i in range(numConductores):

    nombre.append(input(f'Escriba el nombre del conductor {i + 1}: '))
    
    kmsSemana = []
    
    for j in range(7):
        
        kmsSemana.append(float(input(f'Kilómetros del día {j + 1}: ')))
        
    kms.append(kmsSemana)
    print()

for i in range(len(kms)):
    
    sumaKms = 0
    
    for j in range(len(kms[i])):
        
        sumaKms += kms[i][j]
        
    total_kms.append(sumaKms)

print('Listado de kilómetros totales por conductor:\n')

for n, t in zip(nombre, total_kms):
    
    print(f'Conductor: {n} - Total kilómetros: {t}')

print('\n--- Gracias por usar este programa ---')