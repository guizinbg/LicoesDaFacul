import listas
def cheio(final, tamanho):
    return final == tamanho

def vazio(final):
    return final == 0

fila = []
tamanho = int(input("Insira o tamanho da fila: "))

final = 0
programa = 1
while programa:
    print("Escolha uma opcao:")
    print("1. Iniciar a fila (a primeira vez que voce abre o programa ja faz isso.)")
    print("2. Inserir um elemento a fila")
    print("3. Remover Elemento do inicio da fila.")
    print("4. Exibir a fila atual.")
    print("0. Sair do programa")

    opcao = int(input(""))

    match opcao:
        case 0:
            programa = 0
        case 1:
            fila = []
            final = 0
        case 2:
            if cheio(final, tamanho):
                print("A fila esta cheia, nao eh possivel inserir elemento na mesma.")
            else:
                elemento = int(input("Digite o elemento que voce quer inserir: "))
                fila.append(elemento)
                final += 1
        case 3:
            if vazio(final):
                print("A fila esta vazia, nao eh possivel remover elemento na mesma.")
            else:
                del fila[0]
                final -= 1
        case 4:
            listas.imprimirLista(fila)