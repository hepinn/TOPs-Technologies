import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Hepin1230',
        database='bank'
    )
    return connection




