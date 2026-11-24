'''
Crea un programa que lea un fichero llamado 'texto.txt' y genere 'numerado.txt' con todas las líneas
precedidas de su número.
'''
cont = 1

t = open('Ej4/texto.txt')

n = open('Ej4/numerado.txt', 'a')


print('Bienvenido, este programa enumera las lineas de un archivo')

for line in t.readlines():

    n.write(f'{cont} - {line}')

    cont += 1

t.close()
n.close()

print('Operación completada -- Gracias por usar este programa')