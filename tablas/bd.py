import mysql.connector
from mysql.connector import Error

def crear_conexion():
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="nuevo_usuario",
            passwd="contraseña_segura",
            database="base_datos_sistema"
        )
        print("Conexion a base de datos fue exitosa")
    except Error as e:
        print(f"The error '{e}' occurred")
    return conexion

crear_conexion()

def ejecutar_datos(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Datos bien ejecutados")
    except Error as e:
        print(f"El error '{e}' ocurrió")
    finally:
        cursor.close()
        connection.close()
        
        
def mostrar_tabla(connection,query):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


