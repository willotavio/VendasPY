from vendas import conexao, create, read, update, delete
op = 0
while op < 1 or op > 4:
    print("Selecione a ação que deseja realizar\n1. Adicionar\n2. Consultar\n3. Alterar\n4. Excluir\n")
    op = int(input())
    if op == 1:
        create()
    elif op == 2:
        read()
    elif op == 3:
        update()
    elif op == 4:
        delete()
    else:
        print("Selecione uma opção válida")
    print("Deseja realizar mais alguma ação?\n0. Sim\n1. Não")
    op = int(input())