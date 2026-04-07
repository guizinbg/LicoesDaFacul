import listas

l = []

qntd = int(input("Insira o tamanho da fila: "))

for i in range(qntd):
    elemento = int(input(f"Insira o elemento na posicao {i} da lista: "))
    l.append(elemento)

listas.imprimirLista(l)

l2 = []

for i in range(qntd):
    elemento = int(input(f"Insira o elemento na posicao {i} da lista: "))
    l2.append(elemento)

listas.imprimirLista(l2)

if l == l2:
    print("As listas sao iguais.")
else:
    listaA = []
    listaB = []

    for i in range(qntd):
        if l[i] not in l2:
            listaA.append(l[i])
    
    for i in range(qntd):
        if l2[i] not in l:
            listaB.append(l2[i])

listas.imprimirLista(listaA)
listas.imprimirLista(listaB)