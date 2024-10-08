import tkinter as tk
from tkinter import ttk
from ayudas import *
from bd import crear_conexion, ejecutar_datos, mostrar_tabla
from tkinter import messagebox
from tkcalendar import Calendar

def obtener_lista_cursos():
    conexion = crear_conexion()
    consultas = [
        "SELECT DISTINCT curso FROM basico;",
        "SELECT DISTINCT curso FROM egresados;",
        "SELECT DISTINCT curso FROM e_pases;",
        "SELECT DISTINCT curso FROM informatica;",
        "SELECT DISTINCT curso FROM mmo;",
        "SELECT DISTINCT curso FROM programacion;"
    ]
    
    cursos = []
    for consulta in consultas:
        resultados = mostrar_tabla(conexion, consulta)
        cursos.extend([resultado[0] for resultado in resultados])
    
    conexion.close()
    return cursos

def crear_agregar(root, tree, lista_permitidos):
    var_entry1 = tk.StringVar()  # Curso
    var_entry1.set(lista_permitidos[0])  # Valor inicial por defecto
    var_entry2 = tk.StringVar()  # Nombre/s
    var_entry3 = tk.StringVar()  # Apellido/s
    var_entry4 = tk.StringVar()  # F. Ingreso
    var_entry5 = tk.StringVar()  # DNI
    var_entry6 = tk.StringVar()  # Observaciones

    cursos = obtener_lista_cursos()
    if not cursos:
        cursos = lista_permitidos  # Si no hay cursos en la base de datos, usar lista de permitidos

    def obtener_valores(var1, var2, var3, var4, var5, var6):
        vare1 = var1.get()
        vare2 = var2.get()
        vare3 = var3.get()
        vare4 = var4.get()
        vare5 = var5.get()
        vare6 = var6.get()
        valor_1 = vare1.capitalize()
        valor_2 = vare2.title()
        valor_3 = vare3.title()

        if valor_1 in lista_permitidos:
            conexion = crear_conexion()

            # Modificación: Verificar si el DNI ya existe en alguna de las tablas
            consulta = f"""
            SELECT 'basico' AS tabla, curso, nombres, apellidos, fecha_ingreso, dni, observaciones FROM basico WHERE dni = {vare5}
            UNION
            SELECT 'egresados' AS tabla, curso, nombres, apellidos, fecha_ingreso, dni, observaciones FROM egresados WHERE dni = {vare5}
            UNION
            SELECT 'e_pases' AS tabla, curso, nombres, apellidos, fecha_ingreso, dni, observaciones FROM e_pases WHERE dni = {vare5}
            UNION
            SELECT 'informatica' AS tabla, curso, nombres, apellidos, fecha_ingreso, dni, observaciones FROM informatica WHERE dni = {vare5}
            UNION
            SELECT 'mmo' AS tabla, curso, nombres, apellidos, fecha_ingreso, dni, observaciones FROM mmo WHERE dni = {vare5}
            UNION
            SELECT 'programacion' AS tabla, curso, nombres, apellidos, fecha_ingreso, dni, observaciones FROM programacion WHERE dni = {vare5};
            """
            resultado = mostrar_tabla(conexion, consulta)

            if resultado:
                estudiante_existente = resultado[0]  # Obtener los datos del primer estudiante con ese DNI
                tabla, curso, nombres, apellidos, fecha_ingreso, dni, observaciones = estudiante_existente

                # Mostrar mensaje indicando que el DNI ya existe y mostrar los datos del estudiante
                mensaje = (
                    f"El DNI ingresado ya existe en la tabla {tabla}. Datos del estudiante:\n\n"
                    f"Curso: {curso}\n"
                    f"Nombres: {nombres}\n"
                    f"Apellidos: {apellidos}\n"
                    f"Fecha de Ingreso: {fecha_ingreso}\n"
                    f"DNI: {dni}\n"
                    f"Observaciones: {observaciones}\n\n"
                    "¿Desea agregar el estudiante de todos modos?"
                )
                continuar = messagebox.askyesno("DNI existente", mensaje)
                if not continuar:
                    conexion.close()
                    return

            # Insertar datos si el usuario decidió continuar o si el DNI no existía
            valoress = [valor_1, valor_2, valor_3, vare4, vare5, vare6]
            insertar = f"INSERT INTO basico (curso, nombres, apellidos, fecha_ingreso, dni, observaciones) VALUES ('{valoress[0]}', '{valoress[1]}', '{valoress[2]}', '{valoress[3]}', {valoress[4]}, '{valoress[5]}');"
            ejecutar_datos(conexion, insertar)
            top.destroy()
        else:
            messagebox.showerror("Error", "El primer dato es inválido")
    
    def solo_letras(char):
        return char.isalpha() or char.isspace()

    def calendario(var_entry4):
        def obtener_fecha(calendario, var_entry4):
            fecha_seleccionada = calendario.get_date()
            fecha_sin_barras = fecha_seleccionada.replace('/', '')
            var_entry4.set(fecha_sin_barras)
            top2.destroy()
        top2 = tk.Toplevel(top)
        top2.geometry("260x245+550+200")
        top2.config(bg="#fff")
        top2.resizable(False, False)
        top2.grab_set()
        calendario = Calendar(top2, selectmode='day', date_pattern='dd/mm/yyyy', locale='es', background="#fff", foreground="#000", weekendbackground='#fff', othermonthbackground='#fff', daybackground="#fff", showweeknumbers=False, selectbackground="#eee", selectforeground="#000", bordercolor="#fff", headersbackground="#fff", othermonthwebackground="#fff", font=("cambria", 11, "italic"))
        calendario.pack(side="top")
        botonsito = tk.Button(top2, text="Definir Fecha", bg="#3C5BBA", fg="#fff", font=("Helvetica", 11, "bold"), pady=0, bd=2, relief="flat", activebackground="#fff", activeforeground="#3C5BBA", overrelief="solid", width=26, command=lambda: obtener_fecha(calendario, var_entry4))
        botonsito.place(rely=0.88, relx=0.5, anchor="center")
    
    top = tk.Toplevel(root)
    top.grab_set()
    top.resizable(False, False)
    top.title("Agregar estudiante")
    top.config(bg="#fff")
    top.geometry("460x610")
    
    frame_superior = tk.Frame(top, width=460, height=90, bg="#fff")
    frame_superior.pack(side="top")
    frame_superior.pack_propagate(False)
    
    titulo = tk.Label(frame_superior, text="Ingresar Estudiante", font=("Times", 39, "italic bold"), bg="#fff", fg="#3C5BBA")
    titulo.place(relx=0.5, rely=0.45, anchor="center")
    
    frame_inferior = tk.Frame(top, width=460, height=490, bg="#fff")
    frame_inferior.pack(side="top")
    
    validate_cmd = top.register(solo_numeros)
    
    new_frame = crear_frame_auxiliar(frame_inferior, 60)
    
    # Crear el menú desplegable para los cursos
    tk.Label(new_frame, text="Curso", font=("Times", 14), fg="#666a88", bg="#fff").pack(anchor="w", padx=10, pady=5)
    curso_menu = tk.OptionMenu(new_frame, var_entry1, *cursos)
    curso_menu.config(font=("Times", 13), bg="#fff", fg="#222")
    curso_menu.pack(anchor="w", padx=10, pady=0, fill='x')
    
    new_frame2 = crear_frame_auxiliar(frame_inferior, 60)
    validacion = new_frame2.register(solo_letras)
    img = imagen(1)
    label_img = tk.Label(new_frame2, image=img, bg="#fff")
    label_img.image = img
    label_img.place(relx=0.015, rely=0.0)
    label2 = tk.Label(new_frame2, text="Nombre/s:", font=("Times", 14), fg="#666a88", bg="#fff")
    label2.place(relx=0.065, rely=0.0)
    entry2 = tk.Entry(new_frame2, textvariable=var_entry2, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validacion, '%S'))
    entry2.place(relx=0.015, rely=0.5, relwidth=0.95)
    
    new_frame3 = crear_frame_auxiliar(frame_inferior, 60)
    validacion = new_frame3.register(solo_letras)
    img = imagen(2)
    label_img3 = tk.Label(new_frame3, image=img, bg="#fff")
    label_img3.image = img
    label_img3.place(relx=0.015, rely=0.0)
    label3 = tk.Label(new_frame3, text="Apellido/s:", font=("Times", 14), fg="#666a88", bg="#fff")
    label3.place(relx=0.065, rely=0.0)
    entry3 = tk.Entry(new_frame3, textvariable=var_entry3, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validacion, '%S'))
    entry3.place(relx=0.015, rely=0.5, relwidth=0.95)
    
    new_frame4 = crear_frame_auxiliar(frame_inferior, 60)
    boton_calendario = tk.Button(new_frame4, text="Fecha de ingreso", width=25, bd=1, relief="solid", bg="#fff", fg="#666a88", font=("Cambria", 16, "bold"), command=lambda: calendario(var_entry4))
    boton_calendario.place(rely=0.55, relx=0.5, anchor="center")
    
    new_frame5 = crear_frame_auxiliar(frame_inferior, 60)
    crear_entry_con_img(new_frame5, 4, 0.016, 0.0, "DNI", 0.065, 0.0, var_entry5, 0.015, 0.5, 0.95, validate_cmd, only_numbers=True)
    
    new_frame6 = crear_frame_auxiliar(frame_inferior, 150)
    crear_textarea_con_img(new_frame6, 5, 0.015, 0.0, "Observaciones:", 0.065, 0.0, var_entry6, 0.015, 0.18, 0.95, 5)
    
    boton_ingresar = tk.Button(top, text="Ingresar Estudiante", bg="#3C5BBA", fg="#fff", font=("Helvetica", 18, "bold"), pady=2, bd=2, relief="flat", activebackground="#fff", activeforeground="#3C5BBA", overrelief="solid", command=lambda: obtener_valores(var_entry1, var_entry2, var_entry3, var_entry4, var_entry5, var_entry6))
    boton_ingresar.place(relx=0.5, rely=0.93, anchor="center", relwidth=0.97)
    
    top.mainloop()