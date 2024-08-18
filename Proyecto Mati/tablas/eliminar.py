import tkinter as tk
from ayudas import *
from bd import crear_conexion, ejecutar_datos
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime

def crear_eliminar(root, tree):
    top = tk.Toplevel(root)
    top.grab_set()
    top.resizable(False, False)
    
    def obtener_valores(var1, var2, var3, var4, var5, var6):
        confirmacion = messagebox.askquestion("Confirmar", "¿Está seguro de borrar a este estudiante?")
        if confirmacion == 'yes':
            vare1 = var1.get()  # curso
            vare2 = var2.get()  # nombre
            vare3 = var3.get()  # apellido
            vare4 = var4.get()  # f.ingreso
            vare5 = var5.get()  # dni
            vare6 = var6.get()  # obs
            prueba = tree.selection()
            valor_dni = tree.item(prueba, "values")
            if vare5 in valor_dni[4]:
                valoress = [vare1, vare2, vare3, vare4, vare5, vare6] 
                conexion = crear_conexion()
                insertar = f"DELETE FROM estudiantes WHERE dni = {valoress[4]};"
                ejecutar_datos(conexion, insertar)
                conexion.close()
                top.destroy()
            else:
                messagebox.showerror("Error", "El dni no es el seleccionado anteriormente")
        else:
            return
    
    def extraer_numeros_de_fecha2(fecha):
        return ''.join(filter(str.isdigit, fecha))

    def valor_entry4(treeview, entry, posicion):
        try:
            seleccionado = treeview.selection()
            if not seleccionado:
                print("No hay selección")

            valores = treeview.item(seleccionado, 'values')
            if len(valores) <= posicion:
                print("error")

            valor = valores[posicion]
            valor_numeros = extraer_numeros_de_fecha2(valor)
            entry.delete(0, tk.END)
            entry.insert(0, valor_numeros)
        except:
            print("error")

    def validar_entrada(entrada):
        return entrada.isdigit()

    def actualizar_textvar(event, textarea, textvar):
        textvar.set(textarea.get("1.0", tk.END).strip())
    
    def valor_textarea(treeview, textarea, posicion):
        try:
            seleccionado = treeview.selection()
            if not seleccionado:
                print("No hay selección")

            valores = treeview.item(seleccionado, 'values')
            if len(valores) <= posicion:
                raise ValueError(f"La fila seleccionada no tiene al menos {posicion + 1} valores")

            valor_definitivo = valores[posicion]
            textarea.delete('1.0', tk.END)
            textarea.insert('0.0', valor_definitivo)
        except:
            print("error")
            top.destroy()

    def valor_entry(treeview, entry, posicion):
        try:
            seleccionado = treeview.selection()
            if not seleccionado:
                print("No hay selección")

            valores = treeview.item(seleccionado, 'values')
            if len(valores) <= posicion:
                raise ValueError(f"La fila seleccionada no tiene al menos {posicion + 1} valores")

            entry.delete(0, tk.END)
            valor_definitivo = valores[posicion]
            entry.insert(0, valor_definitivo)
        except:
            print("error")
    
    var_entry1 = tk.StringVar()
    var_entry2 = tk.StringVar()
    var_entry3 = tk.StringVar()
    var_entry4 = tk.StringVar()
    var_entry5 = tk.StringVar()
    var_entry6 = tk.StringVar()
    
    top.title("Eliminar estudiante")
    top.config(bg="#fff")
    top.geometry("460x610")
    
    frame_superior = tk.Frame(top, width=460, height=90, bg="#fff")
    frame_superior.pack(side="top")
    frame_superior.pack_propagate(False)
    
    titulo = tk.Label(frame_superior, text="Borrar Estudiante", font=("Times", 39, "italic bold"), bg="#fff", fg="#3C5BBA")
    titulo.place(relx=0.5, rely=0.45, anchor="center")
    
    frame_inferior = tk.Frame(top, width=460, height=490, bg="#fff")
    frame_inferior.pack(side="top")
    
    # Entry 1: Curso
    new_frame = crear_frame_auxiliar(frame_inferior, 60)
    img = imagen(0)
    label_img = tk.Label(new_frame, image=img, bg="#fff")
    label_img.image = img
    label_img.place(relx=0.015, rely=0.0)

    label1 = tk.Label(new_frame, text="Curso:", font=("Times", 14), fg="#666a88", bg="#fff")
    label1.place(relx=0.065, rely=0.0)
    entry1 = tk.Entry(new_frame, textvariable=var_entry1, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry1.place(relx=0.015, rely=0.5, relwidth=0.95)
    valor_entry(tree, entry1, 0)
    
    # Entry 2: Nombre/s
    new_frame2 = crear_frame_auxiliar(frame_inferior, 60)
    img = imagen(1)
    label_img = tk.Label(new_frame2, image=img, bg="#fff")
    label_img.image = img
    label_img.place(relx=0.015, rely=0.0)

    label2 = tk.Label(new_frame2, text="Nombre/s:", font=("Times", 14), fg="#666a88", bg="#fff")
    label2.place(relx=0.065, rely=0.0)
    entry2 = tk.Entry(new_frame2, textvariable=var_entry2, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry2.place(relx=0.015, rely=0.5, relwidth=0.95)
    valor_entry(tree, entry2, 1)
    
    # Entry 3: Apellido/s
    new_frame3 = crear_frame_auxiliar(frame_inferior, 60)
    img = imagen(2)
    label_img3 = tk.Label(new_frame3, image=img, bg="#fff")
    label_img3.image = img
    label_img3.place(relx=0.015, rely=0.0)

    label3 = tk.Label(new_frame3, text="Apellido/s:", font=("Times", 14), fg="#666a88", bg="#fff")
    label3.place(relx=0.065, rely=0.0)
    entry3 = tk.Entry(new_frame3, textvariable=var_entry3, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry3.place(relx=0.015, rely=0.5, relwidth=0.95)
    valor_entry(tree, entry3, 2)
    
    # Entry 4: Fecha de Ingreso con Calendario
    seleccionado = tree.selection()
    valores = tree.item(seleccionado, 'values')
    valorsito = valores[3]
    new_frame4 = crear_frame_auxiliar(frame_inferior, 60)
    
    def calendario(var_entry4):
        def obtener_fecha(calendari, var_entry4):
            fecha_seleccionada = calendari.get_date()
            fecha_sin_barras = fecha_seleccionada.replace('/', '')
            var_entry4.set(fecha_sin_barras)
            top2.destroy()
        
        fecha_inicial_remplazada = valorsito.replace('-', '/')
        fecha_inicial = datetime.strptime(fecha_inicial_remplazada, "%d/%m/%Y")
        top2 = tk.Toplevel(top)
        top2.geometry("260x245+550+200")
        top2.config(bg="#fff")
        top2.resizable(False, False)
        top2.grab_set()
        calendario = Calendar(top2, selectmode='day', date_pattern='dd/mm/yyyy', locale='es', background="#fff", foreground="#000", weekendbackground='#fff', othermonthbackground='#fff', daybackground="#fff", showweeknumbers=False, selectbackground="#eee", selectforeground="#000", bordercolor="#fff", headersbackground="#fff", othermonthwebackground="#fff", font=("cambria", 11, "italic"), year=fecha_inicial.year, month=fecha_inicial.month, day=fecha_inicial.day)
        calendario.pack(side="top")
        botonsito = tk.Button(top2, text="Definir Fecha", bg="#3C5BBA", fg="#fff", font=("Helvetica", 11, "bold"), command=lambda: obtener_fecha(calendario, var_entry4))
        botonsito.pack(side="top", pady=10)
    
    boton_calendario = tk.Button(new_frame4, text="Fecha de ingreso", width=25, bd=1, relief="solid", bg="#fff", fg="#666a88", font=("Times", 14), command=lambda: calendario(var_entry4))
    boton_calendario.place(relx=0.015, rely=0.0)
    entry4 = tk.Entry(new_frame4, textvariable=var_entry4, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry4.place(relx=0.015, rely=0.5, relwidth=0.95)
    valor_entry4(tree, entry4, 3)
    
    # Entry 5: Dni
    new_frame5 = crear_frame_auxiliar(frame_inferior, 60)
    img = imagen(3)
    label_img4 = tk.Label(new_frame5, image=img, bg="#fff")
    label_img4.image = img
    label_img4.place(relx=0.015, rely=0.0)

    label5 = tk.Label(new_frame5, text="Dni:", font=("Times", 14), fg="#666a88", bg="#fff")
    label5.place(relx=0.065, rely=0.0)
    entry5 = tk.Entry(new_frame5, textvariable=var_entry5, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(new_frame5.register(validar_entrada), '%P'))
    entry5.place(relx=0.015, rely=0.5, relwidth=0.95)
    valor_entry(tree, entry5, 4)
    
    # TextArea 6: Observaciones
    new_frame6 = crear_frame_auxiliar(frame_inferior, 120)
    img = imagen(4)
    label_img5 = tk.Label(new_frame6, image=img, bg="#fff")
    label_img5.image = img
    label_img5.place(relx=0.015, rely=0.0)

    label6 = tk.Label(new_frame6, text="Observaciones:", font=("Times", 14), fg="#666a88", bg="#fff")
    label6.place(relx=0.065, rely=0.0)
    textarea = tk.Text(new_frame6, wrap="word", font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, height=5)
    textarea.place(relx=0.015, rely=0.25, relwidth=0.95)
    valor_textarea(tree, textarea, 5)
    
    boton = tk.Button(top, text="Eliminar", bg="#3C5BBA", fg="#fff", font=("Helvetica", 11, "bold"), command=lambda: obtener_valores(var_entry1, var_entry2, var_entry3, var_entry4, var_entry5, var_entry6))
    boton.pack(side="top", pady=10)

    def on_text_change(event):
        actualizar_textvar(event, textarea, var_entry6)

    textarea.bind("<KeyRelease>", on_text_change)
    
    root.wait_window(top)
