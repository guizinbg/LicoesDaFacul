import random

def imprimirLista(lista):
    print("Lista = ", end="")

    for i in lista:
        print(f"{i} ", end="")
    print()

def duplicatas(l):
    listaNova = list()
    for i in l:
        if i not in listaNova:
            listaNova.append(i)
    return listaNova

l = list()
for i in range(10):
    l.append(random.randint(0, 10))

imprimirLista(l)

l = duplicatas(l)

imprimirLista(l)

