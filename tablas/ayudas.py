import tkinter as tk
from PIL import Image,ImageTk


def crear_entry_con_img(new_frame,i,ubicacionx,ubicaciony,texto,ubi1,ubi2,textvar,ubirelx,ubirely,relwidth,validate_cmd,only_numbers=False):
    img = imagen(i)#num_img
    label_img=tk.Label(new_frame,image=img,bg="#fff")
    label_img.image=img
    label_img.place(relx=ubicacionx,rely=ubicaciony)#ubicacionx,ubicaciony

    label1=tk.Label(new_frame,text=texto,font=("Times",14),fg="#666a88",bg="#fff")#texto
    label1.place(relx=ubi1,rely=ubi2)#ubi1,ubi2

    if only_numbers:
        entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
    else:
        entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry1.place(relx=ubirelx, rely=ubirely, relwidth=relwidth)
        
def imagen(i):
    camino_imagen=["tablas/imagenes_tabla/Curso.png",
                   "tablas/imagenes_tabla/nombre.png",
                   "tablas/imagenes_tabla/apellido.png",
                   "tablas/imagenes_tabla/f.ingreso.png",
                   "tablas/imagenes_tabla/dni3.png",
                   "tablas/imagenes_tabla/observacion.png",]
    img=leer_imagen(camino_imagen[i],(20,20))
    return img

def leer_imagen(ruta,tamaño):
    return ImageTk.PhotoImage(Image.open(ruta).resize(tamaño,Image.LANCZOS))

def crear_frame_auxiliar( master, altura):
    frame_auxiliar = tk.Frame(master, bg="#fff", width=460, height=altura)
    frame_auxiliar.pack(side=tk.TOP, fill="x")
    frame_auxiliar.pack_propagate(False)
    return frame_auxiliar


    
def solo_numeros(char):
    return char.isdigit()
#La función solo_numeros sirve para comprobar si un carácter dado es un dígito. Es útil cuando quieres asegurarte de que sólo se permiten números en un Entry de Tkinter.
#si es un numero devuelve true sino devuelve false

def crear_textarea_con_img(new_frame, i, ubicacionx, ubicaciony, texto, ubi1, ubi2, textvar, ubirelx, ubirely, relwidth, altura):
    img = imagen(i)  # num_img
    label_img = tk.Label(new_frame, image=img, bg="#fff")
    label_img.image = img
    label_img.place(relx=ubicacionx, rely=ubicaciony)  # ubicacionx, ubicaciony

    label1 = tk.Label(new_frame, text=texto, font=("Times", 14), fg="#666a88", bg="#fff")  # texto
    label1.place(relx=ubi1, rely=ubi2)  # ubi1, ubi2

    textarea = tk.Text(new_frame, font=("Times", 14), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, height=altura)
    textarea.place(relx=ubirelx, rely=ubirely, relwidth=relwidth)  # ubirelx, ubirely, relwidth
    
    if textvar:
        textarea.insert(tk.END, textvar.get())

    return textarea