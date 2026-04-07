def tabuada(n):
    print(f"Tabuada do {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

n = int(input("Digite o numero que voce quer saber a tabuada: "))

tabuada(n)