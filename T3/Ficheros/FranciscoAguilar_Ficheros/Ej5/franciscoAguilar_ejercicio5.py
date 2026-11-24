'''
Realiza un programa que lea el fichero 'datos.txt' y cree un nuevo fichero 'invertido.txt' con las
líneas en orden inverso.
'''

d = open('Ej5/datos.txt')
i = open('Ej5/invertido.txt', 'a')

print('Bienvenido, este programa invierte el orden de las lineas de un archivo\n')

for line in reversed(d.readlines()):

    i.write(f'{line}\n')

print('Operación terminada -- Gracias por usar este programa')