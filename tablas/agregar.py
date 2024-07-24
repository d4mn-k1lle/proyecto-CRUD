import tkinter as tk
from ayudas import *




def crear_agregar(root):#6 entrys 
    def obtener_valores(var_entry1,var_entry2,var_entry3,var_entry4,var_entry5,var_entry6):
        valor_entry1 = var_entry1.get()#nombre
        valor_entry2 = var_entry2.get()#apellido
        valor_entry3 = var_entry3.get()#usuario
        valor_entry4 = var_entry4.get()#conf usuario
        valor_entry5 = var_entry5.get()#contraseña
        valor_entry6 = var_entry6.get()#conf contraseña
        
    var_entry1=tk.StringVar()#Curso
    var_entry2=tk.StringVar()#Nombre/s
    var_entry3=tk.StringVar()#Apellido/s
    var_entry4=tk.StringVar()#F.Ingreso
    var_entry5=tk.StringVar()#DNI
    var_entry6=tk.StringVar()#Observaciones
    
    top=tk.Toplevel(root)
    top.title("Agregar un estudiante")
    top.config(bg="#fff")
    top.geometry("460x610")
    
    frame_superior=tk.Frame(top,width=460,height=90,bg="#fff")###medidas exactas
    frame_superior.pack(side="top")
    frame_superior.pack_propagate(False)
    
    titulo=tk.Label(frame_superior,text="Ingresar Estudiante",font=("Times",39,"italic bold"),bg="#fff",fg="#3C5BBA")
    titulo.place(relx=0.5,rely=0.45,anchor="center")
    
    #-----------------------------------------------#
    
    frame_inferior=tk.Frame(top,width=460,height=490,bg="#fff",)###medidas exactas
    frame_inferior.pack(side="top")
    
    #-----------------------------------------------#

    validate_cmd = top.register(solo_numeros)

    #-----------------------------------------------#
    new_frame=crear_frame_auxiliar(frame_inferior,60)#alto del frame
    #el nuevo frame_aux
    crear_entry_con_img(new_frame,0,0.015,0.0,"Curso",0.065,0.0,var_entry1,0.015,0.5,0.95,validate_cmd)
    #los parametros son: frame donde se guarda,num_img,ubicacion x,y de imagen,texto,ubicacion en x,y del texto la variable en la que se va guardar el textvar y ubicacion en x,y del entry ademas de su largo con el relwidth
    
    new_frame2=crear_frame_auxiliar(frame_inferior,60)
    crear_entry_con_img(new_frame2,1,0.012,0.0,"Nombre",0.065,0.0,var_entry2,0.015,0.5,0.95,validate_cmd)
    
    new_frame3=crear_frame_auxiliar(frame_inferior,60)
    crear_entry_con_img(new_frame3,2,0.012,0.0,"Apellido",0.065,0.0,var_entry3,0.015,0.5,0.95,validate_cmd)
    
    new_frame4=crear_frame_auxiliar(frame_inferior,60)
    crear_entry_con_img(new_frame4,3,0.016,0.0,"F.Ingreso",0.065,0.0,var_entry4,0.015,0.5,0.95,validate_cmd,only_numbers=True)
    
    new_frame5=crear_frame_auxiliar(frame_inferior,60)
    crear_entry_con_img(new_frame5,4,0.016,0.0,"DNI",0.065,0.0,var_entry5,0.015,0.5,0.95,validate_cmd,only_numbers=True)
    
    new_frame6=crear_frame_auxiliar(frame_inferior,150)
    crear_textarea_con_img(new_frame6,5,0.015,0.0,"Observaciones",0.065,0.0,var_entry5,0.015,0.18,0.95,5)
    
    #-----------------------------------------------#
    boton_ingresar=tk.Button(top,text="Ingresar Estudiante",bg="#3C5BBA",fg="#fff",font=("Helvetica",18,"bold"),pady=2,bd=2,relief="flat",activebackground="#fff",activeforeground="#3C5BBA", overrelief="solid")
    boton_ingresar.place(relx=0.5,rely=0.93,anchor="center",relwidth=0.97)
    
    top.mainloop()
    
ventana=tk.Tk()
ventana.geometry("500x500")

crear_agregar(ventana)
ventana.mainloop()    