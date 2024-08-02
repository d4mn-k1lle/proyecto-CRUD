import tkinter as tk
from PIL import Image,ImageTk
import subprocess

#--------------------parte de agregar(por el momento solo agregar)------------------------#

def leer_imagen(ruta,tamaño):
    return ImageTk.PhotoImage(Image.open(ruta).resize(tamaño,Image.LANCZOS))#hace que funcione la imagen

def imagen(i):#el numero de camino imagen 0,1,2,3,4,5
    camino_imagen=["tablas/imagenes_tabla/Curso.png",#aca estan todas las imagenes de los entrys 
                   "tablas/imagenes_tabla/nombre.png",
                   "tablas/imagenes_tabla/apellido.png",
                   "tablas/imagenes_tabla/f.ingreso.png",
                   "tablas/imagenes_tabla/dni3.png",
                   "tablas/imagenes_tabla/observacion.png",]
    img=leer_imagen(camino_imagen[i],(20,20)),#uso de la funcion leer imagen y tamaño
    return img

def crear_entry_con_img(new_frame,i,ubicacionx,ubicaciony,texto,ubi1,ubi2,textvar,ubirelx,ubirely,relwidth,validate_cmd,only_numbers=False):
    img = imagen(i)#num_img
    label_img=tk.Label(new_frame,image=img,bg="#fff")
    label_img.image=img#esta linea es inprescindible pq sino pierde la referencia y no anda la imagen
    label_img.place(relx=ubicacionx,rely=ubicaciony)#ubicacionx,ubicaciony

    label1=tk.Label(new_frame,text=texto,font=("Times",14),fg="#666a88",bg="#fff")#texto
    label1.place(relx=ubi1,rely=ubi2)#ubi1,ubi2

    if only_numbers:#si only numbers es true(es una parametro asi que se puede elegir) hace que solo se pueda usar numeros, lo hace con el validate_cmd(que esta en agregar)
        entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
    else:
        entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry1.place(relx=ubirelx, rely=ubirely, relwidth=relwidth)
    
def modificar_entry_con_img(x,new_frame,i,ubicacionx,ubicaciony,texto,ubi1,ubi2,textvar,ubirelx,ubirely,relwidth,validate_cmd,tree,entries,only_numbers=False):
    selected_item = tree.selection()[0]  # Obtiene el ID del ítem seleccionado
    item_values = tree.item(selected_item, 'Curso')
    
    img = imagen(i)#num_img
    label_img=tk.Label(new_frame,image=img,bg="#fff")
    label_img.image=img#esta linea es inprescindible pq sino pierde la referencia y no anda la imagen
    label_img.place(relx=ubicacionx,rely=ubicaciony)#ubicacionx,ubicaciony

    label1=tk.Label(new_frame,text=texto,font=("Times",14),fg="#666a88",bg="#fff")#texto
    label1.place(relx=ubi1,rely=ubi2)#ubi1,ubi2

    if only_numbers:#si only numbers es true(es una parametro asi que se puede elegir) hace que solo se pueda usar numeros, lo hace con el validate_cmd(que esta en agregar)
        entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
    else:
        entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
        
    entry1.delete(0, tk.END)
    entry1.insert(0, item_values[x])
    entries.append(entry1)
    entry1.place(relx=ubirelx, rely=ubirely, relwidth=relwidth)
    
        
#para los inputs crea un frame, para que luego podamos poner la img y el label al lado y el input abajo
def crear_frame_auxiliar(master, altura):#master es dentro de donde se va ubicar
    frame_auxiliar = tk.Frame(master, bg="#fff", width=460, height=altura)
    frame_auxiliar.pack(side=tk.TOP, fill="x")
    frame_auxiliar.pack_propagate(False)
    return frame_auxiliar


def solo_numeros(char):
    return char.isdigit()
#La función solo_numeros sirve para comprobar si un carácter dado es un dígito. Es útil cuando quieres asegurarte de que sólo se permiten números en un Entry de Tkinter.
#si es un numero devuelve true sino devuelve false

#sirve para obtener lo que se escribio en el textarea(observacion)
def actualizar_textvar(event, textarea, textvar):
    textvar.set(textarea.get("1.0", tk.END))

#crea el textarea y con parametros le damos la imagen y lo ubicamos, ademas de darle la variable donde se va guardar lo que escriba
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
    #no lo entendi del todo pero hace que se pueda rescatar el texto que escriba , ya que en el tk.Text no te deja usar "textvariable="


#-------------------------------fin de agregar---------------------------------------------#

def abrir_archivo(root,ruta_archivo):
    try:
        subprocess.Popen(["python", ruta_archivo])
        root.destroy()  # Cierra la ventana actual
    except:
        print("error")