def operacoes(numero1, numero2):
    opcao = int(input("Digite qual das operacoes que voce quer fazer:\n1. Adicao\n2. Subtracao\n3. Multiplicacao\n4. Divisao\n"))

    match opcao:
        case 1:
            print(f"{numero1} + {numero2} = {numero1 + numero2}")
        case 2:
            print(f"{numero1} - {numero2} = {numero1 - numero2}")
        case 3:
            print(f"{numero1} * {numero2} = {numero1 * numero2}")
        case 4:
            print(f"{numero1} / {numero2} = {numero1 / numero2}")

numero1 = int(input("Digite o primeiro numero que voce vai realizar a operacao: "))
numero2 = int(input("Digite o segundo numero que voce vai realizar a operacao: "))

operacoes(numero1, numero2)