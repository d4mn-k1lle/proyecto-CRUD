from ParaImagenes import frames_imagenes
import tkinter as tk
from bd.config import conectar_bd,verificar_credenciales
from tkinter import messagebox


def obtener_valores(cnx,var_entry1,var_entry2):
    valor_entry1 = var_entry1.get()#usuario
    valor_entry2 = var_entry2.get()#contraseña
    
    return verificar_credenciales(cnx,valor_entry1,valor_entry2)

def main_login():
    #para el segundo boton que destruya la ventana actual y abra la "secundaria" que seria el registro
    def llamar_2():
        fm_i.abrir_archivo()
        fm_i.cerrar_ventana()

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
    camino_imagen="login_intento-legible.8\imagenes\logo_escuela.png"
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
            if obtener_valores(cnx, var_entry1, var_entry2):
                messagebox.showinfo("Éxito", "Login exitoso")
                # Aquí puedes agregar la lógica para abrir una nueva ventana o realizar otras acciones después del login exitoso
            else:
                messagebox.showerror("Error", "Credenciales incorrectas")
            cnx.close()  # Cerrar conexión después de usarla
    
    #-- botton de iniciar sesion y su ubicacion en la ventana --#
    boton1=tk.Button(frame_SurEste,text="Iniciar sesion",font=("Helvetica",15,"bold"),bg="#0B4EBD",bd=0,fg="#fafafa",width=80,height=1,command=registro)
    boton1.pack(padx=16,pady=28)


    #-- boton de registrar usuario y su ubicacion en la ventana--#
    boton2=tk.Button(frame_SurEste,text="Registrar Usuario",font=("Times",14),bg="#fafafa",bd=0,fg="#0B4E90",width=80,height=1,command=llamar_2)
    boton2.pack(padx=16,pady=0)

    #-- mainloop para que se muestre la ventana --#
    ventana.mainloop()
main_login()
