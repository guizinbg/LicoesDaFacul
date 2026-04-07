def media(nota1, nota2):
    return (nota1 + nota2) / 2

def boletim(nome, nota1, nota2):
    status = "Aprovado" if media(nota1, nota2) >= 6.0 else "Reprovado"
    print(f"Nome: {nome}|Nota 1: {nota1:.2f}|Nota 2: {nota2:.2f}|Situacao: {status}")

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

boletim(nome, nota1, nota2)