objetivo = int(input("Introduce el número inicial: "))
suma = 0
numeros = []

while suma < objetivo:
    n = int(input("Introduce un número: "))
    numeros.append(n)
    suma += n

print(numeros)