import tempfile
import os
import tkinter as tk
# arbol
from tkinter import ttk
from bd import mostrar_tabla, crear_conexion
from PIL import Image, ImageTk
# para moverse entre tablas
from ayudas import abrir_archivo
# botón agregar, modificar y eliminar
from agregar import crear_agregar
from modificar import crear_modificar
from eliminar import crear_eliminar

def tablita(conexion, curso):
    consulta = f"select * from estudiantes where curso='{curso}';"
    data = mostrar_tabla(conexion, consulta)
    
    for item in arboledo.get_children():
        arboledo.delete(item)
    
    for row in data:
        arboledo.insert("", "end", values=row)
        
    conexion.close()

def leer_datos_archivo(nombre_archivo):
    # Obtener la ruta al directorio temporal del sistema
    directorio_temporal = tempfile.gettempdir()
    ruta_completa = os.path.join(directorio_temporal, nombre_archivo)
    
    # Inicializar variables para almacenar los datos
    usuario = None
    contraseña = None
    is_admin = None
    
    # Leer los datos del archivo
    if os.path.exists(ruta_completa):
        with open(ruta_completa, mode='r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if linea.startswith("Usuario:"):
                    usuario = linea.strip().split(":", 1)[1].strip()
                elif linea.startswith("Contraseña:"):
                    contraseña = linea.strip().split(":", 1)[1].strip()
                elif linea.startswith("IsAdmin:"):
                    # Convertir el valor a booleano
                    is_admin = linea.strip().split(":", 1)[1].strip() == '1'
    else:
        print(f"El archivo no existe en la ruta: {ruta_completa}")
    
    return usuario, contraseña, is_admin

# Ejemplo de uso
nombre_archivo = 'resultado_usuario.txt'
usuario, contraseña, is_admin = leer_datos_archivo(nombre_archivo)
print(is_admin)  # Esto imprimirá True o False

# creamos la ventana principal
ventana = tk.Tk()
ventana.title("Tabla Ciclo básico")
ventana.geometry("960x560")
ventana.resizable(False, False)

# función para mostrar el frame seleccionado
def show_frame(frame):
    frame.tkraise()

# función para modificar el título y actualizar la tabla con el curso seleccionado
def DosEnUno(label, texto, curso):
    conexion = crear_conexion()
    label.config(text=texto)
    tablita(conexion, curso)
    
# función para crear los botones de la izquierda
def crear_boton_izq(frame, texto, relx, rely, estado, pady, ruta):
    boton = tk.Button(frame, text=texto, font=("Times", 14, "bold"), width=10, height=1,
                      bg="#fff", fg="#111", borderwidth=2, relief="flat",
                      activebackground="#fff", activeforeground="#111",
                      overrelief="solid", state=estado, disabledforeground="#111",
                      pady=pady, command=lambda: abrir_archivo(ventana, ruta))
    boton.place(relx=relx, rely=rely)

# función para crear los botones del curso
def crear_boton_curso(frame, nombre, relx, rely, comando):
    boton = tk.Button(frame, text=nombre, width=10, height=1,
                      bg="#4575F4", fg="#000", font=("Cambria", 10, "bold"),
                      bd=2, relief="flat", activebackground="#4575F4",
                      activeforeground="#111", overrelief="solid", pady=5,
                      command=comando)
    boton.place(relx=relx, rely=rely, anchor="center")
    return boton

# función para crear los botones de cambio de página
def crear_boton_cambio(frame, nombre, relx, rely, frame_elegido):
    boton = tk.Button(frame, text=nombre, width=10, height=1,
                      pady=5, bg="#4575F4", fg="#000", font=("Cambria", 10, "bold"),
                      bd=2, relief="flat", activebackground="#4575F4",
                      activeforeground="#111", overrelief="solid",
                      command=lambda: show_frame(frame_elegido))
    boton.place(relx=relx, rely=rely, anchor="center")

# función para mostrar el menú contextual
def mostrar_menu(event):
    context_menu.post(event.x_root, event.y_root)

# función para agregar un botón desde el menú contextual
def agregar_boton():
    pass  # Aquí puedes implementar la lógica para agregar un botón dinámicamente

# función para cancelar el menú contextual
def cancelar_menu():
    context_menu.unpost()

# creamos el menú contextual
context_menu = tk.Menu(ventana, tearoff=0, bg="#fff", fg="#000", 
                       font=("Helvetica", 8, "bold italic"), bd=0, 
                       activebackground="#f0f0f0", activeforeground="#000")
context_menu.add_command(label="Agregar botón", command=agregar_boton)
context_menu.add_separator()
context_menu.add_command(label="Cancelar", command=cancelar_menu)

# inicio del código principal

# creamos el frame izquierdo para los botones de navegación y el logo
frame_izq = tk.Frame(ventana, width=165, height=560, bg="#3C5BBA")
frame_izq.pack(side="left")
frame_izq.pack_propagate(False)

# frame para el logo dentro del frame izquierdo
frame_logo = tk.Frame(frame_izq, width=165, height=125, bg="#3C5BBA")
frame_logo.pack(side=tk.TOP)
frame_logo.pack_propagate(False)

# cargamos la imagen del logo
image_path = r"Proyecto mati  cambios administrador y calendario\Proyecto Mati\login_intento-legible.8\imagenes\logo_escuela.png"
image = Image.open(image_path)
new_size = (93, 100)
resized_image = image.resize(new_size, Image.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)

# label para mostrar la imagen del logo
image_label = tk.Label(frame_logo, image=photo, bg="#3C5BBA")
image_label.place(relx=0.5, rely=0.5, anchor='center')

# frame para los botones de la izquierda
frame_botones_izq = tk.Frame(frame_izq, width=165, height=435, bg="#3C5BBA")
frame_botones_izq.pack(side="bottom")

# botones de la izquierda
boton_Basico = crear_boton_izq(frame_botones_izq, "Básico", 0.12, 0.05, "active", 1,
                               r"Proyecto mati  cambios administrador y calendario\Proyecto Mati\tablas\tabla_basico.py")
boton_Superior = crear_boton_izq(frame_botones_izq, "Superior:", 0.12, 0.20, "disabled", 4,
                                 r"Proyecto mati  cambios administrador y calendario\Proyecto Mati\tablas\tabla-basico.py")
boton_Mmo = crear_boton_izq(frame_botones_izq, "MMO", 0.12, 0.304, "active", 4,
                            r"Proyecto mati  cambios administrador y calendario\Proyecto Mati\tablas\tabla_MMO.py")
boton_Informatica = crear_boton_izq(frame_botones_izq, "Informatica", 0.12, 0.408, "active", 4,
                                    r"Proyecto mati  cambios administrador y calendario\Proyecto Mati\tablas\tabla_informatica.py")
boton_Programacion = crear_boton_izq(frame_botones_izq, "Programación", 0.12, 0.511, "active", 4,
                                     r"Proyecto mati  cambios administrador y calendario\Proyecto Mati\tablas\tabla_programacion.py")
boton_Egresados = crear_boton_izq(frame_botones_izq, "Egresados", 0.12, 0.66, "active", 1,
                                  r"Proyecto mati  cambios administrador y calendario\Proyecto Mati\tablas\tabla_egresados.py")
boton_est_pase = crear_boton_izq(frame_botones_izq, "Exalumnos", 0.12, 0.8, "active", 1,
                                 r"Proyecto mati  cambios administrador y calendario\Proyecto Mati\tablas\tabla_e_pases.py")

# creamos el frame superior para los botones de los cursos
frame_cursos = tk.Frame(ventana, width=795, height=130, bg="#ccc")
frame_cursos.pack(side="top")
frame_cursos.pack_propagate(False)

# frame para el título de la tabla
frame_titulo_tabla = tk.Frame(frame_cursos, bg="#fff", width=795, height=80)
frame_titulo_tabla.pack(side="bottom")

# label para mostrar el título de la tabla
titulo_tabla = tk.Label(frame_titulo_tabla, text="Ciclo básico 1ºA", bg="#fff", fg="#111",
                        font=("Cambria", 40, "bold"))
titulo_tabla.place(relx=0.5, rely=0.45, anchor=("center"))

# creamos los frames para los botones de los cursos
frame_botones_sup = tk.Frame(frame_cursos, width=795, height=50, bg="#fff")
frame_botones_sup2 = tk.Frame(frame_cursos, width=795, height=50, bg="#fff")
frame_botones_sup3 = tk.Frame(frame_cursos, width=795, height=50, bg="#fff")

# añadimos los frames a la ventana principal
for frame in (frame_botones_sup, frame_botones_sup2, frame_botones_sup3):
    frame.place(x=0, y=0, width=795, height=50)

# enlazamos el menú contextual con los frames de los botones superiores
for frame in (frame_botones_sup, frame_botones_sup2, frame_botones_sup3):
    frame.bind("<Button-3>", mostrar_menu)

# creamos los botones de los cursos con las funciones correspondientes
boton_1a = crear_boton_curso(frame_botones_sup, "1ºA", 0.08, 0.5, lambda: DosEnUno(titulo_tabla, "Ciclo básico 1ºA", "1a"))
boton_1b = crear_boton_curso(frame_botones_sup, "1ºB", 0.22, 0.5, lambda: DosEnUno(titulo_tabla, "Ciclo básico 1ºB", "1b"))
boton_1c = crear_boton_curso(frame_botones_sup, "1ºC", 0.36, 0.5, lambda: DosEnUno(titulo_tabla, "Ciclo básico 1ºC", "1c"))
boton_1d = crear_boton_curso(frame_botones_sup, "1ºD", 0.50, 0.5, lambda: DosEnUno(titulo_tabla, "Ciclo básico 1ºD", "1d"))
boton_2a = crear_boton_curso(frame_botones_sup, "2ºA", 0.64, 0.5, lambda: DosEnUno(titulo_tabla, "Ciclo básico 2ºA", "2a"))
boton_2b = crear_boton_curso(frame_botones_sup, "2ºB", 0.78, 0.5, lambda: DosEnUno(titulo_tabla, "Ciclo básico 2ºB", "2b"))
boton_siguiente_2 = crear_boton_cambio(frame_botones_sup, "-->", 0.92, 0.5, frame_botones_sup2)

# segundo frame de botones
boton_volver_1 = crear_boton_cambio(frame_botones_sup2, "<--", 0.08, 0.5, frame_botones_sup)
boton_2c = crear_boton_curso(frame_botones_sup2, "2ºC", 0.22, 0.5, lambda: DosEnUno(titulo_tabla, "Ciclo básico 2ºC", "2c"))
boton_2d = crear_boton_curso(frame_botones_sup2, "2ºD", 0.36, 0.5, lambda: DosEnUno(titulo_tabla, "Ciclo básico 2ºD", "2d"))
boton_3a = crear_boton_curso(frame_botones_sup2, "3ºA", 0.50, 0.5, lambda: DosEnUno(titulo_tabla, "Ciclo básico 3ºA", "3a"))
boton_3b = crear_boton_curso(frame_botones_sup2, "3ºB", 0.64, 0.5, lambda: DosEnUno(titulo_tabla, "Ciclo básico 3ºB", "3b"))
boton_3c = crear_boton_curso(frame_botones_sup2, "3ºC", 0.78, 0.5, lambda: DosEnUno(titulo_tabla, "Ciclo básico 3ºC", "3c"))
boton_siguiente_3 = crear_boton_cambio(frame_botones_sup2, "-->", 0.92, 0.5, frame_botones_sup3)

# tercer frame de botones
boton_volver_2 = crear_boton_cambio(frame_botones_sup3, "<--", 0.08, 0.5, frame_botones_sup2)
boton_3d = crear_boton_curso(frame_botones_sup3, "3ºD", 0.22, 0.5, lambda: DosEnUno(titulo_tabla, "Ciclo básico 3ºD", "3d"))

# creamos el frame inferior para los botones de acción (agregar, modificar, eliminar)
frame_acciones = tk.Frame(ventana, width=795, height=60, bg="#fff")
frame_acciones.pack(side="bottom")
frame_acciones.pack_propagate(False)

# botones de acción con configuración basada en permisos
boton_guardar = tk.Button(frame_acciones, text="Guardar", bg="#4575F4", fg="#111",
                          relief="flat", width=10, pady=0, font=("Cambria", 14, "bold"),
                          borderwidth=2, overrelief="solid")
boton_guardar.config(state="normal" if is_admin else "disabled")
boton_guardar.place(relx=0.83, rely=0.5, anchor="center")

boton_nuevo = tk.Button(frame_acciones, text="Agregar", bg="#4575F4", fg="#111",
                        relief="flat", width=10, pady=0, font=("Cambria", 14, "bold"),
                        borderwidth=2, overrelief="solid", command=lambda: crear_agregar(ventana, arboledo, lista_verificacion))
boton_nuevo.config(state="normal" if is_admin else "disabled")
boton_nuevo.place(relx=0.17, rely=0.5, anchor="center")

boton_modificar = tk.Button(frame_acciones, text="Modificar", bg="#4575F4", fg="#111",
                            relief="flat", width=10, pady=0, font=("Cambria", 14, "bold"),
                            borderwidth=2, overrelief="solid", command=lambda: crear_modificar(ventana, arboledo, lista_verificacion))
boton_modificar.config(state="normal" if is_admin else "disabled")
boton_modificar.place(relx=0.39, rely=0.5, anchor="center")

boton_eliminar = tk.Button(frame_acciones, text="Eliminar", bg="#4575F4", fg="#111",
                           relief="flat", width=10, pady=0, font=("Cambria", 14, "bold"),
                           borderwidth=2, overrelief="solid", command=lambda: crear_eliminar(ventana, arboledo))
boton_eliminar.config(state="normal" if is_admin else "disabled")
boton_eliminar.place(relx=0.61, rely=0.5, anchor="center")

# creación del Treeview para mostrar la tabla de estudiantes
arboledo = ttk.Treeview(ventana)
arboledo.pack(fill="both", side="right")

# configuramos las columnas del Treeview
arboledo["columns"] = ["Año", "Nombre", "Apellido", "Ingreso", "DNI", "Obs"]

# configuración de las columnas
arboledo.column('#0', width=0, stretch=tk.NO)
arboledo.column('Año', anchor=tk.CENTER, width=85)
arboledo.column('Nombre', anchor=tk.CENTER, width=140)
arboledo.column('Apellido', anchor=tk.CENTER, width=140)
arboledo.column('Ingreso', anchor=tk.CENTER, width=115)
arboledo.column('DNI', anchor=tk.CENTER, width=115)
arboledo.column('Obs', anchor=tk.CENTER, width=210)

# configuración de las cabeceras
arboledo.heading("#0", text="", anchor=tk.CENTER)
arboledo.heading("Año", text="Curso:", anchor=tk.CENTER)
arboledo.heading("Nombre", text="Nombre/s", anchor=tk.CENTER)
arboledo.heading("Apellido", text="Apellido/s", anchor=tk.CENTER)
arboledo.heading("Ingreso", text="F.Ingreso", anchor=tk.CENTER)
arboledo.heading("DNI", text="DNI", anchor=tk.CENTER)
arboledo.heading("Obs", text="Observaciones", anchor=tk.CENTER)

# añadimos algunas filas de ejemplo
arboledo.insert(parent='', index='end', id=0, text='', values=("5to", "Matias", "Gauto", 2020, 48384544, "Texto de prueba para observar el diseño de la tabla"))
arboledo.insert(parent='', index='end', id=1, text='', values=("5to", "Matias", "Gauto", 2020, 48384544, "Texto de prueba para observar el diseño de la tabla"))

# lista de verificación para la validación de cursos
lista_verificacion = ["1a", "1b", "1c", "1d", "2a", "2b", "2c", "2d", "3a", "3b", "3c", "3d"]

# mostramos la ventana
ventana.mainloop()
