# Objetivo do Projeto

Criar um programa em Python que permita:
- Adicionar um novo contato.
    - Adicionar um nome ao contato.
    - Adicionar um número de telefone ao contato.
- Listar todos os contatos.
- Remover um contato específico.

# Cronograma 

- Dia 1: Configurar o menu do telefone.
- Dia 2: Implementar as funcionalidades de 'Adicionar contatos'.
- Dia 3: Implementar funcionalidade em 'Adicionar nomes e números de telefone aos contatos'.
- Dia 4: Analizar possíveis implementação na Lista de contato.
- Dia 5: Verificar a funcionalidade de 'remover contato específico'.
- Dia 6: Finalizar os ajuste de saída.

# Funcionamento do Programa

 1. O programa exibe um menu com opções:
    - Adicionar contato.
    - Listar contatos.
    - Remover contato.
    - Sair.

 2. O usuário escolhe uma opção digitando o número correspondente.

 3. Dependendo da escolha, o programa executa uma ação:
    - Adicionar um novo contato.
    - Listar todos os contatos.
    - Remover um contato específico.
    - Encerra o programa.

 4. O programa usa um loop while para manter o menu ativo até o usuário optar por sair.

 # Explicação do Código

1. Dicionário de Contatos
    
```bash
    contatos = {}
```

- O dicionário contatos armazena os nomes como chaves e os telefones como valores.
- Exemplo: {'João': '1234-5678', 'Maria': '9876-5432'}.

---

2. Loop Principal:

```bash
    while True:
```

- Mantém o programa em execução até que o usuário escolha sair.

---

3. Exibição do Menu:

```bash
def exibir menu()
    print("\n=== Cadastro de Contatos ===")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Remover contato")
    print("4. Sair")
```
- Exibe as opções disponíveis para o usuário.

---

4. Entrada do Usuário

```bash
    opcao = input("Escolha uma opção: ")
```

- Solicita que o usuário escolha uma opção digitando um número.

---

5. Adicionar Contato

```bash
    if opcao == "1":
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    contatos[nome] = telefone
    print(f"Contato de {nome} adicionado.")
```
 - Solicita o nome e o telefone.
- Adiciona o contato ao dicionário com **contatos[nome] = telefone**.
- Exemplo: Se o usuário digitar **nome = João** e **telefone = 1234**, o dicionário será atualizado para:

```bash
    {'João': '1234'}
```

---

6. Listar Contatos 

```bash
    elif opcao == "2":
    if contatos:
        print("\nContatos:")
        for nome, telefone in contatos.items():
            print(f"{nome}: {telefone}")
    else:
        print("Nenhum contato cadastrado.")
```

- Verifica se há contatos no dicionário:
    - Se houver: Usa um **for** para iterar sobre o dicionário e exibir cada contato no formato **Nome: Telefone**.
    - Se não houver: Informa que não há contatos cadastrados.

---

7. Remover Contato

```bash
    elif opcao == "3":
    nome = input("Digite o nome do contato para remover: ")
    if nome in contatos:
        del contatos[nome]
        print(f"Contato de {nome} removido.")
    else:
        print("Contato não encontrado.")
```

- Solicita o nome do contato a ser removido.
- Verifica se o nome existe no dicionário:
    - Se existir: Remove o contato com **del contatos[nome]**.
    - Se não existir: Exibe uma mensagem de erro.

---

8. Sair do Programa

```bash
    elif opcao == "4":
    print("Saindo do programa.")
    break
```

- Encerra o loop com **break**, finalizando o programa.

---

9. Opição Inválida 

```bash
    else:
    print("Opção inválida.")
```

- Exibe uma mensagem caso o usuário escolha uma opção que não está no menu.

---

 # Resumo das Funcionalidades

Opção - Ação

1. Adiciona um novo contato ao dicionário.
2. Lista todos os contatos cadastrados.
3. Remove um contato com base no nome fornecido pelo usuário.
4. Sai do programa encerrando o loop principal.