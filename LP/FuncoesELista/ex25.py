import listas


t = int(input("Insira o tamanho da lista: "))

l1 = listas.criarLista(t)

listas.imprimirLista(l1)

listaQuadrado = []

for i in l1:
    listaQuadrado.append(i ** 2)

listas.imprimirLista(listaQuadrado)