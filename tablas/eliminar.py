import tkinter as tk
from ayudas import *
from bd import crear_conexion,ejecutar_datos
from tkinter import messagebox


def crear_eliminar(root,tree):
    top=tk.Toplevel(root)
    top.grab_set()
    top.resizable(False,False)
    
    def obtener_valores(var1,var2,var3,var4,var5,var6):
        vare1=var1.get()
        vare2=var2.get()
        vare3=var3.get()
        vare4=var4.get()
        vare5=var5.get()
        vare6=var6.get()
        valoress=[vare1,vare2,vare3,vare4,vare5,vare6] 
        conexion=crear_conexion()
        insertar=f"DELETE FROM estudiantes WHERE dni = {valoress[4]};"
        ejecutar_datos(conexion,insertar)
        conexion.close()
        top.destroy()
    
    def extraer_numeros_de_fecha(fecha):
        numeros = [int(c) for c in fecha if c.isdigit()]
        return numeros

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
                

            # Extraer números del valor de la posición especificada
            valor = valores[posicion]
            valor_numeros = extraer_numeros_de_fecha2(valor)
            entry.delete(0, tk.END)  # Limpiar el contenido del Entry
            entry.insert(0, valor_numeros)  # Insertar los números en el Entry
        # except ValueError as ve:
        #     messagebox.showerror("Error", str(ve))
        # except Exception as e:
        #     messagebox.showerror("Error", f"Error inesperado: {str(e)}")
        except:
            print("error")
    def validar_entrada(entrada):
    # Permitir solo dígitos
        return entrada.isdigit()
    
    def actualizar_textvar(event, textarea, textvar):#el event tiene que estar si o si aunque te marque que no se esta usando
        textvar.set(textarea.get("1.0", tk.END).strip())
    
    def valor_textarea(treeview, textarea, posicion):
        try:
            seleccionado = treeview.selection()
            if not seleccionado:
                print("No hay selección")

            valores = treeview.item(seleccionado, 'values')
            if len(valores) <= posicion:
                raise ValueError(f"La fila seleccionada no tiene al menos {posicion + 1} valores")

            # Obtener el valor de la posición especificada
            valor_definitivo = valores[posicion]
            textarea.delete('1.0', tk.END)  # Limpiar el contenido del Text
            textarea.insert('0.0', valor_definitivo)  # Insertar el valor en el Text
        # except ValueError as ve:
        #     messagebox.showerror("Error", str(ve))
        # except Exception as e:
        #     messagebox.showerror("Error", f"Error inesperado: {str(e)}")
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

            # Convertir el valor de la posición especificada a entero
            # valor_entero = int(valores[posicion])
            entry.delete(0, tk.END)  # Limpiar el contenido del Entry
            valor_definitivo=valores[posicion]
            entry.insert(0, valor_definitivo)  # Insertar el valor entero en el Entry
        # except ValueError as ve:
        #     messagebox.showerror("Error", str(ve))
        # except Exception as e:
        #     messagebox.showerror("Error", f"Error inesperado: {str(e)}")
        except:
            print("error")
    var_entry1=tk.StringVar()
    var_entry2=tk.StringVar()
    var_entry3=tk.StringVar()
    var_entry4=tk.StringVar()
    var_entry5=tk.StringVar()
    var_entry6=tk.StringVar()
    
    
    
    top.title("Agregar un estudiante")
    top.config(bg="#fff")
    top.geometry("460x610")
    
    frame_superior=tk.Frame(top,width=460,height=90,bg="#fff")###medidas exactas
    frame_superior.pack(side="top")
    frame_superior.pack_propagate(False)
    
    titulo=tk.Label(frame_superior,text="Borrar Estudiante",font=("Times",39,"italic bold"),bg="#fff",fg="#3C5BBA")
    titulo.place(relx=0.5,rely=0.45,anchor="center")
    
    frame_inferior=tk.Frame(top,width=460,height=490,bg="#fff",)###medidas exactas
    frame_inferior.pack(side="top")
    
    
    #entry1-------------------------------------------------
    new_frame=crear_frame_auxiliar(frame_inferior,60)
    img = imagen(0)
    label_img=tk.Label(new_frame,image=img,bg="#fff")
    label_img.image=img
    label_img.place(relx=0.015,rely=0.0)

    label1=tk.Label(new_frame,text="Curso:",font=("Times",14),fg="#666a88",bg="#fff")
    label1.place(relx=0.065,rely=0.0)
    entry1 = tk.Entry(new_frame, textvariable=var_entry1, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID,)
    entry1.place(relx=0.015, rely=0.5, relwidth=0.95)
    valor_entry(tree,entry1,0)
    
    
    #entry2------------------------------------------------
    new_frame2=crear_frame_auxiliar(frame_inferior,60)
    img = imagen(1)
    label_img=tk.Label(new_frame2,image=img,bg="#fff")
    label_img.image=img
    label_img.place(relx=0.015,rely=0.0)

    label2=tk.Label(new_frame2,text="Nombre/s:",font=("Times",14),fg="#666a88",bg="#fff")
    label2.place(relx=0.065,rely=0.0)
    entry2 = tk.Entry(new_frame2, textvariable=var_entry2, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry2.place(relx=0.015, rely=0.5, relwidth=0.95)
    valor_entry(tree,entry2,1)


    #entry3------------------------------------------------
    new_frame3=crear_frame_auxiliar(frame_inferior,60)
    img = imagen(2)
    label_img3=tk.Label(new_frame3,image=img,bg="#fff")
    label_img3.image=img
    label_img3.place(relx=0.015,rely=0.0)

    label3=tk.Label(new_frame3,text="Apellido/s:",font=("Times",14),fg="#666a88",bg="#fff")
    label3.place(relx=0.065,rely=0.0)
    entry3 = tk.Entry(new_frame3, textvariable=var_entry3, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
    entry3.place(relx=0.015, rely=0.5, relwidth=0.95)
    valor_entry(tree,entry3,2)


    #entry4------------------------------------------------
    new_frame4=crear_frame_auxiliar(frame_inferior,60)
    img = imagen(3)
    label_img=tk.Label(new_frame4,image=img,bg="#fff")
    label_img.image=img
    label_img.place(relx=0.015,rely=0.0)

    validar_cmd = new_frame4.register(validar_entrada)
    label4=tk.Label(new_frame4,text="F.Ingreso:",font=("Times",14),fg="#666a88",bg="#fff")
    label4.place(relx=0.065,rely=0.0)
    entry4 = tk.Entry(new_frame4, textvariable=var_entry4, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID,validate="key", validatecommand=(validar_cmd, '%P'))
    entry4.place(relx=0.015, rely=0.5, relwidth=0.95)
    valor_entry4(tree,entry4,3)


    #entry5------------------------------------------------
    new_frame5=crear_frame_auxiliar(frame_inferior,60)
    img = imagen(4)
    label_img=tk.Label(new_frame5,image=img,bg="#fff")
    label_img.image=img
    label_img.place(relx=0.015,rely=0.0)

    label5=tk.Label(new_frame5,text="DNI:",font=("Times",14),fg="#666a88",bg="#fff")
    label5.place(relx=0.065,rely=0.0)
    entry5 = tk.Entry(new_frame5, textvariable=var_entry5, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID,)
    entry5.place(relx=0.015, rely=0.5, relwidth=0.95)
    valor_entry(tree,entry5,4)

    #entry6------------------------------------------------
    new_frame6=crear_frame_auxiliar(frame_inferior,150)
    img = imagen(5)
    label_img=tk.Label(new_frame6,image=img,bg="#fff")
    label_img.image=img
    label_img.place(relx=0.015,rely=0.0)
    
    label6=tk.Label(new_frame6,text="Observaciones:",font=("Times",14),fg="#666a88",bg="#fff")
    label6.place(relx=0.065,rely=0.0)#ubi1,ubi2
    textarea = tk.Text(new_frame6, font=("Times", 14), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, height=5)
    textarea.place(relx=0.015, rely=0.18, relwidth=0.95)
    
    textarea.bind("<KeyRelease>", lambda event: actualizar_textvar(event, textarea, var_entry6))
    
    boton_ingresar=tk.Button(top,text="Borrar Estudiante",bg="#3C5BBA",fg="#fff",font=("Helvetica",18,"bold"),pady=2,bd=2,relief="flat",activebackground="#fff",activeforeground="#3C5BBA", overrelief="solid",command=lambda:obtener_valores(var_entry1,var_entry2,var_entry3,var_entry4,var_entry5,var_entry6))
    boton_ingresar.place(relx=0.5,rely=0.95,anchor="center",relwidth=0.97)
    
    valor_textarea(tree,textarea,5)
    top.mainloop()