contatos = {}

while True:
    print("\n=== Cadastro de Contatos ===")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Remover contato")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        contatos[nome] = telefone
        print(f"Contato de {nome} adicionado.")
    elif opcao == "2":
        if contatos:
            print("\nContatos:")
            for nome, telefone in contatos.items():
                print(f"{nome}: {telefone}")
        else:
            print("Nenhum contato cadastrado.")
    elif opcao == "3":
        nome = input("Digite o nome do contato para remover: ")
        if nome in contatos:
            del contatos[nome]
            print(f"Contato de {nome} removido.")
        else:
            print("Contato não encontrado.")
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida.")
