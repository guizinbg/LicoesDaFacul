try:
    numero1 = int(input("Digite o primeiro numero da multiplicacao: "))
    numero2 = int(input("Digite o segundo numero da multiplicacao: "))

except ValueError:
    print("A entrada eh somente numeros inteiros.")

else:
    print(f"{numero1} * {numero2} = {numero1 * numero2}")