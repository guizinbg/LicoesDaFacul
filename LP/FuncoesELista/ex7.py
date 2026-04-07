import random

def printarLista(lista):
    for i in lista:
        print(f"[{i}] ")

def maior(lista):
    maior = lista[0]
    for animal in lista:
        if animal > maior:
            maior = animal
    return maior


lista = list()
for i in range(10):
    lista.append(random.randint(0, 20))

printarLista(lista)

print(f"O maior numero dessa lista eh o {maior(lista)}")
