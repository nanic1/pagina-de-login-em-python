import pymysql

conexao = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database= 'mobibanco'
)

cursor = conexao.cursor()
cursor.execute("CREATE TABLE cedentes(user VARCHAR(255), senha VARCHAR(255), nome VARCHAR(255), email VARCHAR(255))")
