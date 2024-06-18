import pymysql

conexao = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "mobibanco"
)

cursor = conexao.cursor()
print('Conectado ao banco de dados')