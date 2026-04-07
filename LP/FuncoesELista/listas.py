import random
def imprimirLista(lista):
    print("Lista = ", end="")

    for i in lista:
        print(f"{i} ", end="")
    print()

def criarLista(tamanho):
    l1 = []

    for i in range(tamanho):
        l1.append(random.randint(1,tamanho))
    return l1