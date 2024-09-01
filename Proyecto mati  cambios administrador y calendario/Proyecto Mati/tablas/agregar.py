import tkinter as tk
from ayudas import *
from bd import crear_conexion, ejecutar_datos, mostrar_tabla
from tkinter import messagebox
from tkcalendar import Calendar
import json
from datetime import date
from tkinter import ttk


def crear_agregar(root, tree, lista_permitidos, nombre_tabla, guardar_cursos):
    fecha_actual = date.today()

    def capitalizar_palabras(event, entry):
        entry.config(validate="none")
        current_text = entry.get()
        capitalized_text = current_text.title()
        entry.delete(0, tk.END)
        entry.insert(0, capitalized_text)
        entry.config(validate="key")

    var_entry1 = tk.StringVar()  # Curso
    var_entry2 = tk.StringVar()  # Nombre/s
    var_entry3 = tk.StringVar()  # Apellido/s
    var_entry4 = tk.StringVar()  # F. Ingreso
    var_entry5 = tk.StringVar()  # DNI
    var_entry6 = tk.StringVar()  # Observaciones

    def obtener_valores(var1, var2, var3, var4, var5, var6):
        curso = combo.get()
        vare1 = curso
        vare2 = var2.get()
        vare3 = var3.get()
        vare4 = var4.get()
        vare5 = var5.get()
        vare6 = var6.get()
        valor_1 = vare1.capitalize()
        valor_2 = vare2.title()
        valor_3 = vare3.title()

        if not curso or curso == "Ingrese un curso":
            label1.config(fg="#f00", text="Curso:*", font=("Times", 14, "underline"))
        else:
            label1.config(fg="#666a88", text="Curso:", font=("Times", 14))

        if not vare2:
            label2.config(fg="#f00", text="Nombre/s:*", font=("Times", 14, "underline"))
        if not vare3:
            label3.config(fg="#f00", text="Apellido/s:*", font=("Times", 14, "underline"))
        if not vare4:
            boton_calendario.config(fg="#f00")
        if not vare5:
            label5.config(fg="#f00", text="DNI:*", font=("Times", 14, "underline"))
        if not vare6:
            label6.config(fg="#f00", text="Observaciones:*", font=("Times", 14, "underline"))

        if vare2:
            label2.config(fg="#666a88", text="Nombre/s:", font=("Times", 14))
        if vare3:
            label3.config(fg="#666a88", text="Apellido/s:", font=("Times", 14))
        if vare4:
            boton_calendario.config(fg="#666a88")
        if vare5:
            label5.config(fg="#666a88", text="DNI:", font=("Times", 14))
        if vare6:
            label6.config(fg="#666a88", text="Observaciones:", font=("Times", 14))

        if not vare6 or not vare5 or not vare4 or not vare3 or not vare2 or not curso or curso == "Ingrese un curso":
            return

        conexion = crear_conexion()

        # Verificar si el DNI ya existe
        consulta = f"SELECT curso, nombres, apellidos, fecha_ingreso, dni, observaciones FROM {nombre_tabla} WHERE dni = {vare5};"
        resultado = mostrar_tabla(conexion, consulta)

        if resultado:
            estudiante_existente = resultado[0]
            curso, nombres, apellidos, fecha_ingreso, dni, observaciones = estudiante_existente

            mensaje = (
                    f"El DNI ingresado ya existe. Datos del estudiante:\n\n"
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

        # Insertar los datos en la base de datos
        valoress = [valor_1, valor_2, valor_3, vare4, vare5, vare6]
        insertar = f"INSERT INTO {nombre_tabla} (curso, nombres, apellidos, fecha_ingreso, dni, observaciones) VALUES ('{valoress[0]}', '{valoress[1]}', '{valoress[2]}', '{valoress[3]}', {valoress[4]}, '{valoress[5]}');"
        ejecutar_datos(conexion, insertar)
        conexion.close()
        top.destroy()

    def solo_letras(char):
        return char.isalpha() or char.isspace()

    top = tk.Toplevel(root)
    top.grab_set()
    top.resizable(False, False)
    top.title("Agregar estudiante")
    top.config(bg="#fff")
    top.geometry("460x610+89+50")

    frame_superior = tk.Frame(top, width=460, height=90, bg="#fff")
    frame_superior.pack(side="top")
    frame_superior.pack_propagate(False)

    titulo = tk.Label(frame_superior, text="Ingresar Estudiante", font=("Times", 39, "italic bold"), bg="#fff", fg="#3C5BBA")
    titulo.place(relx=0.5, rely=0.45, anchor="center")

    frame_inferior = tk.Frame(top, width=460, height=490, bg="#fff")
    frame_inferior.pack(side="top")

    validate_cmd = top.register(solo_numeros)

    new_frame = crear_frame_auxiliar(frame_inferior, 60)
    label1 = tk.Label(new_frame, text="Curso:", font=("Times", 14), fg="#666a88", bg="#fff")
    label1.place(relx=0.065, rely=0.0)

    def ventana_entry(opciones):
        def guardar_opciones(opciones):
            with open(f'{guardar_cursos}.json', 'w') as file:
                json.dump(opciones, file)

        def obtener_curso():
            nueva_opcion = var_entry1.get()
            opciones = cargar_opciones()
            if nueva_opcion and nueva_opcion not in opciones:
                opciones.append(nueva_opcion)
                combo['values'] = opciones
                guardar_opciones(opciones=opciones)
                entry1.delete(0, tk.END)
                top3.destroy()

        def cargar_opciones():
            try:
                with open(f'{guardar_cursos}.json', 'r') as file:
                    return json.load(file)
            except FileNotFoundError:
                return []

        top3 = tk.Toplevel(top)
        top3.geometry("260x150")
        top3.title("Agregar Curso")
        top3.config(bg="#fff")
        tt = tk.Label(top3, text="Agregar un curso", font=("Times", 21, "italic bold"), bg="#fff", fg="#3C5BBA")
        tt.place(relx=0.5, rely=0.2, anchor="center")
        entry1 = tk.Entry(top3, textvariable=var_entry1, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
        entry1.place(relx=0.019, rely=0.5, relwidth=0.95)
        btnn = tk.Button(top3, text="Ingresar curso", bg="#3C5BBA", fg="#fff", font=("Helvetica", 10, "bold"), pady=1, bd=2, relief="flat", activebackground="#fff", activeforeground="#3C5BBA", overrelief="solid", width=30, command=lambda: obtener_curso())
        btnn.place(relx=0.5, rely=0.86, anchor="center")

        top3.mainloop()

    opcion = []
    try:
        with open(f'{guardar_cursos}.json', 'r') as file:
            opcion = json.load(file)
    except FileNotFoundError:
        pass

    def guardar_opciones2():
        with open(f'{guardar_cursos}.json', 'w') as file:
            json.dump(opcion, file)

    def eliminar_opcion():
        seleccion = combo.get()
        confirmacion = messagebox.askyesno("Confirmación", f"¿Estás seguro de que deseas eliminar '{seleccion}'?")
        if confirmacion:
            if seleccion in opcion:
                opcion.remove(seleccion)
                combo['values'] = opcion
                guardar_opciones2()
                combo.set('')
            combo.set('Ingrese un curso')

    btn = tk.Button(new_frame, text="Agregar Curso", bd=1, relief="solid", bg="#fff", fg="#666a88", font=("Cambria", 10, "bold"), padx=4, pady=1, command=lambda: ventana_entry(opcion))
    btn.place(relx=0.52, rely=0.6, anchor="center")
    btn2 = tk.Button(new_frame, text="Eliminar Curso", bd=1, relief="solid", bg="#fff", fg="#666a88", font=("Cambria", 10, "bold"), padx=4, pady=1, command=lambda: eliminar_opcion())
    btn2.place(relx=0.79, rely=0.6, anchor="center")

    combo = ttk.Combobox(new_frame, values=opcion, state="readonly")
    combo.set("Ingrese un curso")
    combo.place(rely=0.6, relx=0.2, anchor="center")

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
    entry2.bind('<KeyRelease>', lambda event: capitalizar_palabras(event, entry2))

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
    entry3.bind('<KeyRelease>', lambda event: capitalizar_palabras(event, entry3))

    new_frame4 = crear_frame_auxiliar(frame_inferior, 60)
    boton_calendario = tk.Button(new_frame4, text="Fecha de ingreso", width=25, bd=1, relief="solid", bg="#fff", fg="#666a88", font=("Cambria", 16, "bold"), command=lambda: calendario(var_entry4))
    boton_calendario.place(rely=0.55, relx=0.5, anchor="center")

    def calendario(var_entry4):
        def obtener_fecha(calendari, var_entry4):
            fecha_seleccionada = calendari.get_date()
            boton_calendario.config(text=f"{fecha_seleccionada}")
            fecha_sin_barras = fecha_seleccionada.replace('/', '')
            var_entry4.set(fecha_sin_barras)
            top2.destroy()
            top.grab_set()

        top2 = tk.Toplevel(top)
        top2.geometry("260x245+550+200")
        top2.config(bg="#fff")
        top2.resizable(False, False)
        top2.grab_set()
        calendario = Calendar(top2, selectmode='day', date_pattern='dd/mm/yyyy', locale='es', background="#fff", foreground="#000", weekendbackground='#fff', othermonthbackground='#fff', daybackground="#fff", showweeknumbers=False, selectbackground="#eee", selectforeground="#000", bordercolor="#fff", headersbackground="#fff", othermonthwebackground="#fff", font=("cambria", 11, "italic"), maxdate=fecha_actual)
        calendario.pack(side="top")
        botonsito = tk.Button(top2, text="Definir Fecha", bg="#3C5BBA", fg="#fff", font=("Helvetica", 11, "bold"), pady=0, bd=2, relief="flat", activebackground="#fff", activeforeground="#3C5BBA", overrelief="solid", width=26, command=lambda: obtener_fecha(calendario, var_entry4))
        botonsito.place(rely=0.88, relx=0.5, anchor="center")

    # Quinto entry (DNI)
    new_frame5 = crear_frame_auxiliar(frame_inferior, 60)
    validacion = new_frame5.register(solo_letras)
    img = imagen(4)
    label_img5 = tk.Label(new_frame5, image=img, bg="#fff")
    label_img5.image = img
    label_img5.place(relx=0.016, rely=0.0)

    label5 = tk.Label(new_frame5, text="DNI:", font=("Times", 14), fg="#666a88", bg="#fff")
    label5.place(relx=0.065, rely=0.0)

    entry5 = tk.Entry(new_frame5, textvariable=var_entry5, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
    entry5.place(relx=0.015, rely=0.5, relwidth=0.95)

    new_frame6 = crear_frame_auxiliar(frame_inferior, 150)
    img = imagen(5)
    label_img6 = tk.Label(new_frame6, image=img, bg="#fff")
    label_img6.image = img
    label_img6.place(relx=0.015, rely=0.0)
    label6 = tk.Label(new_frame6, text="Observaciones:", font=("Times", 14), fg="#666a88", bg="#fff")
    label6.place(relx=0.065, rely=0.0)
    textarea = tk.Text(new_frame6, font=("Times", 14), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, height=5)
    textarea.place(relx=0.015, rely=0.18, relwidth=0.95)
    textarea.bind("<KeyRelease>", lambda event: actualizar_textvar(event, textarea, var_entry6))

    boton_ingresar = tk.Button(top, text="Ingresar Estudiante", bg="#3C5BBA", fg="#fff", font=("Helvetica", 18, "bold"), pady=2, bd=2, relief="flat", activebackground="#fff", activeforeground="#3C5BBA", overrelief="solid", command=lambda: obtener_valores(var_entry1, var_entry2, var_entry3, var_entry4, var_entry5, var_entry6))
    boton_ingresar.place(relx=0.5, rely=0.93, anchor="center", relwidth=0.97)

    top.mainloop()