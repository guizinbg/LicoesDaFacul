listaAlunos = []
listaStatus = []
for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do(a) {nome}: "))

    listaAlunos.append([nome, nota])

for i in range(5):
    if listaAlunos[i][1] < 6:
        listaStatus.append("Reprovado")
    else:
        listaStatus.append("Aprovado")


for i in range(5):
    print(f"Nome: {listaAlunos[i][0]}, Nota: {listaAlunos[i][1]}, Status: {listaStatus[i]}")