def primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

try:
    numero = int(input("Digite um numero: "))

    if numero == 1:
        raise ValueError
except ValueError:
    print("A entrada eh invalida ou o numero eh 1.")
else:
    if primo(numero):
        print(f"O numero {numero} eh primo.")
    else:
        print(f"O numero {numero} nao eh primo.")
