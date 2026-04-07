carrinho = []


programa = True

while programa:
    print("Escolha uma opcao:")
    print("1. Adicionar produto ao carrinho.")
    print("2. Remover produto do carrinho.")
    print("3. Exibir o carrinho atual.")
    print("0. Sair do programa")

    opcao = int(input(""))

    match opcao:
        case 1:
            nome = input("Insira o nome do produto: ")
            preco = float(input("Insira o valor do produto: "))
            carrinho.append([nome, preco])
        case 2:
            nome_remover = input("Insira o nome do produto que voce quer remover: ")
            
            produto_encontrado = False
            
            for item in carrinho:
                if item[0] == nome_remover: 
                    carrinho.remove(item)
                    print(f"{nome_remover} foi removido com sucesso!")
                    produto_encontrado = True
                    break 
            
            if not produto_encontrado:
                print("Produto não encontrado no carrinho.")
        case 3:
            for i in carrinho:
                print(f"Nome: {i[0]} | preco: {i[1]:.2f}")
        case 0:
            programa = False