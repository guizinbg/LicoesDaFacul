def triangulo(base, altura):
    return base * altura / 2

try:
    base = float(input("Insira a base do triangulo: "))
    altura = float(input("Insira a altura do triangulo: "))

    if base < 0 or altura < 0:
        raise ValueError

except ValueError:
    print("Entrada invalida. Valor não numerico ou negativo é invalido.")

else:
    print(f"A area do triangulo é {triangulo(base, altura)}")