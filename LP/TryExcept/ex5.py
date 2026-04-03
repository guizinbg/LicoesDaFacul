import math

try:
    numero = float(input("Digite um numero: "))

    print(math.sqrt(numero))
except ValueError:
    print("O valor tem que ser nao negativo e um numero valido.")