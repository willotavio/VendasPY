# from vendas import conexao, create, read, update, delete
# op = 0
# while op < 1 or op > 4:
#     print("Selecione a ação que deseja realizar\n1. Adicionar\n2. Consultar\n3. Alterar\n4. Excluir\n")
#     op = int(input())
#     if op == 1:
#         create()
#     elif op == 2:
#         read()
#     elif op == 3:
#         update()
#     elif op == 4:
#         delete()
#     else:
#         print("Selecione uma opção válida")
#     print("Deseja realizar mais alguma ação?\n0. Sim\n1. Não")
#     op = int(input())

from vendas import conexao, create, read, update, delete
import PySimpleGUI as sg

conexao.connect()
cursor = conexao.cursor()
comando = 'SELECT nm_produto, vlr_produto FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
cursor.close()
conexao.close()

sg.theme("SandyBeach")
layout = [
    [sg.Text("Lista de Vendas")],
    [sg.Listbox(resultado, s=(30, 5), key="query")],
    [sg.Text("Adicionar Venda")],
    [sg.Text("Nome do produto:"), sg.InputText(key="nm_produto", size=(10, 1))],
    [sg.Text("Valor do produto:"), sg.InputText(key="vlr_produto", size=(10, 1))],
    [sg.Button("Adicionar"), sg.Button("Atualizar")],
    [sg.InputText(key="cd_produto"), sg.Button("Deletar")]
]

janela1 = sg.Window('Vendas', layout)

while True:
    events, values = janela1.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == "Adicionar":
        create(janela1, values)
    if events == "Atualizar":
        update(janela1, values)
    if events == "Deletar":
        delete(janela1, values)