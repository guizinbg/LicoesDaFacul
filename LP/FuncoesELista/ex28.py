import listas

l = []

qntd = int(input("Insira o tamanho da fila: "))

for i in range(qntd):
    elemento = int(input(f"Insira o elemento na posicao {i} da lista: "))
    l.append(elemento)

listas.imprimirLista(l)
listaNova = []

for i in range(qntd):
    soma = l[0]
    for j in range(i, 0, -1):
        soma += l[j]
    listaNova.append(soma)

listas.imprimirLista(listaNova)