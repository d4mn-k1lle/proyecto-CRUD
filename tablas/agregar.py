import tkinter as tk
from ayudas import *

def crear_agregar(root,tree):#6 entrys y el arbol, es para que al presionar el boton de Ingresar Estudiante obtenga los valores y los inserte(el boton esta al final del codigo)
    def obtener_valores(var_entry1,var_entry2,var_entry3,var_entry4,var_entry5,var_entry6,tree,top):
        valor_entry1 = var_entry1.get()#Curso
        valor_entry2 = var_entry2.get()#Nombre
        valor_entry3 = var_entry3.get()#Apellido
        valor_entry4 = var_entry4.get()#F.Ingreso
        valor_entry5 = var_entry5.get()#DNI
        valor_entry6 = var_entry6.get()#Observaciones
        
        valores=(valor_entry1,valor_entry2,valor_entry3,valor_entry4,valor_entry5,valor_entry6)
        tree.insert("",tk.END,values=valores)
        
        top.destroy()
        
    var_entry1=tk.StringVar()#Curso
    var_entry2=tk.StringVar()#Nombre/s
    var_entry3=tk.StringVar()#Apellido/s
    var_entry4=tk.StringVar()#F.Ingreso
    var_entry5=tk.StringVar()#DNI
    var_entry6=tk.StringVar()#Observaciones
    
    
    #creamos la ventana toplevel para que si se cierra la principal tmb se cierre
    top=tk.Toplevel(root)
    top.title("Agregar un estudiante")
    top.config(bg="#fff")
    top.geometry("460x610")
    
    #creamos el frame donde va estar el titulo de "Ingresar Estudiante"
    frame_superior=tk.Frame(top,width=460,height=90,bg="#fff")###medidas exactas
    frame_superior.pack(side="top")
    frame_superior.pack_propagate(False)
    
    #creamos el label del titulo "Ingresar Estudiante"
    titulo=tk.Label(frame_superior,text="Ingresar Estudiante",font=("Times",39,"italic bold"),bg="#fff",fg="#3C5BBA")
    titulo.place(relx=0.5,rely=0.45,anchor="center")
    
    #-----------------------------------------------#
    
    #creamos el frame que va ocupar el resto de la pantalla (la aprte de abajo del titulo)
    frame_inferior=tk.Frame(top,width=460,height=490,bg="#fff",)###medidas exactas
    frame_inferior.pack(side="top")
    
    #-----------------------------------------------#

    validate_cmd = top.register(solo_numeros)#para dni y F.ingreso, aunq por tema de compatibilidad con la funcion en otro archivo debe ir en cada uno como parametro

    #-----------------------------------------------#
    #creamos el primer entry
    new_frame=crear_frame_auxiliar(frame_inferior,60)#alto del frame
    #el nuevo frame_aux
    crear_entry_con_img(new_frame,0,0.015,0.0,"Curso",0.065,0.0,var_entry1,0.015,0.5,0.95,validate_cmd)
    #los parametros son: frame donde se guarda,num_img,ubicacion x,y de imagen,texto,ubicacion en x,y del texto la variable en la que se va guardar el textvar y ubicacion en x,y del entry ademas de su largo con el relwidth
    
    #-----------------------------------------------#
    #segundo entry
    new_frame2=crear_frame_auxiliar(frame_inferior,60)
    crear_entry_con_img(new_frame2,1,0.012,0.0,"Nombre",0.065,0.0,var_entry2,0.015,0.5,0.95,validate_cmd)
    
    #-----------------------------------------------#
    #tercer entry
    new_frame3=crear_frame_auxiliar(frame_inferior,60)
    crear_entry_con_img(new_frame3,2,0.012,0.0,"Apellido",0.065,0.0,var_entry3,0.015,0.5,0.95,validate_cmd)
    
    #-----------------------------------------------#
    #cuarto entry
    new_frame4=crear_frame_auxiliar(frame_inferior,60)
    crear_entry_con_img(new_frame4,3,0.016,0.0,"F.Ingreso",0.065,0.0,var_entry4,0.015,0.5,0.95,validate_cmd,only_numbers=True)
    
    #-----------------------------------------------#
    #quinto entry
    new_frame5=crear_frame_auxiliar(frame_inferior,60)
    crear_entry_con_img(new_frame5,4,0.016,0.0,"DNI",0.065,0.0,var_entry5,0.015,0.5,0.95,validate_cmd,only_numbers=True)
    
    #-----------------------------------------------#
    #sexto entry
    new_frame6=crear_frame_auxiliar(frame_inferior,150)
    crear_textarea_con_img(new_frame6,5,0.015,0.0,"Observaciones",0.065,0.0,var_entry6,0.015,0.18,0.95,5)
    
    #-----------------------------------------------#
    #boton de ingresar, que va insertar en la tabla al ser presionado por eso el lambda
    boton_ingresar=tk.Button(top,text="Ingresar Estudiante",bg="#3C5BBA",fg="#fff",font=("Helvetica",18,"bold"),pady=2,bd=2,relief="flat",activebackground="#fff",activeforeground="#3C5BBA", overrelief="solid",command=lambda:obtener_valores(var_entry1,var_entry2,var_entry3,var_entry4,var_entry5,var_entry6,tree,top))
    boton_ingresar.place(relx=0.5,rely=0.93,anchor="center",relwidth=0.97)
    
    top.mainloop()
