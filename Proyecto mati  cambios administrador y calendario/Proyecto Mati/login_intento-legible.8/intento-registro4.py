import tkinter as tk
from ParaImagenes import frames_imagenes
from bd.config import conectar_bd, insert_data, verificar_usuario_existente
from tkinter import messagebox

def llamar_2():
    fm_i.abrir_archivo_registro()
    fm_i.cerrar_ventana()

# conectamos a la base de datos
cnx = conectar_bd()

# creamos la ventana
ventana = tk.Tk()
fm_i = frames_imagenes(ventana, 420, 560)
fm_i.centrar_ventana()
ventana.title("Registro")
ventana.resizable(width=False, height=False)  # que no se pueda agrandar ni achicar la ventana

# -- creamos la funcion que lo que hace es agarra de la lista y utiliza la funcion leer imagen y le asignamos un tamaño de 20x20px -- #
def imagen(i):
    camino_imagen=["Proyecto Mati\login_intento-legible.8\imagenes/nombre.png",
                   "Proyecto Mati\login_intento-legible.8\imagenes/apellido.png",
                   "Proyecto Mati\login_intento-legible.8\imagenes/usuario.png",
                   "Proyecto Mati\login_intento-legible.8\imagenes/confirmacion_redonda.png",
                   "Proyecto Mati\login_intento-legible.8\imagenes/contraseña.png",
                   "Proyecto Mati\login_intento-legible.8\imagenes/confirmacion_redonda.png",
                   "Proyecto Mati\login_intento-legible.8\imagenes/email.png"]
    img = fm_i.leer_imagen(camino_imagen[i], (20, 20))
    return img

def obtener_valores(var_entry1, var_entry2, var_entry3, var_entry4, var_entry5, var_entry6, var_entry7):
    # Se guardan los valores de los var_entry en los valor_entry
    valor_entry1 = var_entry1.get()  # Nombre
    valor_entry2 = var_entry2.get()  # Apellido
    valor_entry3 = var_entry3.get()  # Usuario
    valor_entry4 = var_entry4.get()  # Conf usuario
    valor_entry5 = var_entry5.get()  # Contraseña
    valor_entry6 = var_entry6.get()  # Conf contraseña
    valor_entry7 = var_entry7.get()  # Email

    # Verificar si alguno de los campos está vacío
    if any(v == "" for v in [valor_entry1, valor_entry2, valor_entry3, valor_entry5, valor_entry7]):
        messagebox.showerror("ERROR", "Hay campos sin completar")
        return

    # Verificar formato del email (endswith Sirve para comprobar si una cadena termina con un texto específico, en este caso dominios_permitidos )
    dominios_permitidos = ["gmail.com", ".gob.ar"]
    if not ("@" in valor_entry7 and any(valor_entry7.endswith(dominio) for dominio in dominios_permitidos)):
        messagebox.showerror("ERROR", "El gmail es invalido.")
        return

    # Verificar si los campos coinciden y si el email es válido
    if (valor_entry3 == valor_entry4 and valor_entry5 == valor_entry6):
        if verificar_usuario_existente(cnx, valor_entry3):
            messagebox.showerror("Error", f"El usuario '{valor_entry3}' ya existe")
        else:
            insert_data(cnx, valor_entry1, valor_entry2, valor_entry4, valor_entry5, valor_entry7)
            messagebox.showinfo("Aviso", "Los datos han sido guardados exitosamente")
            llamar_2()
    else:
        messagebox.showerror("ERROR", "Los datos ingresados son inválidos, vuelva a intentarlo")

def main():
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

    entry1 = tk.Entry(new_frame, textvariable=var_entry1, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry1.place(relx=0.02, rely=0.5, relwidth=0.95)
    # -- Fin del primer frame -- #

    # -- Segundo frame -- #    
    new_frame2 = fm_i.crear_frame_auxiliar(frame_restante, 50)
    img2 = imagen(1)
    label_img2 = tk.Label(new_frame2, image=img2)
    label_img2.configure(bg="#f0f0f0")
    label_img2.place(relx=0.01, rely=0.0)

    label2 = tk.Label(new_frame2, text="Apellido:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
    label2.place(relx=0.06, rely=0.0)

    entry2 = tk.Entry(new_frame2, textvariable=var_entry2, font=("Times", 11), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry2.place(relx=0.02, rely=0.5, relwidth=0.95)
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

    # -- Quinto frame -- #
    new_frame5 = fm_i.crear_frame_auxiliar(frame_restante, 50)
    img5 = imagen(4)
    label_img5 = tk.Label(new_frame5, image=img5)
    label_img5.configure(bg="#f0f0f0")
    label_img5.place(relx=0.01, rely=0.0)

    label5 = tk.Label(new_frame5, text="Contraseña:", font=("Times", 12), fg="#666a88", bg="#f0f0f0")
    label5.place(relx=0.06, rely=0.0)

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
        obtener_valores(var_entry1, var_entry2, var_entry3, var_entry4, var_entry5, var_entry6, var_entry7)

    bt_guardar = tk.Button(frame_restante, text="Crear usuario", width=400, bg="#226EAD", fg="#f0f0f0", font=("Helvetica", 14), bd=0, command=obt_val)
    bt_guardar.pack(pady=18, padx=7)

    bt_volver = tk.Button(frame_restante, text="Volver al login", width=100, bg="#f0f0f0", fg="#226EAD", font=("Helvetica", 12, "bold"), bd=0, command=llamar_2)
    bt_volver.pack(pady=0, padx=7)
    ventana.mainloop()

main()
