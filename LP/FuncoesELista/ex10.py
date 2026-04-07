def printQuad(n):

    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


n = int(input("Digite o tamanho do lado do quadrado: "))

printQuad(n)