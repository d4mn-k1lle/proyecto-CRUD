import tkinter as tk
from ayudas import *
from bd import crear_conexion,ejecutar_datos
from tkinter import messagebox


def crear_modificar(root,tree):
    
    def mostrar_valor_entero_en_entry(treeview, entry):
        try:
            seleccionado = treeview.selection()
            if not seleccionado:
                raise ValueError("No hay selección")

            valores = treeview.item(seleccionado, 'values')
            if len(valores) < 5:
                raise ValueError("La fila seleccionada no tiene al menos cinco valores")

            # Convertir el quinto valor a entero
            valor_entero = int(valores[4])
            entry.delete(0, tk.END)  # Limpiar el contenido del Entry
            entry.insert(0, valor_entero)  # Insertar el valor entero en el Entry
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    var_entry1=tk.StringVar()
    var_entry2=tk.StringVar()
    var_entry3=tk.StringVar()
    var_entry4=tk.StringVar()
    var_entry5=tk.StringVar()
    var_entry6=tk.StringVar()
    
    
    
    top=tk.Toplevel(root)
    top.title("Agregar un estudiante")
    top.config(bg="#fff")
    top.geometry("460x610")
    
    frame_superior=tk.Frame(top,width=460,height=90,bg="#fff")###medidas exactas
    frame_superior.pack(side="top")
    frame_superior.pack_propagate(False)
    
    titulo=tk.Label(frame_superior,text="Ingresar Estudiante",font=("Times",39,"italic bold"),bg="#fff",fg="#3C5BBA")
    titulo.place(relx=0.5,rely=0.45,anchor="center")
    
    frame_inferior=tk.Frame(top,width=460,height=490,bg="#fff",)###medidas exactas
    frame_inferior.pack(side="top")
    
    validate_cmd = top.register(solo_numeros)
    
    new_frame=crear_frame_auxiliar(frame_inferior,60)#alto del frame
    #el nuevo frame_aux
    img = imagen(0)#num_img
    label_img=tk.Label(new_frame,image=img,bg="#fff")
    label_img.image=img#esta linea es inprescindible pq sino pierde la referencia y no anda la imagen
    label_img.place(relx=0.015,rely=0.0)#ubicacionx,ubicaciony

    label1=tk.Label(new_frame,text="Curso:",font=("Times",14),fg="#666a88",bg="#fff")#texto
    label1.place(relx=0.065,rely=0.0)#ubi1,ubi2
    es_numero=False
    if es_numero:#si only numbers es true(es una parametro asi que se puede elegir) hace que solo se pueda usar numeros, lo hace con el validate_cmd(que esta en agregar)
        entry1 = tk.Entry(new_frame, textvariable=var_entry1, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
    else:
        entry1 = tk.Entry(new_frame, textvariable=var_entry1, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry1.place(relx=0.015, rely=0.5, relwidth=0.95)
    mostrar_valor_entero_en_entry(tree,entry1)
    
    new_frame2=crear_frame_auxiliar(frame_inferior,60)#alto del frame
    #el nuevo frame_aux
    img = imagen(1)#num_img
    label_img=tk.Label(new_frame2,image=img,bg="#fff")
    label_img.image=img#esta linea es inprescindible pq sino pierde la referencia y no anda la imagen
    label_img.place(relx=0.015,rely=0.0)#ubicacionx,ubicaciony

    label2=tk.Label(new_frame2,text="Curso:",font=("Times",14),fg="#666a88",bg="#fff")#texto
    label2.place(relx=0.065,rely=0.0)#ubi1,ubi2
    es_numero=False
    if es_numero:#si only numbers es true(es una parametro asi que se puede elegir) hace que solo se pueda usar numeros, lo hace con el validate_cmd(que esta en agregar)
        entry2 = tk.Entry(new_frame2, textvariable=var_entry2, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
    else:
        entry2 = tk.Entry(new_frame2, textvariable=var_entry2, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry2.place(relx=0.015, rely=0.5, relwidth=0.95)


    new_frame3=crear_frame_auxiliar(frame_inferior,60)#alto del frame
    #el nuevo frame_aux
    img = imagen(2)#num_img
    label_img3=tk.Label(new_frame3,image=img,bg="#fff")
    label_img3.image=img#esta linea es inprescindible pq sino pierde la referencia y no anda la imagen
    label_img3.place(relx=0.015,rely=0.0)#ubicacionx,ubicaciony

    label3=tk.Label(new_frame3,text="Curso:",font=("Times",14),fg="#666a88",bg="#fff")#texto
    label3.place(relx=0.065,rely=0.0)#ubi1,ubi2
    es_numero=False
    if es_numero:#si only numbers es true(es una parametro asi que se puede elegir) hace que solo se pueda usar numeros, lo hace con el validate_cmd(que esta en agregar)
        entry3 = tk.Entry(new_frame3, textvariable=var_entry3, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
    else:
        entry3 = tk.Entry(new_frame3, textvariable=var_entry3, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry3.place(relx=0.015, rely=0.5, relwidth=0.95)


    new_frame4=crear_frame_auxiliar(frame_inferior,60)#alto del frame
    #el nuevo frame_aux
    img = imagen(3)#num_img
    label_img=tk.Label(new_frame4,image=img,bg="#fff")
    label_img.image=img#esta linea es inprescindible pq sino pierde la referencia y no anda la imagen
    label_img.place(relx=0.015,rely=0.0)#ubicacionx,ubicaciony

    label4=tk.Label(new_frame4,text="Curso:",font=("Times",14),fg="#666a88",bg="#fff")#texto
    label4.place(relx=0.065,rely=0.0)#ubi1,ubi2
    es_numero=False
    if es_numero:#si only numbers es true(es una parametro asi que se puede elegir) hace que solo se pueda usar numeros, lo hace con el validate_cmd(que esta en agregar)
        entry4 = tk.Entry(new_frame4, textvariable=var_entry4, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
    else:
        entry4 = tk.Entry(new_frame4, textvariable=var_entry4, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry4.place(relx=0.015, rely=0.5, relwidth=0.95)


    new_frame5=crear_frame_auxiliar(frame_inferior,60)#alto del frame
    #el nuevo frame_aux
    img = imagen(4)#num_img
    label_img=tk.Label(new_frame5,image=img,bg="#fff")
    label_img.image=img#esta linea es inprescindible pq sino pierde la referencia y no anda la imagen
    label_img.place(relx=0.015,rely=0.0)#ubicacionx,ubicaciony

    label5=tk.Label(new_frame5,text="Curso:",font=("Times",14),fg="#666a88",bg="#fff")#texto
    label5.place(relx=0.065,rely=0.0)#ubi1,ubi2
    es_numero=False
    if es_numero:#si only numbers es true(es una parametro asi que se puede elegir) hace que solo se pueda usar numeros, lo hace con el validate_cmd(que esta en agregar)
        entry5 = tk.Entry(new_frame5, textvariable=var_entry5, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
    else:
        entry5 = tk.Entry(new_frame5, textvariable=var_entry5, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry5.place(relx=0.015, rely=0.5, relwidth=0.95)


    new_frame6=crear_frame_auxiliar(frame_inferior,60)#alto del frame
    #el nuevo frame_aux
    img = imagen(5)#num_img
    label_img=tk.Label(new_frame6,image=img,bg="#fff")
    label_img.image=img#esta linea es inprescindible pq sino pierde la referencia y no anda la imagen
    label_img.place(relx=0.015,rely=0.0)#ubicacionx,ubicaciony

    label6=tk.Label(new_frame6,text="Curso:",font=("Times",14),fg="#666a88",bg="#fff")#texto
    label6.place(relx=0.065,rely=0.0)#ubi1,ubi2
    es_numero=False
    if es_numero:#si only numbers es true(es una parametro asi que se puede elegir) hace que solo se pueda usar numeros, lo hace con el validate_cmd(que esta en agregar)
        entry6 = tk.Entry(new_frame6, textvariable=var_entry6, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
    else:
        entry6 = tk.Entry(new_frame6, textvariable=var_entry6, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry6.place(relx=0.015, rely=0.5, relwidth=0.95)
    
    
    boton_ingresar=tk.Button(top,text="Ingresar Estudiante",bg="#3C5BBA",fg="#fff",font=("Helvetica",18,"bold"),pady=2,bd=2,relief="flat",activebackground="#fff",activeforeground="#3C5BBA", overrelief="solid")
    boton_ingresar.place(relx=0.5,rely=0.93,anchor="center",relwidth=0.97)
    
    top.mainloop()