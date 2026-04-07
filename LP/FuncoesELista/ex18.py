import random

def imprimirLista(lista):
    print("Lista = ", end="")

    for i in lista:
        print(f"{i} ", end="")
    print()

def multi(l):
    for i in range(len(l)):
        l[i] *= 2
    return l

l1 = []

for i in range(10):
    l1.append(random.randint(0,20))

imprimirLista(l1)

imprimirLista(multi(l1))