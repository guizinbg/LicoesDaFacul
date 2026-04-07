import math as mt

def area (raio):
    return mt.pi * mt.pow(raio, 2)

raio = float(input("Entre com o valor do raio: "))

print(f"O valor da area eh {area(raio): .2f} .")