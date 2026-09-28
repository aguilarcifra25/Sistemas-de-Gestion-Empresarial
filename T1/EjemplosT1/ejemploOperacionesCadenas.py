proverb1 = 'Hola'
proverb2 = 'mundo'
proverb3 = '           AB           '

sentence = proverb1 + ', ' + proverb2

print(sentence[8]) #Elemento 8 hacia la derecha
print(sentence[-3]) #Elemento -3 hacia la izquierda
print('\n')

print(sentence[:4]) #Desde el principio a la 4 posicion
print(sentence[6:]) #Desde la sexta posición hasta el final
print(sentence[::2]) #Desde el principio al final de 2 en 2
print('\n')

print(',' in sentence) #Comprobar si ',' esta en la cadena (Booleano)
print('Hola' not in sentence) #Comprobar si 'hola' no esta en la cadena (Booleano)
print('\n')

print(len(sentence)) #Longitud de la cadena
print('\n')

print(sentence.split(',')) #Partir la cadena donde haya un ','
print(sentence.split()) #Parte la cadena donde haya espacios
print('\n')

print(sentence.partition(',')) #Parte la cadena usando el separador, pero también lo devuelve
print('\n')

print(proverb3.strip()) #Elimina los espacios al principio y final de la cadena
print(proverb3.lstrip()) #Elimina los espacios a la izquierda de la cadena
print(proverb3.rstrip()) #Elimina los espacios a la derecha de la cadena
print('\n')

print(sentence.startswith('Hola')) #Comprueba si empieza por algo
print(sentence.endswith('ndo')) #Comprueba si acaba por algo
print(sentence.find(',')) #Busca donde esta algo (Igual a index, pero si no lo encuentra find no peta y da un -1)
print('\n')

print(proverb3.replace('','C')) #Reemplaza una cosa por otra
print(proverb3.replace('','C', 1)) #Reemplaza una cosa por otra un numero de veces
print('\n')

print(sentence.upper()) #Todo a mayúsculas
print(proverb3.lower()) #Todo a minúsculas
print(sentence.swapcase()) #Cambia mayúsculas por minúsculas
print(proverb2.capitalize()) #Primera a mayúsculas
print(sentence.title()) #Cada nueva palabra tras espacio con la primera en mayúsculas
print('\n')

print('R2D2'.isalnum(), "C3-PO".isalnum()) #Detecta si solo tiene letras y números
print('314'.isnumeric(), '3.14'.isnumeric()) #Comprueba que solo hay números
print('abc'.isalpha(), 'a-b-c'.isalpha()) #Comprueba que solo hay letras
print('\n')

print('ABC'.isupper()) #Comprueba que todo es mayúsculas
print('abc'.islower()) #Comprueba que todo es minúsculas
print('Abc'.istitle()) #Comprueba que la primera es mayúscula