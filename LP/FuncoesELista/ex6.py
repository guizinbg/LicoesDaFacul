def media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    return (nota1 + nota2 + nota3 + nota4) / 4

mediaNota = media()

if mediaNota >= 7.0:
    print("O Aluno esta aprovado.")
else:
    print("O Aluno esta reprovado.")