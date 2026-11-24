#Lectura

f = open('ejemplo.txt', 'r')

print(f.read())      #Devuelve todo el contenido del fichero como una cadena de texto (str)
print(f.readlines()) #Devuelve todo el contenido del fichero como una lista (list) donde cada elemento es una línea

for line in f:

    print(line)


#f.seek(0)   #Descomentando la linea volvemos al principio del fichero, dejando imprimir otra vez

for line in f:

    print(line)

f.close()

#Escritura

#Siempre que se abre un fichero en modo escritura utilizando el
#argumento w , el fichero se inicializa, borrando cualquier contenido que pudiera tener.

f = open('ejemplo.txt', 'w')

canary_iata = ( 'TFN', 'TFS', 'LPA', 'GMZ', 'VDE', 'SPC', 'ACE', 'FUE')

for code in canary_iata:

    f.write(code + '\n' )

f.close()