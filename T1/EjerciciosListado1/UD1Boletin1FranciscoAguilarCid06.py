import random

num = random.randint(0, 30)

if num >= 0 and num <= 10:

    print(f"El número está entre 0 y 10 ({num})")

elif num >= 11 and num <= 20:

    print(f"El número está entre 11 y 20 ({num})")

else:

    print(f"El número está entre 21 y 30 ({num})")