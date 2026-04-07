import listas

l1 = listas.criarLista(15)

listas.imprimirLista(l1)

l2 = listas.criarLista(15)

listas.imprimirLista(l2)

listaNumeros = []
listaInter = []
for i in range(len(l1)):
    if l1[i] not in listaNumeros:
        for j in range(i + 1, len(l1), 1):
            if l1[i] == l2[j]:
                listaInter.append(l1[i])
        
        listaNumeros.append(l1[i])
    
listas.imprimirLista(listaInter)
