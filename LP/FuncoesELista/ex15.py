def classificacao(temperatura):
    if temperatura < 16:
        print("Frio")
    elif temperatura < 25:
        print("Agradavel")
    else:
        print("Quente")

t = float(input("Insira a temperatura local em Graus Celsius: "))

classificacao(t)