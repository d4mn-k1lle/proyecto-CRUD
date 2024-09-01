# Importar la función desde el archivo observar.py
from observar import mostrar_informacion

# Resto de tus importaciones
import tempfile
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from bd import mostrar_tabla, crear_conexion
from PIL import Image, ImageTk
from ayudas import abrir_archivo
from agregar import crear_agregar
from modificar import crear_modificar
from eliminar import crear_eliminar

# Definición de funciones
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

def actualizar_combobox():
    conexion = crear_conexion()
    consulta = f"select Curso from basico;"
    cursos = mostrar_tabla(conexion, consulta)
    
    if cursos:
        course_cb['values'] = cursos
    else:
        messagebox.showwarning("ADVERTENCIA", "No se encontraron cursos en la base de datos.")

def course_changed(event):
    curso_seleccionado = selected_course.get()
    DosEnUno(titulo_tabla, "Ciclo Basico " + curso_seleccionado, curso_seleccionado)
    print("curso seleccionado")

def tablita(conexion, curso):
    consulta = f"select * from basico where curso='{curso}';"
    data = mostrar_tabla(conexion, consulta)
    
    for item in arboledo.get_children():
        arboledo.delete(item)
    
    for row in data:
        arboledo.insert("", "end", values=row)
        
    conexion.close()

def show_frame(frame):
    frame.tkraise()

def DosEnUno(label, texto, curso):
    conexion = crear_conexion()
    label.config(text=texto)
    tablita(conexion, curso)

def crear_boton_izq(frame, texto, relx, rely, estado, pady, ruta):
    boton = tk.Button(frame, text=texto, font=("Times", 14, "bold"), width=10, height=1, bg="#fff", fg="#111",
                      borderwidth=2, relief="flat", activebackground="#fff", activeforeground="#111", overrelief="solid",
                      state=estado, disabledforeground="#111", pady=pady, command=lambda: abrir_archivo(ventana, ruta))
    boton.place(relx=relx, rely=rely)

def crear_boton_curso(frame, nombre, relx, rely, comando):
    boton = tk.Button(frame, text=nombre, width=10, height=1, bg="#4575F4", fg="#000", font=("Cambria", 10, "bold"), bd=2,
                      relief="flat", activebackground="#4575F4", activeforeground="#111", overrelief="solid", pady=5, command=comando)
    boton.place(relx=relx, rely=rely, anchor="center")

def crear_boton_cambio(frame, nombre, relx, rely, frame_elegido):
    boton = tk.Button(frame, text=nombre, width=10, height=1, pady=5, bg="#4575F4", fg="#000", font=("Cambria", 10, "bold"),
                      bd=2, relief="flat", activebackground="#4575F4", activeforeground="#111", overrelief="solid",
                      command=lambda: show_frame(frame_elegido))
    boton.place(relx=relx, rely=rely, anchor="center")

# Leer los datos del archivo y verificar si el usuario es administrador
nombre_archivo = 'resultado_usuario.txt'
usuario, contraseña, is_admin = leer_datos_archivo(nombre_archivo)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Tabla Ciclo Basico")
ventana.geometry("960x560")
ventana.resizable(False, False)

# Frame izquierdo para botones y logo
frame_izq = tk.Frame(ventana, width=165, height=560, bg="#3C5BBA")
frame_izq.pack(side="left")
frame_izq.pack_propagate(False)

# Frame para el logo dentro del frame del título
frame_logo = tk.Frame(frame_izq, width=165, height=125, bg="#3C5BBA")
frame_logo.pack(side=tk.TOP)
frame_logo.pack_propagate(False)

# Ruta de la imagen del logo
image_path = "Proyecto Mati\login_intento-legible.8\imagenes\logo_escuela.png"
image = Image.open(image_path)

# Redimensionar imagen del logo
new_size = (93, 100)
resized_image = image.resize(new_size, Image.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)

# Mostrar el logo
image_label = tk.Label(frame_logo, image=photo, bg="#3C5BBA")
image_label.place(relx=0.5, rely=0.5, anchor='center')

# Frame para los botones de la izquierda
frame_botones_izq = tk.Frame(frame_izq, width=165, height=435, bg="#3C5BBA")
frame_botones_izq.pack(side="bottom")

# Botones de la izquierda
crear_boton_izq(frame_botones_izq, "Basico", 0.12, 0.05, "active", 1, "Proyecto Mati\\tablas\\tabla_basico.py")
crear_boton_izq(frame_botones_izq, "Superior:", 0.12, 0.20, "disabled", 4, "Proyecto Mati\\tablas\\tabla-basico.py")
crear_boton_izq(frame_botones_izq, "MMO", 0.12, 0.304, "active", 4, "Proyecto Mati\\tablas\\tabla_MMO.py")
crear_boton_izq(frame_botones_izq, "Informatica", 0.12, 0.408, "active", 4, "Proyecto Mati\\tablas\\tabla_informatica.py")
crear_boton_izq(frame_botones_izq, "Programacion", 0.12, 0.511, "active", 4, "Proyecto Mati\\tablas\\tabla_programacion.py")
crear_boton_izq(frame_botones_izq, "Egresados", 0.12, 0.66, "active", 1, "Proyecto Mati\\tablas\\tabla_egresados.py")
crear_boton_izq(frame_botones_izq, "Exalumnos", 0.12, 0.8, "active", 1, "Proyecto Mati\\tablas\\tabla_e_pases.py")

# Frame superior para botones de 1a, 1b, 1c
frame_cursos = tk.Frame(ventana, width=795, height=80, bg="#ccc")
frame_cursos.pack(side="top")
frame_cursos.pack_propagate(False)

# Frame para el título de cada tabla
frame_titulo_tabla = tk.Frame(frame_cursos, bg="#fff", width=795, height=80)
frame_titulo_tabla.pack(side="bottom")

# Título de la tabla
titulo_tabla = tk.Label(frame_titulo_tabla, text="Ciclo Basico", bg="#fff", fg="#111", font=("Cambria", 40, "bold"))
titulo_tabla.place(relx=0.5, rely=0.45, anchor=("center"))

# Frame para el ComboBox de selección de curso
frame_comboBox = tk.Frame(ventana, bg="#fff", width=40, height=40)
frame_comboBox.pack(fill=tk.X, padx=0, pady=0)

# Crear el ComboBox
selected_course = tk.StringVar()
course_cb = ttk.Combobox(frame_comboBox, textvariable=selected_course, background="#fff")
course_cb.set("Por favor seleccione una opcion")

# Inicializar el ComboBox con cursos de la base de datos
actualizar_combobox()

# Evitar que se pueda escribir un valor
course_cb['state'] = 'readonly'
course_cb['background'] = '#fff'

# Ubicar el widget
course_cb.pack(fill=tk.X, padx=5, pady=15)

# Asociar el evento de selección al ComboBox
course_cb.bind('<<ComboboxSelected>>', course_changed)

# Frame para los botones de acciones (agregar, modificar, eliminar, observar)
frame_acciones = tk.Frame(ventana, width=795, height=60, bg="#fff")
frame_acciones.pack(side="bottom")
frame_acciones.pack_propagate(False)

# Botones de acciones
boton_nuevo = tk.Button(frame_acciones, text="Agregar", bg="#4575F4", fg="#111", relief="flat", width=10, pady=0,
                        font=("Cambria", 14, "bold"), borderwidth=2, overrelief="solid",
                        command=lambda: crear_agregar(ventana, arboledo, lista_verificacion, "basico", "opciones_btns_basico"))
boton_nuevo.config(state="normal" if is_admin else "disabled")
boton_nuevo.place(relx=0.17, rely=0.5, anchor="center")

boton_modificar = tk.Button(frame_acciones, text="Modificar", bg="#4575F4", fg="#111", relief="flat", width=10, pady=0,
                            font=("Cambria", 14, "bold"), borderwidth=2, overrelief="solid",
                            command=lambda: crear_modificar(ventana, arboledo, lista_verificacion, "basico", "opciones_btns_basico"))
boton_modificar.config(state="normal" if is_admin else "disabled")
boton_modificar.place(relx=0.39, rely=0.5, anchor="center")

boton_eliminar = tk.Button(frame_acciones, text="Eliminar", bg="#4575F4", fg="#111", relief="flat", width=10, pady=0,
                           font=("Cambria", 14, "bold"), borderwidth=2, overrelief="solid",
                           command=lambda: crear_eliminar(ventana, arboledo, "basico", "opciones_btns_basico"))
boton_eliminar.config(state="normal" if is_admin else "disabled")
boton_eliminar.place(relx=0.61, rely=0.5, anchor="center")

# Botón "Observar" que llama a la función mostrar_informacion
boton_guardar = tk.Button(frame_acciones, text="Observar", bg="#4575F4", fg="#111", relief="flat", width=10, pady=0,
                          font=("Cambria", 14, "bold"), borderwidth=2, overrelief="solid",
                          command=lambda: mostrar_informacion(arboledo, ventana))
boton_guardar.place(relx=0.83, rely=0.5, anchor="center")
lista_verificacion=[ ]
# Treeview para mostrar la tabla
arboledo = ttk.Treeview(ventana)
arboledo.pack(fill="both", side="right")

# Configuración de las columnas del Treeview
arboledo["columns"] = ["Año", "Nombre", "Apellido", "Ingreso", "DNI", "Obs"]
arboledo.column('#0', width=0, stretch=tk.NO)
arboledo.column('Año', anchor=tk.CENTER, width=85)
arboledo.column('Nombre', anchor=tk.CENTER, width=140)
arboledo.column('Apellido', anchor=tk.CENTER, width=140)
arboledo.column('Ingreso', anchor=tk.CENTER, width=115)
arboledo.column('DNI', anchor=tk.CENTER, width=115)
arboledo.column('Obs', anchor=tk.CENTER, width=210)

# Encabezados de las columnas del Treeview
arboledo.heading("#0", text="", anchor=tk.CENTER)
arboledo.heading("Año", text="Curso:", anchor=tk.CENTER)
arboledo.heading("Nombre", text="Nombre/s", anchor=tk.CENTER)
arboledo.heading("Apellido", text="Apellido/s", anchor=tk.CENTER)
arboledo.heading("Ingreso", text="F.Ingreso", anchor=tk.CENTER)
arboledo.heading("DNI", text="DNI", anchor=tk.CENTER)
arboledo.heading("Obs", text="Observaciones", anchor=tk.CENTER)

# Insertar datos de ejemplo en el Treeview
arboledo.insert(parent='', index='end', id=1, text='', values=("--", "--", "--", "AA-AA-AAAA", 12345678, "observaciones generales"))

# Mostrar la ventana principal
ventana.mainloop()
