try:
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    if numero1 == 0 or numero2 == 0:
        raise ZeroDivisionError
except ValueError:
    print("Entrada Invalida.")
except ZeroDivisionError:
    print("Divisao por zero nao eh possivel.")
else:
    print(f"{numero1} / {numero2} = {numero1 / numero2}")