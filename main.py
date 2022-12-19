from vendas import conexao, create, read, update, delete
import PySimpleGUI as sg

read()

sg.theme("SandyBeach")
layout = [
    [sg.Text("Lista de Vendas")],
    [sg.Listbox(read.resultado, s=(30, 5), key="query")],
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