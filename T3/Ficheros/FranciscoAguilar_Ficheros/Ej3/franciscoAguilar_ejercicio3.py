'''
Haz un programa que copie el contenido de un fichero llamado 'origen.txt' en otro llamado
'copia.txt'
'''

print('Bienvenido, este programa copia el contenido de un fichero en otro\n')

o = open('Ej3/original.txt', 'r')
c = open('Ej3/copia.txt', 'w')

c.write(o.read())

o.close()
c.close()

print('Se ha realizado la copia -- Gracias por usar este programa')