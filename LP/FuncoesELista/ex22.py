import listas

l = listas.criarLista(15)

listas.imprimirLista(l)

posicao = int(input("Insira a posicao que voce quer alterar o numero: "))

l[posicao] = int(input(f"Insira o valor que voce quer inserir na posicao {posicao} da lista: "))

listas.imprimirLista(l)
