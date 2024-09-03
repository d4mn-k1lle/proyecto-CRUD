import tkinter as tk
from ParaImagenes import frames_imagenes
from bd.config import conectar_bd, insert_data, verificar_usuario_existente,verificar_credenciales
from tkinter import messagebox
from tkinter import ttk



def main_registro():
    
    def solo_letras(char):
        # Retorna True si el carácter es una letra o un espacio
        return char.isalpha() or char.isspace()
    
    def capitalizar_palabras(event,entry):
            # Obtener el texto actual del Entry
            entry.config(validate="none")
            current_text = entry.get()
            # Capitalizar la primera letra de cada palabra
            capitalized_text = current_text.title()
            # Actualizar el texto del Entry
            entry.delete(0, tk.END)
            entry.insert(0, capitalized_text)
            entry.config(validate="key")
    
    def obtener_valores(var_entry1, var_entry2, var_entry3, var_entry4, var_entry5, var_entry6, var_entry7,lb1,lb2,lb3,lb4,lb5,lb6,lb7,etr3,etr4,etr5,etr6,etr7):
        # Se guardan los valores de los var_entry en los valor_entry
        valor_entry1 = var_entry1.get()  # Nombre
        valor_entry2 = var_entry2.get()  # Apellido
        valor_entry3 = var_entry3.get()  # Usuario
        valor_entry4 = var_entry4.get()  # Conf usuario
        valor_entry5 = var_entry5.get()  # Contraseña
        valor_entry6 = var_entry6.get()  # Conf contraseña
        valor_entry7 = var_entry7.get()  # Email

        if not valor_entry1:
            lb1.config(fg="#f00", font=("Times", 12,"underline"),text="Nombre:*")
        if not valor_entry2:
            lb2.config(fg="#f00", font=("Times", 12,"underline"),text="Apellido:*")
        if not valor_entry3:
            lb3.config(fg="#f00", font=("Times", 12,"underline"),text="Usuario:*")
        if not valor_entry4:
            lb4.config(fg="#f00", font=("Times", 12,"underline"),text="Confirmar Usuario:*")
        if not valor_entry5:
            lb5.config(fg="#f00", font=("Times", 12,"underline"),text="Contraseña:*")
        if not valor_entry6:
            lb6.config(fg="#f00", font=("Times", 12,"underline"),text="Confirmar Contraseña:*")
        if not valor_entry7:
            lb7.config(fg="#f00", font=("Times", 12,"underline"),text="Email:*")

        if valor_entry1:
            lb1.config(fg="#666a88", font=("Times", 12),text="Nombre:")
        if valor_entry2:
            lb2.config(fg="#666a88", font=("Times", 12),text="Apellido:")
        if valor_entry3:
            lb3.config(fg="#666a88", font=("Times", 12),text="Usuario:")
        if valor_entry4:
            lb4.config(fg="#666a88", font=("Times", 12),text="Confirmar Usuario:")  
        if valor_entry5:
            lb5.config(fg="#666a88", font=("Times", 12),text="Contraseña:")
        if valor_entry6:
            lb6.config(fg="#666a88", font=("Times", 12),text="Confirmar Contraseña:")
        if valor_entry7:
            lb7.config(fg="#666a88", font=("Times", 12),text="Email:")
        
        if valor_entry3!=valor_entry4:
            lb3.config(fg="#f00", font=("Times", 12),text="Usuario:*")
            lb4.config(fg="#f00", font=("Times", 12),text="Confirmar Usuario:*")
            if valor_entry3 and valor_entry4:  
                etr3.config(fg="#f00")
                etr4.config(fg="#f00")
        if valor_entry3==valor_entry4 and valor_entry3 and valor_entry4:
            lb3.config(fg="#666a88", font=("Times", 12),text="Usuario:")
            lb4.config(fg="#666a88", font=("Times", 12),text="Confirmar Usuario:")  
            if valor_entry3 and valor_entry4:
                etr3.config(fg="#222")
                etr4.config(fg="#222")
            
        if valor_entry5!=valor_entry6:
            lb5.config(fg="#f00", font=("Times", 12),text="Contraseña:*")
            lb6.config(fg="#f00", font=("Times", 12),text="Confirmar Contraseña:*")  
            if valor_entry5 and valor_entry6:
                etr5.config(fg="#f00")
                etr6.config(fg="#f00")
        if valor_entry5==valor_entry6 and valor_entry5 and valor_entry6:
            lb5.config(fg="#666a88", font=("Times", 12),text="Contraseña:")
            lb6.config(fg="#666a88", font=("Times", 12),text="Confirmar Contraseña:")  
            if valor_entry5 and valor_entry6:
                etr5.config(fg="#222")
                etr6.config(fg="#222")

        # Verificar formato del email (endswith Sirve para comprobar si una cadena termina con un texto específico, en este caso dominios_permitidos )
        dominios_permitidos = ["abc.gob.ar"]
        if not ("@" in valor_entry7 and any(valor_entry7.endswith(dominio) for dominio in dominios_permitidos)):
            etr7.config(fg="#f00")
            lb7.config(fg="#f00",text="Email(@abc.gob.ar):*")
            return
        else:
            etr7.config(fg="#222")
            lb7.config(fg="#222",text="Email:")

        # Verifica si las confirmaciones estan correctas != compara entre una y otra, si no son iguales, manda error.
        if valor_entry3 != valor_entry4:
            messagebox.showerror("ERROR", "El usuario no coincide con el que proporcionaste.")
            return
        if valor_entry5 != valor_entry6:
            messagebox.showerror("ERROR", "La contraseña no coincide con la que proporcionaste.")
            return
        
        # Verificar si el usuario ya existe en la base de datos
        if verificar_usuario_existente(cnx, valor_entry3):
            messagebox.showerror("Error", f"El usuario '{valor_entry3}' ya existe")
        else:
            insert_data(cnx, valor_entry1, valor_entry2, valor_entry4, valor_entry5, valor_entry7)
            messagebox.showinfo("Aviso", "Los datos han sido guardados exitosamente")
            llamar_2()
    # creamos la ventana
    ventana = tk.Tk()
    fm_i = frames_imagenes(ventana, 420, 560)
    fm_i.centrar_ventana()
    ventana.title("Registro")
    ventana.resizable(width=False, height=False)  # que no se pueda agrandar ni achicar la ventana
    # conectamos a la base de datos
    cnx = conectar_bd()
    
    def llamar_2():
        fm_i.cerrar_ventana()
        # fm_i.abrir_archivo_registro()
        main_login()
    
    def imagen(i):
        camino_imagen=["C:/Users/Net Bonzi/Desktop/tkinter/login_intento-legible.8/imagenes/nombre.png",
                   "C:/Users/Net Bonzi/Desktop/tkinter/login_intento-legible.8/imagenes/apellido.png",
                   "C:/Users/Net Bonzi/Desktop/tkinter/login_intento-legible.8/imagenes/usuario.png",
                   "C:/Users/Net Bonzi/Desktop/tkinter/login_intento-legible.8/imagenes/confirmacion_redonda.png",
                   "C:/Users/Net Bonzi/Desktop/tkinter/login_intento-legible.8/imagenes/contraseña.png",
                   "C:/Users/Net Bonzi/Desktop/tkinter/login_intento-legible.8/imagenes/confirmacion_redonda.png",
                   "C:/Users/Net Bonzi/Desktop/tkinter/login_intento-legible.8/imagenes/email.png"]
        img = fm_i.leer_imagen(camino_imagen[i], (20, 20))
        return img
    

    validacion = ventana.register(solo_letras)
    # creamos el frame del título
    frame_titulo = tk.Frame(ventana, bg="#f0f0f0", width=420, height=100)
    frame_titulo.pack(side=tk.TOP, fill="x")
    frame_titulo.pack_propagate(False)

    # el label del título
    label_titulo = tk.Label(frame_titulo, text="Registro", font=("Times", 48), bg="#f0f0f0", fg="#226EAD")
    label_titulo.pack(expand=False, pady=10)

    # creamos el segundo frame que va ocupar todo el espacio restante por eso el nombre
    # y además va contener a los siete frames para los inputs
    frame_restante = tk.Frame(ventana, bg="#f0f0f0", width=420, height=460)
    frame_restante.pack(side=tk.BOTTOM, fill="both")
    frame_restante.pack_propagate(False)

    # -- creamos un frame para cada input básicamente porque sino es imposible poner la imagen, texto al lado y el input abajo entonces la solución que encontré es crear un frame que dentro de él vaya un input y su imagen y label -- #
    var_entry1 = tk.StringVar()  # Nombre
    var_entry2 = tk.StringVar()  # Apellido
    var_entry3 = tk.StringVar()  # Usuario
    var_entry4 = tk.StringVar()  # Conf usuario
    var_entry5 = tk.StringVar()  # Contraseña
    var_entry6 = tk.StringVar()  # Conf contraseña
    var_entry7 = tk.StringVar()  # Email

    # -- Primer frame -- #
    new_frame = fm_i.crear_frame_auxiliar(frame_restante, 50)
    img = imagen(0)
    label_img = tk.Label(new_frame, image=img)
    label_img.configure(bg="#f0f0f0")
    label_img.place(relx=0.01, rely=0.0)  # ubicación

    label1 = tk.Label(new_frame, text="Nombre:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
    label1.place(relx=0.06, rely=0.0)

    entry1 = tk.Entry(new_frame, textvariable=var_entry1, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID,validate='key',validatecommand=(validacion,'%S'))
    entry1.place(relx=0.02, rely=0.5, relwidth=0.95)
    entry1.bind('<KeyRelease>',lambda event:capitalizar_palabras(event,entry1))
    # -- Fin del primer frame -- #

    # -- Segundo frame -- #    
    new_frame2 = fm_i.crear_frame_auxiliar(frame_restante, 50)
    img2 = imagen(1)
    label_img2 = tk.Label(new_frame2, image=img2)
    label_img2.configure(bg="#f0f0f0")
    label_img2.place(relx=0.01, rely=0.0)

    label2 = tk.Label(new_frame2, text="Apellido:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
    label2.place(relx=0.06, rely=0.0)

    entry2 = tk.Entry(new_frame2, textvariable=var_entry2, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID,validate='key',validatecommand=(validacion,'%S'))
    entry2.place(relx=0.02, rely=0.5, relwidth=0.95)
    entry2.bind('<KeyRelease>',lambda event:capitalizar_palabras(event,entry2))
    # -- Fin del segundo frame -- #

    # -- Tercer frame -- #
    new_frame3 = fm_i.crear_frame_auxiliar(frame_restante, 50)
    img3 = imagen(2)
    label_img3 = tk.Label(new_frame3, image=img3)
    label_img3.configure(bg="#f0f0f0")
    label_img3.place(relx=0.01, rely=0.0)

    label3 = tk.Label(new_frame3, text="Usuario:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
    label3.place(relx=0.06, rely=0.0)

    entry3 = tk.Entry(new_frame3, textvariable=var_entry3, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry3.place(relx=0.02, rely=0.5, relwidth=0.95)
    # -- Fin del tercer frame -- #

    # -- Cuarto frame -- #
    new_frame4 = fm_i.crear_frame_auxiliar(frame_restante, 50)
    img4 = imagen(3)
    label_img4 = tk.Label(new_frame4, image=img4)
    label_img4.configure(bg="#f0f0f0")
    label_img4.place(relx=0.01, rely=0.0)

    label4 = tk.Label(new_frame4, text="Confirmar usuario:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
    label4.place(relx=0.057, rely=0.0)

    entry4 = tk.Entry(new_frame4, textvariable=var_entry4, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry4.place(relx=0.02, rely=0.5, relwidth=0.95)
    # -- Fin del cuarto frame -- #

    def ver_contraseña(entry,ver):
        if ver.get():  # Si el check está marcado
            entry.config(show='')  # Muestra el texto
        else:
            entry.config(show='*')  # Oculta el texto

    ver = tk.BooleanVar(value=False)
    

    # -- Quinto frame -- #
    new_frame5 = fm_i.crear_frame_auxiliar(frame_restante, 50)
    img5 = imagen(4)
    label_img5 = tk.Label(new_frame5, image=img5)
    label_img5.configure(bg="#f0f0f0")
    label_img5.place(relx=0.01, rely=0.0)

    label5 = tk.Label(new_frame5, text="Contraseña:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
    label5.place(relx=0.06, rely=0.0)
    
    style = ttk.Style()
    style.configure("TCheckbutton", font=("Times", 11), foreground="#666a88")

    check=ttk.Checkbutton(new_frame5,text="Mostrar contraseña",variable=ver,command=lambda:ver_contraseña(entry5,ver),style="TCheckbutton")
    check.place(relx=0.65,rely=0.01)

    entry5 = tk.Entry(new_frame5, textvariable=var_entry5, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, show="*")
    entry5.place(relx=0.02, rely=0.5, relwidth=0.95)
    # -- Fin del quinto frame -- #

    # -- Sexto frame -- #
    
    new_frame6 = fm_i.crear_frame_auxiliar(frame_restante, 50)
    img6 = imagen(5)
    label_img6 = tk.Label(new_frame6, image=img6)
    label_img6.configure(bg="#f0f0f0")
    label_img6.place(relx=0.01, rely=0.0)

    label6 = tk.Label(new_frame6, text="Confirmar contraseña:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
    label6.place(relx=0.06, rely=0.0)


    ver2 = tk.BooleanVar(value=False)
    check=ttk.Checkbutton(new_frame6,text="Mostrar contraseña",variable=ver2,command=lambda:ver_contraseña(entry6,ver2),style="TCheckbutton")
    check.place(relx=0.65,rely=0.01)
    
    
    entry6 = tk.Entry(new_frame6, textvariable=var_entry6, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, show="*")
    entry6.place(relx=0.02, rely=0.5, relwidth=0.95)
    # -- Fin del sexto frame -- #

    # -- Séptimo frame -- #
    new_frame7 = fm_i.crear_frame_auxiliar(frame_restante, 50)
    img7 = imagen(6)
    label_img7 = tk.Label(new_frame7, image=img7)
    label_img7.configure(bg="#f0f0f0")
    label_img7.place(relx=0.013, rely=0.0)

    label7 = tk.Label(new_frame7, text="Email:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
    label7.place(relx=0.067, rely=0.0)

    entry7 = tk.Entry(new_frame7, textvariable=var_entry7, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry7.place(relx=0.02, rely=0.5, relwidth=0.95)
    # -- Fin del séptimo frame -- #

    # para que al llamarla sin paréntesis se ejecute solo cuando se ejecute el botón
    def obt_val():
        obtener_valores(var_entry1, var_entry2, var_entry3, var_entry4, var_entry5, var_entry6, var_entry7,label1,label2,label3,label4,label5,label6,label7,entry3,entry4,entry5,entry6,entry7)

    bt_guardar = tk.Button(frame_restante, text="Crear usuario", width=400, bg="#226EAD", fg="#f0f0f0", font=("Helvetica", 14), bd=0, command=obt_val)
    bt_guardar.pack(pady=18, padx=7)

    bt_volver = tk.Button(frame_restante, text="Volver al login", width=100, bg="#f0f0f0", fg="#226EAD", font=("Helvetica", 12, "bold"), bd=0, command=llamar_2)
    bt_volver.pack(pady=0, padx=7)
    ventana.mainloop()
    



def main_login():
    def obtener_valores(cnx,var_entry1,var_entry2):
        valor_entry1 = var_entry1.get()#usuario
        valor_entry2 = var_entry2.get()#contraseña
        
        return verificar_credenciales(cnx,valor_entry1,valor_entry2)
    #para el segundo boton que destruya la ventana actual y abra la "secundaria" que seria el registro
    def llamar_2():
        fm_i.cerrar_ventana()
        # fm_i.abrir_archivo()
        main_registro()

    #-- creamos la ventana y heredamos la clase frames_imagenes --#
    ventana=tk.Tk()
    fm_i=frames_imagenes(ventana,720,480)
    fm_i.centrar_ventana()#fm_i es un nombre nada mas para llamar las cosas de la clase luego si quieren lo cambian a lo que quieran
    ventana.title("Login")
    ventana.resizable(width=False, height=False)#la ventana no se puede agrandar ni achicar
    
    
    var_entry1=tk.StringVar()
    var_entry2=tk.StringVar()
    
    
    #-- creamos el frame del logo de la escuela que basicamente ocupa toda la parte izquierda --#
    frame_izq=tk.Frame(ventana,bg="#0B4EBD",width=280,height=480)
    frame_izq.pack(side=tk.LEFT,fill=tk.Y)
    frame_izq.pack_propagate(False)#hacer que el frame mantenga su tamaño (si o si necesario)

    #-- llamammos la imagen y le damos tamaño --#
    camino_imagen="C:/Users/Net Bonzi/Desktop/tkinter/login_intento-legible.8/imagenes/logo_escuela.png"
    img=fm_i.leer_imagen(camino_imagen,(200,200))#imagen y tamaño asignados a img

    label_img=tk.Label(frame_izq,image=img)#se 
    ###la linea sig no se si es explicitamente necesaria sinceramente,fijense###
    #label_img.image=img la comento si salta algun error fijense de agregarla
    label_img.configure(bg="#0B4EBD")
    label_img.place(relx=0.14,rely=0.29)

    #-- le damos fondo,alto, y ancho, para luego en el .place darle cuanto del espacio disponible del eje x va ocupar y luego con el y. por ultimo el ne le indica que va en el noroeste --#
    frame_NorOeste=tk.Frame(ventana,bg="#fafafa",width=440,height=145)
    frame_NorOeste.place(relx=1.0,rely=0.0,anchor="ne")#el relx y rely hacen qeu se ubique en la esquina arriba a la derecha
    frame_NorOeste.pack_propagate(False)

    #-- titulo --#
    label_titulo=tk.Label(frame_NorOeste,text="Inicio de sesion",font=("Times",42),bg="#fafafa",fg="#666a88")#0B4EBD antes
    label_titulo.pack(expand=True,pady=20)

    #-- creamos el frame de abajo a la derecha --#
    frame_SurEste=tk.Frame(ventana,bg="#fafafa",width=440,height=335)
    frame_SurEste.place(relx=1.0,rely=1.0,anchor="se")
    frame_SurEste.pack_propagate(False)
    #aca usamos rely 1.0 para que se ubique en una esquina de abajo en este caso la de abajo a la derecha (incluyendo a relx=1.0)

    #-- creamos el label usuario --#
    label1=tk.Label(frame_SurEste,text="Usuario: ",font=("Times",14),fg="#666a88",bg="#fafafa")#0B4EBD antes
    label1.pack(pady=10,padx=15,anchor="w")

    #-- creamos el input del usuario(mas adelante si quieren le podriamos poner un placeholder) --#
    entry1=tk.Entry(frame_SurEste,textvariable=var_entry1,width=80,font=("Times",14),fg="#111",bd=1,relief=tk.SOLID)
    entry1.pack(pady=5,padx=15,anchor="w")

    #-- creamos el label contraseña --#
    label2=tk.Label(frame_SurEste,text="Contraseña: ",font=("Times",14),fg="#666a88",bg="#fafafa")#0b4ebd antes
    label2.pack(pady=11,padx=15,anchor="w")

    #-- creamos el input de la contraseña y con el show hacemos que no se vea sino que se vean asteriscos --#
    entry2=tk.Entry(frame_SurEste,textvariable=var_entry2,width=80,font=("Times",14),fg="#111",bd=1,relief=tk.SOLID,show="*")
    entry2.pack(pady=6,padx=15,anchor="w")#el anchor define el lugar del widget(dentro del frame obvio)

    #funcion para qeu no se ejecute automatico
    def registro():
        cnx = conectar_bd()
        if cnx:
            # Verificar credenciales
            if obtener_valores(cnx, var_entry1, var_entry2)==True:
                messagebox.showinfo("Éxito", "Login exitoso")
                fm_i.abrir_archivo_panelcontrol()
                ventana.destroy()
                # Aquí puedes agregar la lógica para abrir una nueva ventana o realizar otras acciones después del login exitoso
            else:
                messagebox.showerror("Error", "Credenciales incorrectas")
            cnx.close()  # Cerrar conexión después de usarla
    
    #-- botton de iniciar sesion y su ubicacion en la ventana --#
    boton1=tk.Button(frame_SurEste,text="Iniciar sesion",font=("Helvetica",15,"bold"),bg="#0B4EBD",bd=0,fg="#fafafa",width=80,height=1,command=lambda:registro())
    boton1.pack(padx=16,pady=28)


    #-- boton de registrar usuario y su ubicacion en la ventana--#
    boton2=tk.Button(frame_SurEste,text="Registrar Usuario",font=("Times",14),bg="#fafafa",bd=0,fg="#0B4E90",width=80,height=1,command=llamar_2)
    boton2.pack(padx=16,pady=0)

    #-- mainloop para que se muestre la ventana --#
    ventana.mainloop()
main_login()