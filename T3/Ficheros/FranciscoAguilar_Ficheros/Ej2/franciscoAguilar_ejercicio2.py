'''
Crea un programa que añada la fecha y hora actuales al final de un fichero.
'''

import datetime

print('Bienvenido, este programa añade la hora al final de un archivo\n')

f = open('Ej2/documento.txt', 'a')

f.write(str(datetime.datetime.now()))

print('Se ha añadido la hora -- Gracias por usar el programa')