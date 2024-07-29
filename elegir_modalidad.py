import tkinter as tk
from PIL import Image,ImageTk

def pantalla_principal():
    #-- creamos la ventana donde va estar ubicado todo --#
    ventana=tk.Tk()
    ventana.title("Inicio")
    ventana.geometry("740x560")
    ventana.resizable(False,False)#no se puede achicar ni agrandar


    #--#--#--#


    #-- creamos el frame donde va estar el titulo y el logo de la escuela--#
    frame_titulo=tk.Frame(ventana,height=130,bg="#3C5BBA")
    frame_titulo.pack(side="top",fill="both")
    frame_titulo.pack_propagate(False)

    #-- creamos el titulo EESTN1 y lo ubicamos dentro del frame--#
    titulo=tk.Label(frame_titulo,text="EESTNº1",bg="#3C5BBA",font=("Cambria",50,"bold"),fg="#041C65")
    titulo.place(relx=0.17,rely=0.012,)

    #-- creamos el subtitulo detallanod cada una de las letras de eestn1  y lo ubicamos en el frame--#
    subtitulo=tk.Label(frame_titulo,text="Escuela Tecnica Manuel Belgrano Nro1",bg="#3C5BBA",font=("Cambria",14,"bold"),fg="#041C65")
    subtitulo.place(relx=0.119,rely=0.65)


    #--#--#--#


    #-- creamos un frame para el logo dentro del frame del titulo y hacemos que no se pueda achicar ni agrandar --#
    frame_logo=tk.Frame(frame_titulo,width=200,height=130,bg="#3C5BBA")
    frame_logo.pack(side=tk.RIGHT)
    frame_logo.pack_propagate(False)

    #-- le damos la ruta de la imagen y lo metemos en image --# 
    image_path = "login_intento-legible.8/imagenes/logo_escuela.png" 
    image = Image.open(image_path)

    #-- le damos el tamaño y la achicamos con calidad con lanczos --#
    new_size = (115,120)  #
    resized_image = image.resize(new_size, Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)

    #-- la metemos en un label para que se vea y ubicamos el label en el centro del frame del logo --#
    image_label = tk.Label(frame_logo, image=photo,bg="#3C5BBA")
    # image_label.image = photo  esta asi pq no la considero necesaria
    image_label.place(relx=0.5, rely=0.5, anchor='center')


    #--#--#--#


    #-- creamos el frame para los botones y los nombres de los integrantes --#
    frame_botones=tk.Frame(ventana,width=740,height=430,bg="#C6CFE9",bd=1,relief=tk.SOLID)
    frame_botones.pack(side="bottom",fill="x")
    frame_botones.pack_propagate(False)

    #-- creamos un label para que no quede tan vacio arriba en este mismo frame --#
    titulo_elegir=tk.Label(frame_botones,text="Por favor, elija la opción deseada:",bg="#C6CFE9",font=("Book Antiqua",22,"bold"),fg="#222")
    titulo_elegir.place(relx=0.04,rely=0.04)
    
    #-- Se crea el label del curso y año  
    CursoProgramacion = tk.Label(ventana,
                text = "5*3 Progracion 2024",
                fg="#1d1d1d",
                bg="#B5BED6",
                font=("Times",14,"italic bold"),
                width=15,
                height=2)
    CursoProgramacion.place(relx=0.75, rely=0.906)
    
    

    #-- creamos el boton de ciclo basico --#
    boton_basico=tk.Button(frame_botones,text="Basico",font=("Times",14,"bold"),width=15,height=2,bg="#fff",fg="#111",borderwidth=2,relief="flat",activebackground="#fff",activeforeground="#111", overrelief="solid")
    boton_basico.place(relx=0.07,rely=0.20)

    #-- creamos el boton de MMO --#
    boton_MMO=tk.Button(frame_botones,text="MMO",font=("Times",14,"bold"),width=15,height=2,bg="#fff",fg="#111",borderwidth=2,relief="flat",activebackground="#fff",activeforeground="#111", overrelief="solid")
    boton_MMO.place(relx=0.39,rely=0.20)

    #-- creamos el boton de informatica --#
    boton_informatica=tk.Button(frame_botones,text="Informatica",font=("Times",14,"bold"),width=15,height=2,bg="#fff",fg="#111",borderwidth=2,relief="flat",activebackground="#fff",activeforeground="#111", overrelief="solid")
    boton_informatica.place(relx=0.07,rely=0.46)

    #-- creamos el boton de programacion --#
    boton_programacion=tk.Button(frame_botones,text="Programacion",font=("Times",14,"bold"),width=15,height=2,bg="#fff",fg="#111",borderwidth=2,relief="flat",activebackground="#fff",activeforeground="#111", overrelief="solid")
    boton_programacion.place(relx=0.39,rely=0.46)

    #-- creamos el boton de egresados --#
    boton_egresados=tk.Button(frame_botones,text="Egresados",font=("Times",14,"bold"),width=15,height=2,bg="#fff",fg="#111",borderwidth=2,relief="flat",activebackground="#fff",activeforeground="#111", overrelief="solid")
    boton_egresados.place(relx=0.07,rely=0.72)

    #-- creamos el boton de exalumnos --#
    boton_exalumnos=tk.Button(frame_botones,text="Exalumnos",font=("Times",14,"bold"),width=15,height=2,bg="#fff",fg="#111",borderwidth=2,relief="flat",activebackground="#fff",activeforeground="#111", overrelief="solid")
    boton_exalumnos.place(relx=0.39,rely=0.72)


    #--#--#--#


    #-- creamos el frame donde van a estar los integrantes --#
    frame_integrantes=tk.Frame(frame_botones,width=205,height=430,bg="#B5BED6")
    frame_integrantes.pack(side="right")

    #-- el label para integrantes del proyecto y lo ubicamos --#
    integrantes=tk.Label(frame_integrantes,text="Integrantes\n del proyecto:",font=("Cambria",20,"italic"),bg="#B5BED6",fg="#111")
    frame_integrantes.pack_propagate(False)
    integrantes.place(relx=0.49,rely=0.13,anchor="center")

    #-- creamos el label del primer integrante --#
    integrante1=tk.Label(frame_integrantes,text="-Matias Gauto",font=("Cambria",14,),bg="#B5BED6",fg="#1d1d1d")
    integrante1.place(relx=0.08,rely=0.27)

    #-- creamos el label del segundo integrante --#
    integrante2=tk.Label(frame_integrantes,text="-Aramis Lanas",font=("Cambria",14,),bg="#B5BED6",fg="#1d1d1d")
    integrante2.place(relx=0.08,rely=0.34)

    #-- creamos el label del tercer integrante --#
    integrante3=tk.Label(frame_integrantes,text="-Belenger Hernandez",font=("Cambria",14,),bg="#B5BED6",fg="#1d1d1d")
    integrante3.place(relx=0.08,rely=0.41)

    #-- creamos el label del cuarto integrante --#
    integrante4=tk.Label(frame_integrantes,text="-Matias Cardozo",font=("Cambria",14,),bg="#B5BED6",fg="#1d1d1d")
    integrante4.place(relx=0.08,rely=0.48)

    #-- creamos el label del quinto integrante --#
    integrante5=tk.Label(frame_integrantes,text="-Tiziano Cavallo",font=("Cambria",14,),bg="#B5BED6",fg="#1d1d1d")
    integrante5.place(relx=0.08,rely=0.55)

    #-- creamos el label del sexto integrante --#
    integrante6=tk.Label(frame_integrantes,text="-Gonzalo Cardozo",font=("Cambria",14,),bg="#B5BED6",fg="#1d1d1d")
    integrante6.place(relx=0.08,rely=0.62)

    #-- creamos el label del septimo integrante --#
    integrante7=tk.Label(frame_integrantes,text="-Marien Persico",font=("Cambria",14,),bg="#B5BED6",fg="#1d1d1d")
    integrante7.place(relx=0.08,rely=0.69)

    #-- creamos el label del octavo integrante --#
    integrante8=tk.Label(frame_integrantes,text="-Miranda Lopez",font=("Cambria",14,),bg="#B5BED6",fg="#1d1d1d")
    integrante8.place(relx=0.08,rely=0.76)

    #-- creamos el label del noveno integrante --#
    integrante9=tk.Label(frame_integrantes,text="-Ian Aaron Celi",font=("Cambria",14,),bg="#B5BED6",fg="#1d1d1d")
    integrante9.place(relx=0.08,rely=0.83)




    #mostramos la ventana
    ventana.mainloop()
    
pantalla_principal()