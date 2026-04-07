import random

def imprimirLista(lista):
    print("Lista = ", end="")

    for i in lista:
        print(f"{i} ", end="")
    print()

def mesclagem(l1, l2):
    listaNova = []
    for i in range(len(l1)):
        if l1[i] > l2[i]:
            listaNova.append(l2[i])
            listaNova.append(l1[i])
        else:
            listaNova.append(l1[i])
            listaNova.append(l2[i])
    listaNova.sort()
    return listaNova


l1 = []

for i in range(10):
    l1.append(random.randint(0,20))

l1.sort()

imprimirLista(l1)

l2 = []

for i in range(10):
    l2.append(random.randint(0,20))

l2.sort()

imprimirLista(l2)

listaFinal = mesclagem(l1, l2)

imprimirLista(listaFinal)



