import pymysql

conexao = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

cursor = conexao.cursor()
cursor.execute("CREATE DATABASE mobibanco")
