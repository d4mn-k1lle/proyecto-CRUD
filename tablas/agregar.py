import tkinter as tk
from ayudas import *
from bd import crear_conexion,ejecutar_datos
from tkinter import messagebox
from tkcalendar import *

def crear_agregar(root,tree,lista_permitidos):#6 entrys y el arbol, es para que al presionar el boton de Ingresar Estudiante obtenga los valores y los inserte(el boton esta al final del codigo)
    #falta conseguir los valores y que se inseerten
    #Cerrar la ventana secundaria anterior si existe
    var_entry1=tk.StringVar()#Curso
    var_entry2=tk.StringVar()#Nombre/s
    var_entry3=tk.StringVar()#Apellido/s
    var_entry4=tk.StringVar()#F.Ingreso
    var_entry5=tk.StringVar()#DNI
    var_entry6=tk.StringVar()#Observaciones
    
    def obtener_valores(var1,var2,var3,var4,var5,var6):
        vare1=var1.get()
        vare2=var2.get()
        vare3=var3.get()
        vare4=var4.get()
        vare5=var5.get()
        vare6=var6.get()
        valor_1=vare1.capitalize()
        valor_2=vare2.title()
        valor_3=vare3.title()
        if valor_1 in lista_permitidos:
            conexion=crear_conexion()
            valoress=[valor_1,valor_2,valor_3,vare4,vare5,vare6] 
            insertar=f"insert into estudiantes (curso,nombres,apellidos,fecha_ingreso,dni,observaciones)values('{valoress[0]}','{valoress[1]}','{valoress[2]}','{valoress[3]}',{valoress[4]},'{valoress[5]}');"
            ejecutar_datos(conexion,insertar)
            conexion.close()
            top.destroy()
        else:
            messagebox.showerror("Error","el primer dato es invalido")
        
    def solo_letras(char):
    # Retorna True si el carácter es una letra, False de lo contrario
        return char.isalpha() or char.isspace()

    #creamos la ventana toplevel para que si se cierra la principal tmb se cierre
    top=tk.Toplevel(root)
    top.grab_set()
    top.resizable(False,False)
    top.title("Agregar estudiante")
    top.config(bg="#fff")
    top.geometry("460x610+89+50")
    # top.protocol("WM_DELETE_WINDOW", lambda: None)
    
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
    crear_entry_con_img(new_frame,0,0.015,0.0,"Curso:",0.065,0.0,var_entry1,0.015,0.5,0.95,validate_cmd)
    #los parametros son: frame donde se guarda,num_img,ubicacion x,y de imagen,texto,ubicacion en x,y del texto la variable en la que se va guardar el textvar y ubicacion en x,y del entry ademas de su largo con el relwidth
    
    #-----------------------------------------------#
    #entry2------------------------------------------------
    new_frame2=crear_frame_auxiliar(frame_inferior,60)
    validacion = new_frame2.register(solo_letras)
    img = imagen(1)
    label_img=tk.Label(new_frame2,image=img,bg="#fff")
    label_img.image=img
    label_img.place(relx=0.015,rely=0.0)

    label2=tk.Label(new_frame2,text="Nombre/s:",font=("Times",14),fg="#666a88",bg="#fff")
    label2.place(relx=0.065,rely=0.0)
    entry2 = tk.Entry(new_frame2, textvariable=var_entry2, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID,validate="key",validatecommand=(validacion,'%S'))
    entry2.place(relx=0.015, rely=0.5, relwidth=0.95)
    
    #-----------------------------------------------#
    new_frame3=crear_frame_auxiliar(frame_inferior,60)
    validacion = new_frame3.register(solo_letras)
    img = imagen(2)
    label_img3=tk.Label(new_frame3,image=img,bg="#fff")
    label_img3.image=img
    label_img3.place(relx=0.015,rely=0.0)

    label3=tk.Label(new_frame3,text="Apellido/s:",font=("Times",14),fg="#666a88",bg="#fff")
    label3.place(relx=0.065,rely=0.0)
    entry3 = tk.Entry(new_frame3, textvariable=var_entry3, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID,validate="key",validatecommand=(validacion,'%S'))
    entry3.place(relx=0.015, rely=0.5, relwidth=0.95)
    
    #-----------------------------------------------#
    #cuarto entry
    new_frame4=crear_frame_auxiliar(frame_inferior,60)
    boton_calendario=tk.Button(new_frame4,text="Fecha de ingreso",width=25,bd=1,relief="solid",bg="#fff",fg="#666a88",font=("Cambria",16,"bold"),command=lambda:calendario(var_entry4))
    boton_calendario.place(rely=0.55,relx=0.5,anchor="center")
    def calendario(var_entry4):
        def obtener_fecha(calendari,var_entry4):
            fecha_seleccionada=calendari.get_date()
            fecha_sin_barras = fecha_seleccionada.replace('/', '')
            var_entry4.set(fecha_sin_barras)
            top2.destroy()
        top2=tk.Toplevel(top)
        top2.geometry("260x245+550+200")#260x185 tamaño del calendario 
        top2.config(bg="#fff")
        top2.resizable(False,False)
        top2.grab_set()
        calendario = Calendar(top2, selectmode='day', date_pattern='dd/mm/yyyy', locale='es',background="#fff",foreground="#000",weekendbackground='#fff',othermonthbackground='#fff',daybackground="#fff",showweeknumbers=False,selectbackground="#eee",selectforeground="#000",bordercolor="#fff",headersbackground="#fff",othermonthwebackground="#fff",font=("cambria",11,"italic"))
        calendario.pack(side="top")
        botonsito=tk.Button(top2,text="Definir Fecha",bg="#3C5BBA",fg="#fff",font=("Helvetica",11,"bold"),pady=0,bd=2,relief="flat",activebackground="#fff",activeforeground="#3C5BBA", overrelief="solid",width=26,command=lambda:obtener_fecha(calendario,var_entry4))
        botonsito.place(rely=0.88,relx=0.5,anchor="center")
    
    #-----------------------------------------------#
    #quinto entry
    new_frame5=crear_frame_auxiliar(frame_inferior,60)
    crear_entry_con_img(new_frame5,4,0.016,0.0,"DNI",0.065,0.0,var_entry5,0.015,0.5,0.95,validate_cmd,only_numbers=True)
    
    #-----------------------------------------------#
    #sexto entry
    new_frame6=crear_frame_auxiliar(frame_inferior,150)
    crear_textarea_con_img(new_frame6,5,0.015,0.0,"Observaciones:",0.065,0.0,var_entry6,0.015,0.18,0.95,5)
    
    #-----------------------------------------------#
    #boton de ingresar, que va insertar en la tabla al ser presionado por eso el lambda
    boton_ingresar=tk.Button(top,text="Ingresar Estudiante",bg="#3C5BBA",fg="#fff",font=("Helvetica",18,"bold"),pady=2,bd=2,relief="flat",activebackground="#fff",activeforeground="#3C5BBA", overrelief="solid",command=lambda:obtener_valores(var_entry1,var_entry2,var_entry3,var_entry4,var_entry5,var_entry6))
    boton_ingresar.place(relx=0.5,rely=0.93,anchor="center",relwidth=0.97)
    
    top.mainloop()
