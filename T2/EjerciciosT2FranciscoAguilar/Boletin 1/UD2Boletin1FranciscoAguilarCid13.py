abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('Bienvenido al programa de filtrar el abecedario\n')

print('Abecedario original:')
print(abecedario)
print()

for i in range(len(abecedario) - 1, -1, -1):

    if (i + 1) % 3 == 0:

        abecedario.pop(i)

print('Lista resultante tras eliminar las posiciones múltiplos de 3:')
print(abecedario)

print('\n--- Gracias por usar este programa ---')