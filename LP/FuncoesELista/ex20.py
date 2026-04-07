import listas
import random


l = listas.criarLista(10)

listaNumeros = []

listas.imprimirLista(l)

for i in range(len(l)):
    if l[i] not in listaNumeros:
            cont = 1
            for j in range(i + 1, len(l), 1):
                  if l[i] == l[j]:
                        cont += 1
            print(f"o numero {l[i]} aparece {cont} vezes na lista.")
            listaNumeros.append(l[i])
    
                        
