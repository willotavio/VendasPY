import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='vendaspy',
)

# crud
# create
def create(janela1, values):
    conexao.connect()
    cursor = conexao.cursor()
    comando = f'INSERT INTO vendas (nm_produto, vlr_produto) VALUES ("{values["nm_produto"]}", {values["vlr_produto"]})'
    cursor.execute(comando)
    conexao.commit()
    comando = 'SELECT nm_produto, vlr_produto FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    janela1["query"].update(resultado)

# read
def read():
    conexao.connect()
    cursor = conexao.cursor()
    comando = 'SELECT nm_produto, vlr_produto FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()

# update
def update(janela1, values):
    conexao.connect()
    cursor = conexao.cursor()
    comando = f'UPDATE vendas SET nm_produto = "{values["nm_produto"]}", vlr_produto = "{values["vlr_produto"]}" WHERE nm_produto = "{values["nm_produto"]}"'
    cursor.execute(comando)
    conexao.commit()
    comando = 'SELECT nm_produto, vlr_produto FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    janela1["query"].update(resultado)

# delete
def delete(janela1, values):
    conexao.connect()
    cursor = conexao.cursor()
    comando = f'DELETE FROM vendas WHERE cd_vendas = "{values["cd_produto"]}"'
    cursor.execute(comando)
    conexao.commit()
    comando = 'SELECT nm_produto, vlr_produto FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    janela1["query"].update(resultado)