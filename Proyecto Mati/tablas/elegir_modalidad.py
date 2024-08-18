import tkinter as tk
from PIL import Image, ImageTk

from ayudas import abrir_archivo

def pantalla_principal():
    #-- creamos la ventana donde va a estar ubicado todo --#
    ventana = tk.Tk()
    ventana.title("Inicio")
    ventana.geometry("740x560")
    ventana.resizable(False, False)  # No se puede achicar ni agrandar

    #--#--#--#

    #-- creamos el frame donde va a estar el título y el logo de la escuela--#
    frame_titulo = tk.Frame(ventana, height=130, bg="#3C5BBA")
    frame_titulo.pack(side="top", fill="both")
    frame_titulo.pack_propagate(False)

    #-- creamos el título EESTN1 y lo ubicamos dentro del frame--#
    titulo = tk.Label(frame_titulo, text="EESTNº1", bg="#3C5BBA", font=("Cambria", 50, "bold"), fg="#041C65")
    titulo.place(relx=0.17, rely=0.012)

    #-- creamos el subtítulo detallando cada una de las letras de EESTN1 y lo ubicamos en el frame--#
    subtitulo = tk.Label(frame_titulo, text="Escuela Tecnica Manuel Belgrano Nro1", bg="#3C5BBA", font=("Cambria", 14, "bold"), fg="#041C65")
    subtitulo.place(relx=0.119, rely=0.65)

    #--#--#--#

    #-- creamos un frame para el logo dentro del frame del título y hacemos que no se pueda achicar ni agrandar --#
    frame_logo = tk.Frame(frame_titulo, width=200, height=130, bg="#3C5BBA")
    frame_logo.pack(side=tk.RIGHT)
    frame_logo.pack_propagate(False)

    #-- le damos la ruta de la imagen y lo metemos en image --# 
    image_path = "Proyecto Mati\\login_intento-legible.8\\imagenes\\logo_escuela.png" 
    image = Image.open(image_path)

    #-- le damos el tamaño y la achicamos con calidad con Lanczos --#
    new_size = (115, 120) 
    resized_image = image.resize(new_size, Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)

    #-- la metemos en un label para que se vea y ubicamos el label en el centro del frame del logo --#
    image_label = tk.Label(frame_logo, image=photo, bg="#3C5BBA")
    image_label.image = photo  # Necesario para mantener la referencia de la imagen
    image_label.place(relx=0.5, rely=0.5, anchor='center')

    #--#--#--#

    #-- creamos el frame para los botones y los nombres de los integrantes --#
    frame_botones = tk.Frame(ventana, width=740, height=430, bg="#C6CFE9", bd=1, relief=tk.SOLID)
    frame_botones.pack(side="bottom", fill="x")
    frame_botones.pack_propagate(False)

    #-- creamos un label para que no quede tan vacío arriba en este mismo frame --#
    titulo_elegir = tk.Label(frame_botones, text="Por favor, elija la opción deseada:", bg="#C6CFE9", font=("Book Antiqua", 22, "bold"), fg="#222")
    titulo_elegir.place(relx=0.04, rely=0.04)

    #-- Se crea el label del curso y año --#
    CursoProgramacion = tk.Label(ventana,
                                 text="5*3 Programación 2024",
                                 fg="#1d1d1d",
                                 bg="#B5BED6",
                                 font=("Times", 14, "italic bold"),
                                 width=15,
                                 height=2)
    CursoProgramacion.place(relx=0.75, rely=0.906)

    #-- creamos los botones de las distintas secciones --#
    boton_basico = tk.Button(frame_botones, text="Básico", font=("Times", 14, "bold"), width=15, height=2, bg="#fff", fg="#111",
                             borderwidth=2, relief="flat", activebackground="#fff", activeforeground="#111", overrelief="solid",
                             command=lambda: abrir_archivo(ventana, r"Proyecto Mati\\tablas\\tabla_basico.py"))
    boton_basico.place(relx=0.07, rely=0.20)

    boton_MMO = tk.Button(frame_botones, text="MMO", font=("Times", 14, "bold"), width=15, height=2, bg="#fff", fg="#111",
                          borderwidth=2, relief="flat", activebackground="#fff", activeforeground="#111", overrelief="solid",
                          command=lambda: abrir_archivo(ventana, r"Proyecto Mati\\tablas\\tabla_MMO.py"))
    boton_MMO.place(relx=0.39, rely=0.20)

    boton_informatica = tk.Button(frame_botones, text="Informática", font=("Times", 14, "bold"), width=15, height=2, bg="#fff", fg="#111",
                                  borderwidth=2, relief="flat", activebackground="#fff", activeforeground="#111", overrelief="solid",
                                  command=lambda: abrir_archivo(ventana, r"Proyecto Mati\\tablas\\tabla_informatica.py"))
    boton_informatica.place(relx=0.07, rely=0.46)

    boton_programacion = tk.Button(frame_botones, text="Programación", font=("Times", 14, "bold"), width=15, height=2, bg="#fff", fg="#111",
                                   borderwidth=2, relief="flat", activebackground="#fff", activeforeground="#111", overrelief="solid",
                                   command=lambda: abrir_archivo(ventana, r"Proyecto Mati\\tablas\\tabla_programacion.py"))
    boton_programacion.place(relx=0.39, rely=0.46)

    boton_egresados = tk.Button(frame_botones, text="Egresados", font=("Times", 14, "bold"), width=15, height=2, bg="#fff", fg="#111",
                                borderwidth=2, relief="flat", activebackground="#fff", activeforeground="#111", overrelief="solid",
                                command=lambda: abrir_archivo(ventana, r"Proyecto Mati\\tablas\\tabla_egresados.py"))
    boton_egresados.place(relx=0.07, rely=0.72)

    boton_e_pases = tk.Button(frame_botones, text="E.Pases", font=("Times", 14, "bold"), width=15, height=2, bg="#fff", fg="#111",
                              borderwidth=2, relief="flat", activebackground="#fff", activeforeground="#111", overrelief="solid",
                              command=lambda: abrir_archivo(ventana, r"Proyecto Mati\\tablas\\tabla_e_pases.py"))
    boton_e_pases.place(relx=0.39, rely=0.72)

    #--#--#--#

    #-- creamos el frame donde van a estar los integrantes --#
    frame_integrantes = tk.Frame(frame_botones, width=205, height=430, bg="#B5BED6")
    frame_integrantes.pack(side="right")
    frame_integrantes.pack_propagate(False)

    #-- el label para integrantes del proyecto y lo ubicamos --#
    integrantes = tk.Label(frame_integrantes, text="Integrantes\n del proyecto:", font=("Cambria", 20, "italic"), bg="#B5BED6", fg="#111")
    integrantes.place(relx=0.49, rely=0.13, anchor="center")

    #-- creamos los labels para cada integrante --#
    nombres_integrantes = [
        "-Matias Gauto", "-Tiziano Cavallo", "-Belenger Hernandez", "-Aramis Lanas",
        "-Miranda Lopez", "-Marien Persico", "-Matias Cardozo", "-Gonzalo Cardozo",
        "-Ian Aaron Celi"
    ]

    for i, nombre in enumerate(nombres_integrantes):
        tk.Label(frame_integrantes, text=nombre, font=("Cambria", 14), bg="#B5BED6", fg="#1d1d1d").place(relx=0.08, rely=0.27 + (i * 0.07))

    #-- mostramos la ventana --#
    ventana.mainloop()

pantalla_principal()
