import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='vendaspy',
)

# crud
# create
def create():
    conexao.connect()
    cursor = conexao.cursor()
    nm_produto = str(input('Digite o nome do produto vendido\n'))
    vlr_produto = float(input('Digite o valor do produto vendido\n'))
    comando = f'INSERT INTO vendas (nm_produto, vlr_produto) VALUES ("{nm_produto}", {vlr_produto})'  # comando sql
    # f no começo do comando e variaveis com colchetes para o python reconhecer que sao variaveis e nao textos
    cursor.execute(comando)  # executa o comando
    conexao.commit()  # edita o banco de dados
    # resultado = cursor.fetchall() # ler o banco de dados
    cursor.close()
    conexao.close()

# read
def read():
    conexao.connect()
    cursor = conexao.cursor()
    cd_vendas = int(input('Digite o código do produto que deseja consultar\n'))
    comando = f'SELECT * FROM vendas WHERE cd_vendas = {cd_vendas}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
    cursor.close()
    conexao.close()

# update
def update():
    conexao.connect()
    cursor = conexao.cursor()
    cd_vendas = int(input('Digite o código do produto que deseja alterar\n'))
    nm_produto = str(input('Digite o novo nome do produto\n'))
    vlr_produto = float(input('Digite o novo valor do produto\n'))
    comando = f'UPDATE vendas SET nm_produto = "{nm_produto}", vlr_produto = {vlr_produto} WHERE cd_vendas = {cd_vendas}'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

# delete
def delete():
    conexao.connect()
    cursor = conexao.cursor()
    cd_vendas = int(input('Digite o código do produto que deseja excluir\n'))
    comando = f'DELETE FROM vendas WHERE cd_vendas = "{cd_vendas}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()