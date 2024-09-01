import tempfile
import os
import mysql.connector

def conectar_bd():
    try:
        cnx = mysql.connector.connect(user='nuevo_usuario', password='contraseña_segura',
                                      host='localhost', database='base_datos_login')
        print("Conexión a la base de datos exitosa.")
        return cnx
    except mysql.connector.Error as err:
        print(f"Error al conectarse a MySQL: {err}")
        return None

def insert_data(cnx, nombre, apellido, usuario, contraseña, email):
    cursor = cnx.cursor()
    insert_query = "INSERT INTO usuarios (nombre,apellido,usuario,contraseña,email) VALUES (%s,%s,%s,%s,%s)"
    data = (nombre, apellido, usuario, contraseña, email)
    try:
        cursor.execute(insert_query, data)
        cnx.commit()
        print("Datos insertados exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar datos: {err}")
    cursor.close()

def verificar_usuario_existente(cnx, usuario):
    cursor = cnx.cursor()
    query = "SELECT COUNT(*) FROM usuarios WHERE usuario = %s"
    cursor.execute(query, (usuario,))
    resultado = cursor.fetchone()
    cursor.close()
    return resultado[0] > 0

def verificar_credenciales(cnx, usuario, contraseña):
    cursor = cnx.cursor()
    query = "SELECT contraseña, isAdmin FROM usuarios WHERE usuario = %s"
    cursor.execute(query, (usuario,))
    resultado = cursor.fetchone()
    print(f"Resultados de la consulta: {resultado}")
    cursor.close()

    if resultado:
        contraseña_bd = resultado[0]
        coincide = contraseña == contraseña_bd
    else:
        coincide = False
    
    directorio_temporal = tempfile.gettempdir()
    nombre_archivo = 'resultado_usuario.txt'
    ruta_completa = os.path.join(directorio_temporal, nombre_archivo)

    with open(ruta_completa, mode='w', encoding='utf-8') as archivo:
        archivo.write(f"Usuario: {usuario}\n")
        archivo.write(f"Contraseña: {contraseña}\n")
        archivo.write(f"IsAdmin: {resultado[1]}\n")

    print(f"Resultado guardado en el archivo temporal: {ruta_completa}")

    return coincide
