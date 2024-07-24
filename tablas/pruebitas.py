import tkinter as tk
from PIL import Image, ImageTk

def crear_frame_auxiliar(master, altura):
    frame_auxiliar = tk.Frame(master, bg="#f0f0f0", width=460, height=altura)
    frame_auxiliar.pack(side=tk.TOP, fill="x")
    frame_auxiliar.pack_propagate(False)
    return frame_auxiliar

def leer_imagen(ruta, tamaño):
    return ImageTk.PhotoImage(Image.open(ruta).resize(tamaño, Image.LANCZOS))

def imagen(i):
    camino_imagen = [
        "tablas/imagenes_tabla/Curso.png",
        "tablas/imagenes_tabla/nombre.png",
        "tablas/imagenes_tabla/apellido.png",
        "tablas/imagenes_tabla/dni3.png",
        "tablas/imagenes_tabla/f.ingreso.png",
        "tablas/imagenes_tabla/observacion.png",
    ]
    img = leer_imagen(camino_imagen[i], (20, 20))
    return img

def crear_agregar(root):
    def obtener_valores():
        valor_entry1 = var_entry1.get()
        valor_entry2 = var_entry2.get()
        valor_entry3 = var_entry3.get()
        valor_entry4 = var_entry4.get()
        valor_entry5 = var_entry5.get()
        valor_entry6 = var_entry6.get()
        print(valor_entry1, valor_entry2, valor_entry3, valor_entry4, valor_entry5, valor_entry6)
        
    var_entry1 = tk.StringVar()  # Curso
    var_entry2 = tk.StringVar()  # Nombre/s
    var_entry3 = tk.StringVar()  # Apellido/s
    var_entry4 = tk.StringVar()  # F.Ingreso
    var_entry5 = tk.StringVar()  # DNI
    var_entry6 = tk.StringVar()  # Observaciones
    
    top = tk.Toplevel(root)
    top.title("Agregar un estudiante")
    top.geometry("460x600")
    
    frame_superior = tk.Frame(top, width=460, height=110, bg="#fff")
    frame_superior.pack(side="top")
    frame_superior.pack_propagate(False)
    
    titulo = tk.Label(frame_superior, text="Ingresar Estudiante", font=("Times", 39, "italic bold"), bg="#fff", fg="#3C5BBA")
    titulo.place(relx=0.5, rely=0.45, anchor="center")
    
    frame_inferior = tk.Frame(top, width=460, height=490, bg="#fff", bd=1, relief="solid")
    frame_inferior.pack(side="top")
    
    def crear_entry_con_img(new_frame, i, ubicacionx, ubicaciony, texto, ubi1, ubi2, textvar, ubirelx, ubirely, relwidth):
        img = imagen(i)
        label_img = tk.Label(new_frame, image=img, bg="#f0f0f0")
        label_img.image = img  # Guardar referencia para evitar que la imagen sea recolectada por el garbage collector
        label_img.place(relx=ubicacionx, rely=ubicaciony)
        
        label1 = tk.Label(new_frame, text=texto, font=("Times", 12), fg="#666a88", bg="#f0f0f0")
        label1.place(relx=ubi1, rely=ubi2)
        
        entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
        entry1.place(relx=ubirelx, rely=ubirely, relwidth=relwidth)
        
    new_frame = crear_frame_auxiliar(frame_inferior, 50)
    crear_entry_con_img(new_frame, 0, 0.01, 0.0, "Curso", 0.06, 0.0, var_entry1, 0.02, 0.5, 0.95)
    
    
    top.mainloop()
    
ventana = tk.Tk()
ventana.geometry("500x500")

crear_agregar(ventana)
ventana.mainloop()
