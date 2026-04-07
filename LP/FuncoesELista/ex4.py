def conversor(reais):
    return reais / 5.16

try:
    preco = float(input("DIgite o valor em Reais: "))

except ValueError:
    print("O valor precisa ser um numero.")
else:
    print(f"O preco de R${preco} em dolares eh ${conversor(preco):.2f}")
