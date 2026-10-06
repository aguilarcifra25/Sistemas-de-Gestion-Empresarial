num = int(input('Indica un número para calcular su factorial: '))
fact = 1

for i in range (1, num + 1):

    fact = fact * i

print(f'El resultado es {fact}')
