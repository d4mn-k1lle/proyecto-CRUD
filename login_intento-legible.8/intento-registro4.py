import tkinter as tk
from ParaImagenes import frames_imagenes
from bd.config import conectar_bd,insert_data,verificar_usuario_existente
from tkinter import messagebox

def llamar_2():
    fm_i.abrir_archivo_registro()
    fm_i.cerrar_ventana()
    
    
#conectamos a la base de datos
cnx = conectar_bd()


#creamos la ventana
ventana=tk.Tk()
fm_i=frames_imagenes(ventana,420,560)
fm_i.centrar_ventana()
ventana.title("Registro")
ventana.resizable(width=False, height=False)#que no se pueda agrandar ni achicar la ventana
#-- creamos la funcion que lo que hace es agarra de la lista y utiliza la funcion leer imagen y le asignamos un tamaño de 20x20px --#
def imagen(i):
    camino_imagen=["login_intento-legible.8/imagenes/nombre.png",
                   "login_intento-legible.8/imagenes/apellido.png",
                   "login_intento-legible.8/imagenes/usuario.png",
                   "login_intento-legible.8/imagenes/confirmacion_redonda.png",
                   "login_intento-legible.8/imagenes/contraseña.png",
                   "login_intento-legible.8/imagenes/confirmacion_redonda.png",
                   "login_intento-legible.8/imagenes/email.png"]
    img=fm_i.leer_imagen(camino_imagen[i],(20,20))
    return img

def obtener_valores(var_entry1,var_entry2,var_entry3,var_entry4,var_entry5,var_entry6,var_entry7):
    #se guardan los valores de los var_entry en en los valor_entry
    valor_entry1 = var_entry1.get()#nombre
    valor_entry2 = var_entry2.get()#apellido
    valor_entry3 = var_entry3.get()#usuario
    valor_entry4 = var_entry4.get()#conf usuario
    valor_entry5 = var_entry5.get()#contraseña
    valor_entry6 = var_entry6.get()#conf contraseña
    valor_entry7 = var_entry7.get()#email

    if ((valor_entry3==valor_entry4 and valor_entry5==valor_entry6 and "@" in valor_entry7)and
        (valor_entry1!="" and valor_entry2!="" and valor_entry3!="" and valor_entry5!="")):
        if (verificar_usuario_existente(cnx,valor_entry3)):
            messagebox.showerror("Error",f"el usuario'{valor_entry3}' ya existe")
        else:
            insert_data(cnx, valor_entry1, valor_entry2,valor_entry4,valor_entry5,valor_entry7)
            messagebox.showinfo("Aviso","Los datos han sido guardados exitosamente")
            llamar_2()
            
            
    else:
        messagebox.showerror("ERROR","los datos ingresados son invalidos, vuelva a intentarlo")
        
def main():

    #creamos el frame del titulo
    frame_titulo=tk.Frame(ventana,bg="#f0f0f0",width=420,height=100)
    frame_titulo.pack(side=tk.TOP,fill="x")
    frame_titulo.pack_propagate(False)

    #el label del titulo
    label_titulo=tk.Label(frame_titulo,text="Registro",font=("Times",48),bg="#f0f0f0",fg="#226EAD")
    label_titulo.pack(expand=False,pady=10)

    #creamos el segundo frame que va ocupar todo el espacio restante por eso el nombre
    #y ademas va contener a los siete frames para los inputs
    frame_restante=tk.Frame(ventana,bg="#f0f0f0",width=420,height=460)
    frame_restante.pack(side=tk.BOTTOM,fill="both")
    frame_restante.pack_propagate(False)

    #-- creames un frame para cada input basicamente porque sino es imposible poner la imagen, texto al lad y el input abajo entcs la solucion que encontre es crear un frame que dentro de el vaya un input y su imagen y label --#
    
    #aparte asi las posiciones no cambian casi nada y dsp con un poco mas de tiempo hacer una funcion en vez de 7 copiados y pegado diferenciados por un numero

    var_entry1=tk.StringVar()#nombre
    var_entry2=tk.StringVar()#apellido
    var_entry3=tk.StringVar()#usuario
    var_entry4=tk.StringVar()#conf usuario
    var_entry5=tk.StringVar()#contraseña
    var_entry6=tk.StringVar()#conf contraseña
    var_entry7=tk.StringVar()#email

    #-- primer frame --#
    new_frame=fm_i.crear_frame_auxiliar(frame_restante,50)
    img=imagen(0)
    label_img=tk.Label(new_frame,image=img)
    label_img.configure(bg="#f0f0f0")
    label_img.place(relx=0.01,rely=0.0)#ubicacion

    label1=tk.Label(new_frame,text="Nombre:",font=("Times",12),fg="#666a88",bg="#f0f0f0")
    label1.place(relx=0.06,rely=0.0)

    entry1=tk.Entry(new_frame,textvariable=var_entry1,font=("Times",11),fg="#222",bg="#fff",bd=1,relief=tk.SOLID)
    entry1.place(relx=0.02,rely=0.5,relwidth=0.95)
    #-- fin del primer frame --#
    
    #-- segundo frame --#    
    new_frame2=fm_i.crear_frame_auxiliar(frame_restante,50)
    img2=imagen(1)
    label_img2=tk.Label(new_frame2,image=img2)
    label_img2.configure(bg="#f0f0f0")
    label_img2.place(relx=0.01,rely=0.0)
    
    label2=tk.Label(new_frame2,text="Apellido:",font=("Times",12),fg="#666a88",bg="#f0f0f0")
    label2.place(relx=0.06,rely=0.0)
    
    entry2=tk.Entry(new_frame2,textvariable=var_entry2,font=("Times",11),fg="#222",bg="#fff",bd=1,relief=tk.SOLID)
    entry2.place(relx=0.02,rely=0.5,relwidth=0.95)
    #-- fin del segundo frame --#
    
    #-- tercer frame --#
    new_frame3=fm_i.crear_frame_auxiliar(frame_restante,50)
    img3=imagen(2)
    label_img3=tk.Label(new_frame3,image=img3)
    label_img3.configure(bg="#f0f0f0")
    label_img3.place(relx=0.01,rely=0.0)
    
    label3=tk.Label(new_frame3,text="Usuario:",font=("Times",12),fg="#666a88",bg="#f0f0f0")
    label3.place(relx=0.06,rely=0.0)
    
    entry3=tk.Entry(new_frame3,textvariable=var_entry3,font=("Times",11),fg="#222",bg="#fff",bd=1,relief=tk.SOLID)
    entry3.place(relx=0.02,rely=0.5,relwidth=0.95)
    #-- fin del tercer frame --#
    
    #-- cuarto frame --#
    new_frame4=fm_i.crear_frame_auxiliar(frame_restante,50)
    img4=imagen(3)
    label_img4=tk.Label(new_frame4,image=img4)
    label_img4.configure(bg="#f0f0f0")
    label_img4.place(relx=0.01,rely=0.0)
    
    label4=tk.Label(new_frame4,text="Confirmar usuario:",font=("Times",12),fg="#666a88",bg="#f0f0f0")
    label4.place(relx=0.057,rely=0.0)
    
    entry4=tk.Entry(new_frame4,textvariable=var_entry4,font=("Times",11),fg="#222",bg="#fff",bd=1,relief=tk.SOLID)
    entry4.place(relx=0.02,rely=0.5,relwidth=0.95)
    #-- fin del cuarto frame --#
    
    #-- quinto frame --#
    new_frame5=fm_i.crear_frame_auxiliar(frame_restante,50)
    img5=imagen(4)
    label_img5=tk.Label(new_frame5,image=img5)
    label_img5.configure(bg="#f0f0f0")
    label_img5.place(relx=0.01,rely=0.0)
    
    label5=tk.Label(new_frame5,text="Contraseña:",font=("Times",12),fg="#666a88",bg="#f0f0f0")
    label5.place(relx=0.06,rely=0.0)
    
    entry5=tk.Entry(new_frame5,textvariable=var_entry5,font=("Times",11),fg="#222",bg="#fff",bd=1,relief=tk.SOLID,show="*")
    entry5.place(relx=0.02,rely=0.5,relwidth=0.95)
    #-- fin del quinto frame --#
    
    #-- sexto frame --#
    new_frame6=fm_i.crear_frame_auxiliar(frame_restante,50)
    img6=imagen(5)
    label_img6=tk.Label(new_frame6,image=img6)
    label_img6.configure(bg="#f0f0f0")
    label_img6.place(relx=0.01,rely=0.0)
    
    label6=tk.Label(new_frame6,text="Confirmar contraseña:",font=("Times",12),fg="#666a88",bg="#f0f0f0")
    label6.place(relx=0.06,rely=0.0)
    
    entry6=tk.Entry(new_frame6,textvariable=var_entry6,font=("Times",11),fg="#222",bg="#fff",bd=1,relief=tk.SOLID,show="*")
    entry6.place(relx=0.02,rely=0.5,relwidth=0.95)
    #-- fin del sexto frame --#
    
    #-- septimo frame --#
    new_frame7=fm_i.crear_frame_auxiliar(frame_restante,50)
    img7=imagen(6)
    label_img7=tk.Label(new_frame7,image=img7)
    label_img7.configure(bg="#f0f0f0")
    label_img7.place(relx=0.013,rely=0.0)
    
    label7=tk.Label(new_frame7,text="Email:",font=("Times",12),fg="#666a88",bg="#f0f0f0")
    label7.place(relx=0.067,rely=0.0)
    
    entry7=tk.Entry(new_frame7,textvariable=var_entry7,font=("Times",11),fg="#222",bg="#fff",bd=1,relief=tk.SOLID)
    entry7.place(relx=0.02,rely=0.5,relwidth=0.95)
    #-- fin del sexto frame --#
    
    #para que al llamarla sin parentesis se ejecute solo cuando se ejecute el boton
    def obt_val():
        obtener_valores(var_entry1, var_entry2, var_entry3, var_entry4, var_entry5, var_entry6, var_entry7)
    
    bt_guardar=tk.Button(frame_restante,text="Crear usuario",width=400,bg="#226EAD",fg="#f0f0f0",font=("Helvetica",14),bd=0,command=obt_val)
    bt_guardar.pack(pady=18,padx=7)
    
    bt_volver=tk.Button(frame_restante,text="Volver al login",width=100,bg="#f0f0f0",fg="#226EAD",font=("Helvetica",12,"bold"),bd=0,command=llamar_2)
    bt_volver.pack(pady=0,padx=7)
    ventana.mainloop()
main()
