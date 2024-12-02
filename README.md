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

2. Loop Principal:

```bash
    while True:
```

- Mantém o programa em execução até que o usuário escolha sair.

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

4. Entrada do Usuário