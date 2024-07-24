import mysql.connector

#funcion que conecta a la base de datos base_datos_login, con el usuario "nuevo_usuario" y la contra "contraseña_segura"
def conectar_bd():
    try:
        cnx = mysql.connector.connect(user='nuevo_usuario', password='contraseña_segura',
                                      host='localhost', database='base_datos_login')
        print("Conexión a la base de datos exitosa.")
        return cnx
    except mysql.connector.Error as err:
        print(f"Error al conectarse a MySQL: {err}")
        return None

#funcion para insertar los datos
def insert_data(cnx,nombre,apellido,usuario,contraseña,email):
    cursor = cnx.cursor()
    insert_query = "INSERT INTO usuarios (nombre,apellido,usuario,contraseña,email) VALUES (%s,%s,%s,%s,%s)"
    data = (nombre,apellido,usuario,contraseña,email)
    try:
        cursor.execute(insert_query, data)
        cnx.commit()
        print("Datos insertados exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar datos: {err}")
    cursor.close()
    
def verificar_usuario_existente(cnx, usuario):
    cursor = cnx.cursor()
    query = "SELECT * FROM usuarios WHERE usuario = %s"
    cursor.execute(query, (usuario,))
    resultado = cursor.fetchone()
    cursor.close()
    return resultado is not None

def verificar_credenciales(cnx, usuario, contraseña):
    cursor = cnx.cursor()
    query = "SELECT contraseña FROM usuarios WHERE usuario = %s"
    cursor.execute(query, (usuario,))
    resultado = cursor.fetchone()
    cursor.close()

    if resultado:
        contraseña_bd = resultado[0]
        if contraseña == contraseña_bd:
            return True  # Contraseña coincide
        else:
            return False  # Contraseña no coincide
    else:
        return False  # Usuario no encontrado
