'''
Escribe un programa que cuente cuántas líneas NO vacías contiene un fichero 'entrada.txt' que
tenga varias líneas de prueba
'''
cont = 0

print('Bienvenido, este programa cuenta cuántas lineas de texto escritas tiene un archivo.\n')

f = open('Ej1/entrada.txt', 'r')

for line in f.readlines():

    if line != '\n':

        cont += 1

print(f'El archivo tiene {cont} lineas no vacías -- Gracias por usar el programa')