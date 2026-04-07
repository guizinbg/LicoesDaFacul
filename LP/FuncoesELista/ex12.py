def alerta(bateria):
    if bateria <= 15.0:
        print("Bateria Fraca")
    else:
        print(f"Bateria em {bateria:.2f}%")

bateria = float(input("Insira o seu percentual de bateria: "))

alerta(bateria)