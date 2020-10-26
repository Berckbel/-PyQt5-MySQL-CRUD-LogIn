import pymysql

def connection():
    conn = pymysql.connect(
        host="localhost", port=3306, user="root",
        password="", db="ejercicio_qtpy"
    )
    print('Database is Connected!')
    return conn