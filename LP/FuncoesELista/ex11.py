def validar(senha):
    return len(senha) >= 8

senha = input("Digite a sua senha: ")

if validar(senha):
    print("A senha preenche os minimos de segurança.")
else:
    print(f"A senha nao preenche os minimos de segurança pois tem {len(senha)} caracteres.")