try:
    distancia = float(input("DIgite a distancia da viagem em Km: "))
    velocidadeMedia = float(input("Digite a Velocidade em Km/h: "))

    tempo = distancia / velocidadeMedia

except ValueError:
    print("A entrada eh invalida.")

except ZeroDivisionError:
    print("A divisao por zero nao eh possivel.")

else:
    print(f"A viagem demorou {tempo} horas.")