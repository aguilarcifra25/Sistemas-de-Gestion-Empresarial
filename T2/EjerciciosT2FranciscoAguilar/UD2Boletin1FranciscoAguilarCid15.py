cadena = ""
cadenaMin = ""
letrasVistas = []
esIsograma = True

print('Bienvenido al comprobador de isogramas\n')

cadena = input('Escriba una cadena de texto: ')

cadenaMin = cadena.lower()

for i in range(len(cadenaMin)):

    caracter = cadenaMin[i]

    if caracter in letrasVistas:

        esIsograma = False
        break
        
    else:

        letrasVistas.append(caracter)

print()

if esIsograma:

    print(f'La cadena "{cadena}" SÍ es un isograma.')

else:

    print(f'La cadena "{cadena}" NO es un isograma.')


print('\n--- Gracias por usar este programa ---')