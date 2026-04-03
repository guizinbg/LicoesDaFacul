try:
    numero = int(input("Digite um numero: "))
except ValueError:
    print("A sua entrada esta invalida.")
else:
    print(f"o numero {numero} eh um inteiro.")