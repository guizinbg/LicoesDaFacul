import listas
l = []

for i in range(10):
    entrada = int(input(f"Digite o {i + 1} valor da lista: "))
    l.append(entrada)

listas.imprimirLista(l)

listaPositivos = []
for item in l:
    if item >= 0:
        listaPositivos.append(item)

l = listaPositivos

listas.imprimirLista(l)
