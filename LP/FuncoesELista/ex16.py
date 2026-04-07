listaPar = list()
listaImpar = list()

for i in range(10):
    n = int(input("Digite o numero desejado: "))
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)

print("Lista Par = ", end="")

for i in listaPar:
    print(f"{i} ", end="")
print()

print("Lista Impar = ", end="")

for i in listaImpar:
    print(f"{i} ", end="")
print()