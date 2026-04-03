try:
    palavra = input("Escolha a palavra para checar se eh palindromo: ")

    if not palavra.isalpha():
        raise ValueError

except ValueError:
    print("Entrada Invalida. A palavra so pode conter letras, nao pode inserir numeros nem caracteres especiais.")
else:
    palavra = palavra.lower()
    inverso = palavra[::-1]

    if palavra == inverso:
        print("a palavra eh um palindromo.")
    else:
        print("A palavra nao eh um palindromo.")