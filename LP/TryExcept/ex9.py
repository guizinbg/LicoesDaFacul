try:
    kg = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = kg / (altura * altura)
except ValueError:
    print("A entrada eh invalida.")

except ZeroDivisionError:
    print("A divisao por zero nao eh possivel.")

else:
    print(f"O seu IMC eh {imc: .2f}")