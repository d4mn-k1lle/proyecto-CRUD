import tkinter as tk
from PIL import Image, ImageTk
import subprocess

#--------------------parte de agregar(por el momento solo agregar)------------------------#

def leer_imagen(ruta, tamaño):
    return ImageTk.PhotoImage(Image.open(ruta).resize(tamaño, Image.LANCZOS))  # Hace que funcione la imagen

def imagen(i):  # El número de camino imagen 0,1,2,3,4,5
    # Combinando los caminos de imágenes de ambos códigos
    caminos_imagen = [
        "Proyecto Mati\\tablas\\imagenes_tabla\\Curso.png",  # Imagen del primer código
        "Proyecto Mati\\tablas\\imagenes_tabla\\nombre.png",
        "Proyecto Mati\\tablas\\imagenes_tabla\\apellido.png",
        "Proyecto Mati\\tablas\\imagenes_tabla\\f.ingreso.png",
        "Proyecto Mati\\tablas\\imagenes_tabla\\dni3.png",
        "Proyecto Mati\\tablas\\imagenes_tabla\\observacion.png",
        "tablas\\imagenes_tabla\\Curso.png",  # Imagen del segundo código
        "tablas\\imagenes_tabla\\nombre.png",
        "tablas\\imagenes_tabla\\apellido.png",
        "tablas\\imagenes_tabla\\f.ingreso.png",
        "tablas\\imagenes_tabla\\dni3.png",
        "tablas\\imagenes_tabla\\observacion.png",
    ]
    img = leer_imagen(caminos_imagen[i], (20, 20))  # Uso de la función leer imagen y tamaño
    return img

def crear_entry_con_img(new_frame, i, ubicacionx, ubicaciony, texto, ubi1, ubi2, textvar, ubirelx, ubirely, relwidth, validate_cmd, only_numbers=False):
    img = imagen(i)  # num_img
    label_img = tk.Label(new_frame, image=img, bg="#fff")
    label_img.image = img  # Esta línea es imprescindible porque si no pierde la referencia y no anda la imagen
    label_img.place(relx=ubicacionx, rely=ubicaciony)  # ubicacionx, ubicaciony

    label1 = tk.Label(new_frame, text=texto, font=("Times", 14), fg="#666a88", bg="#fff")  # texto
    label1.place(relx=ubi1, rely=ubi2)  # ubi1, ubi2

    if only_numbers:  # Si only numbers es true, hace que solo se puedan usar números
        entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
    else:
        entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry1.place(relx=ubirelx, rely=ubirely, relwidth=relwidth)

def modificar_entry_con_img(x, new_frame, i, ubicacionx, ubicaciony, texto, ubi1, ubi2, textvar, ubirelx, ubirely, relwidth, validate_cmd, tree, entries, only_numbers=False):
    selected_item = tree.selection()[0]  # Obtiene el ID del ítem seleccionado
    item_values = tree.item(selected_item, 'values')

    img = imagen(i)  # num_img
    label_img = tk.Label(new_frame, image=img, bg="#fff")
    label_img.image = img  # Esta línea es imprescindible porque si no pierde la referencia y no anda la imagen
    label_img.place(relx=ubicacionx, rely=ubicaciony)  # ubicacionx, ubicaciony

    label1 = tk.Label(new_frame, text=texto, font=("Times", 14), fg="#666a88", bg="#fff")  # texto
    label1.place(relx=ubi1, rely=ubi2)  # ubi1, ubi2

    if only_numbers:  # Si only numbers es true, hace que solo se puedan usar números
        entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
    else:
        entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)

    entry1.delete(0, tk.END)
    entry1.insert(0, item_values[x])
    entries.append(entry1)
    entry1.place(relx=ubirelx, ubirely=ubirely, relwidth=relwidth)

# Para los inputs crea un frame, para que luego podamos poner la img y el label al lado y el input abajo
def crear_frame_auxiliar(master, altura):  # master es dentro de donde se va ubicar
    frame_auxiliar = tk.Frame(master, bg="#fff", width=460, height=altura)
    frame_auxiliar.pack(side=tk.TOP, fill="x")
    frame_auxiliar.pack_propagate(False)
    return frame_auxiliar

def solo_numeros(char):
    return char.isdigit()

# Sirve para obtener lo que se escribió en el textarea (observación)
def actualizar_textvar(event, textarea, textvar):
    textvar.set(textarea.get("1.0", tk.END))

# Crea el textarea y con parámetros le damos la imagen y lo ubicamos, además de darle la variable donde se va guardar lo que escriba
def crear_textarea_con_img(new_frame, i, ubicacionx, ubicaciony, texto, ubi1, ubi2, textvar, ubirelx, ubirely, relwidth, altura):
    img = imagen(i)  # num_img
    label_img = tk.Label(new_frame, image=img, bg="#fff")
    label_img.image = img
    label_img.place(relx=ubicacionx, rely=ubicaciony)  # ubicacionx, ubicaciony

    label1 = tk.Label(new_frame, text=texto, font=("Times", 14), fg="#666a88", bg="#fff")  # texto
    label1.place(relx=ubi1, rely=ubi2)  # ubi1, ubi2

    textarea = tk.Text(new_frame, font=("Times", 14), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, height=altura)
    textarea.place(relx=ubirelx, rely=ubirely, relwidth=relwidth)  # ubirelx, ubirely, relwidth

    textarea.bind("<KeyRelease>", lambda event: actualizar_textvar(event, textarea, textvar))

#-------------------------------fin de agregar---------------------------------------------#

def abrir_archivo(root, ruta_archivo):
    try:
        subprocess.Popen(["python", ruta_archivo])
        root.destroy()  # Cierra la ventana actual
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")
