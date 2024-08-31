import tkinter as tk
from ayudas import *
from bd import crear_conexion,ejecutar_datos
from tkinter import messagebox
from tkcalendar import *
from datetime import date,datetime
import json
from tkinter import ttk

def verificar_valor_en_lista(valor, lista):
    if valor in lista:
        print("Hola")
    else:
        print("Mal hecho")
        
def crear_modificar(root,tree,lista_permitidos,nombre_tabla,guardar_cursos):
    top=tk.Toplevel(root)
    top.grab_set()
    top.resizable(False,False)
    fecha_actual=date.today()
    def verificacion(ventana,treeview):
        seleccionado1=treeview.selection()
        if not seleccionado1:
            ventana.destroy()

    
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
    
    
    def obtener_valores(var1,var2,var3,var4,var5,var6):
        curso=combo.get()
        vare1=var1.get()
        vare1=curso
        vare2=var2.get()
        vare3=var3.get()
        vare4=var4.get()
        vare5=var5.get()
        vare6=var6.get()
        
        if vare6=="":
            seleccionado = tree.selection()
            valores = tree.item(seleccionado, 'values')
            valor_definitivo=valores[5]
            vare6=valor_definitivo
            
         #si no esta bien echo
        if not vare1:
            label1.config(fg="#f00",text="Curso:*",font=("Times",14,"underline"))            
        if not vare2:
            label2.config(fg="#f00",text="Nombre/s:*",font=("Times",14,"underline"))
        if not vare3:
            label3.config(fg="#f00",text="Apellido/s:*",font=("Times",14,"underline"))
        if not vare5:
            label5.config(fg="#f00",text="DNI:*",font=("Times",14,"underline"))
        if not vare6:
            label6.config(fg="#f00",text="Observaciones:*",font=("Times",14,"underline"))
        
        #si esta bien echo
        if vare1:
            label1.config(fg="#666a88",text="Curso:",font=("Times",14))            
        if vare2:
            label2.config(fg="#666a88",text="Nombre/s:",font=("Times",14))
        if vare3:
            label3.config(fg="#666a88",text="Apellido/s:",font=("Times",14))
        if vare5:
            label5.config(fg="#666a88",text="DNI:",font=("Times",14))
        if vare6:
            label6.config(fg="#666a88",text="Observaciones:",font=("Times",14))

        #si alguno de todos esta mal no permite ingresar la consulta
        if not vare6 or not vare5 or not vare3 or not vare2 or not vare1:
            return
        if not vare4:
            seleccionado = tree.selection()
            valores = tree.item(seleccionado, 'values')
            valor_definitivo = valores[3]
            valor_definitivo2=valor_definitivo.replace("-","")
            vare4=valor_definitivo2
        valor_1=vare1.capitalize()
        valor_2=vare2.title()
        valor_3=vare3.title()
        conexion=crear_conexion()
        valoress=[valor_1,valor_2,valor_3,vare4,vare5,vare6]
        insertar=f"UPDATE {nombre_tabla} SET curso='{valoress[0]}',nombres='{valoress[1]}', apellidos='{valoress[2]}',fecha_ingreso='{vare4}',dni={valoress[4]},observaciones='{valoress[5]}' where dni={valoress[4]};"
        ejecutar_datos(conexion,insertar)
        conexion.close() 
        top.destroy()
    


    
    def validar_entrada(entrada):
    # Permitir solo dígitos
        return entrada.isdigit()
    
    def solo_letras(char):
    # Retorna True si el carácter es una letra, False de lo contrario
        return char.isalpha() or char.isspace()
    
    
    def actualizar_textvar(event, textarea, textvar):#el event tiene que estar si o si aunque te marque que no se esta usando
        textvar.set(textarea.get("0.0", tk.END).strip())
    
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
            textarea.delete('0.0', tk.END)  # Limpiar el contenido del Text
            textarea.insert('0.0', valor_definitivo)  # Insertar el valor en el Text
        # except ValueError as ve:
        #     messagebox.showerror("Error", str(ve))
        # except Exception as e:
        #     messagebox.showerror("Error", f"Error inesperado: {str(e)}")
        except:
            print("Error")
            top.destroy()
    def valor_entry(treeview, entry, posicion):
        try:
            seleccionado = treeview.selection()
            if not seleccionado:
                # raise ValueError("No hay selección")
                print("No hay selección")

            valores = treeview.item(seleccionado, 'values')
            print(treeview.item(seleccionado,'values'))
            if len(valores) <= posicion:
                raise ValueError(f"La fila seleccionada no tiene al menos {posicion + 1} valores")

            # Convertir el valor de la posición especificada a entero
            # valor_entero = int(valores[posicion])
            entry.config(validate="none")
            valor_definitivo=valores[posicion]
            entry.delete(0, tk.END)  # Limpiar el contenido del Entry
            entry.insert(0, valor_definitivo)  # Insertar el valor entero en el Entry
            entry.config(validate='key')
        # except ValueError as ve:
        #     messagebox.showerror("Error", str(ve))
        # except Exception as e:
        #     messagebox.showerror("Error", f"Error inesperado: {str(e)}")
        except:
            print("Error")
    
    var_entry1=tk.StringVar()
    var_entry2=tk.StringVar()
    var_entry3=tk.StringVar()
    var_entry4=tk.StringVar()
    var_entry5=tk.StringVar()
    var_entry6=tk.StringVar()
    
    
    
    top.title("Modicar estudiante")
    top.config(bg="#fff")
    top.geometry("460x610")
    
    frame_superior=tk.Frame(top,width=460,height=90,bg="#fff")###medidas exactas
    frame_superior.pack(side="top")
    frame_superior.pack_propagate(False)
    
    titulo=tk.Label(frame_superior,text="Modificar Estudiante",font=("Times",39,"italic bold"),bg="#fff",fg="#3C5BBA")
    titulo.place(relx=0.5,rely=0.45,anchor="center")
    
    frame_inferior=tk.Frame(top,width=460,height=490,bg="#fff",)###medidas exactas
    frame_inferior.pack(side="top")
    
    
    
    #entry1-------------------------------------------------
    new_frame=crear_frame_auxiliar(frame_inferior,60)#alto del frame
    #el nuevo frame_aux
    img = imagen(0)#num_img
    label_img=tk.Label(new_frame,image=img,bg="#fff")
    label_img.image=img#esta linea es inprescindible pq sino pierde la referencia y no anda la imagen
    label_img.place(relx=0.015,rely=0.0)#ubicacionx,ubicaciony

    label1=tk.Label(new_frame,text="Curso:",font=("Times",14),fg="#666a88",bg="#fff")#texto
    label1.place(relx=0.065,rely=0.0)#ubi1,ubi2

    def ventana_entry(opciones):
        def guardar_opciones(opciones):
            with open(f'{guardar_cursos}.json', 'w') as file:
                json.dump(opciones, file)
        def obtener_curso():
            nueva_opcion=var_entry1.get()
            opciones=cargar_opciones()
            if nueva_opcion and nueva_opcion not in opciones:
                opciones.append(nueva_opcion)
                combo['values']=opciones
                guardar_opciones(opciones=opciones)
                entry1.delete(0,tk.END)
                top3.destroy()
                
        def cargar_opciones():
            try:
                with open(f'{guardar_cursos}.json', 'r') as file:
                    return json.load(file)
            except FileNotFoundError:
                return []
            
        top3=tk.Toplevel(top)
        top3.geometry("260x150")
        top3.title("Agregar Curso")
        top3.config(bg="#fff")
        tt=tk.Label(top3,text="Agregar un curso",font=("Times",21,"italic bold"),bg="#fff",fg="#3C5BBA")
        tt.place(relx=0.5,rely=0.2,anchor="center")
        entry1 = tk.Entry(top3, textvariable=var_entry1, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
        entry1.place(relx=0.019, rely=0.5, relwidth=0.95)
        btnn=tk.Button(top3,text="Ingresar curso",bg="#3C5BBA",fg="#fff",font=("Helvetica",10,"bold"),pady=1,bd=2,relief="flat",activebackground="#fff",activeforeground="#3C5BBA", overrelief="solid",width=30,command=lambda:obtener_curso())
        btnn.place(relx=0.5,rely=0.86,anchor="center")
        
        top3.mainloop()
    opcion=[]
    try:
            with open(f'{guardar_cursos}.json', 'r') as file:
                opcion=json.load(file)
    except FileNotFoundError:
         return opcion
     
    def guardar_opciones2():
        with open(f'{guardar_cursos}.json', 'w') as file:
            json.dump(opcion, file)
    def eliminar_opcion():
        seleccion = combo.get()  # Obtener la opción seleccionada
        confirmacion = messagebox.askyesno("Confirmación", f"¿Estás seguro de que deseas eliminar '{seleccion}'?")
        if confirmacion:
            if seleccion in opcion:
                opcion.remove(seleccion)  # Eliminarla de la lista de opciones
                combo['values'] = opcion  # Actualizar el Combobox
                guardar_opciones2()  # Guardar la lista actualizada en el archivo .json
                combo.set('')  # Limpiar la selección del Combobox
            else:
                return
            combo.set('Ingrese un curso')
        
    btn=tk.Button(new_frame,text="Agregar Curso",bd=1,relief="solid",bg="#fff",fg="#666a88",font=("Cambria",10,"bold"),padx=4,pady=1,command=lambda: ventana_entry(opcion))
    btn.place(relx=0.52,rely=0.6,anchor="center")
    btn2=tk.Button(new_frame,text="Eliminar Curso",bd=1,relief="solid",bg="#fff",fg="#666a88",font=("Cambria",10,"bold"),padx=4,pady=1,command=lambda: eliminar_opcion())
    btn2.place(relx=0.79,rely=0.6,anchor="center")
    
    style=ttk.Style()
    style.configure("TCombobox", font=("Times", 12))
    
    combo = ttk.Combobox(new_frame, values=opcion, state="readonly",style="TCombobox")
    seleccionado = tree.selection()
    valores = tree.item(seleccionado, 'values')
    if valores and len(valores) > 0:  # Verificar que 'valores' no esté vacío
        valor_definitivo = valores[0]  # Asignar el primer valor de 'valores'
        valor_definitivo=valores[0]
        combo.set(f"{valor_definitivo}")
        combo.place(rely=0.6,relx=0.2,anchor="center")
    else:
        return top.destroy()
    #entry2------------------------------------------------
    new_frame2=crear_frame_auxiliar(frame_inferior,60)
    validacion = new_frame2.register(solo_letras)
    img = imagen(1)
    label_img=tk.Label(new_frame2,image=img,bg="#fff")
    label_img.image=img
    label_img.place(relx=0.015,rely=0.0)

    label2=tk.Label(new_frame2,text="Nombre/s:",font=("Times",14),fg="#666a88",bg="#fff")
    label2.place(relx=0.065,rely=0.0)
    entry2 = tk.Entry(new_frame2, textvariable=var_entry2, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID,validate="key",validatecommand=(validacion,'%S'))
    entry2.place(relx=0.015, rely=0.5, relwidth=0.95)
    valor_entry(tree,entry2,1)
    entry2.bind('<KeyRelease>',lambda event:capitalizar_palabras(event,entry2))


    #entry3------------------------------------------------
    new_frame3=crear_frame_auxiliar(frame_inferior,60)
    validacion2 = new_frame3.register(solo_letras)
    img = imagen(2)
    label_img3=tk.Label(new_frame3,image=img,bg="#fff")
    label_img3.image=img
    label_img3.place(relx=0.015,rely=0.0)

    label3=tk.Label(new_frame3,text="Apellido/s:",font=("Times",14),fg="#666a88",bg="#fff")
    label3.place(relx=0.065,rely=0.0)
    entry3 = tk.Entry(new_frame3, textvariable=var_entry3, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID,validate="key",validatecommand=(validacion2,'%S'))
    entry3.place(relx=0.015, rely=0.5, relwidth=0.95)
    valor_entry(tree,entry3,2)
    entry3.bind('<KeyRelease>',lambda event:capitalizar_palabras(event,entry3))


    #entry4----------------------------------------------
    seleccionado=tree.selection()
    valores=tree.item(seleccionado,'values')
    valorsito=valores[3]
    new_frame4=crear_frame_auxiliar(frame_inferior,60)
    boton_calendario=tk.Button(new_frame4,text="Fecha de ingreso",width=25,bd=1,relief="solid",bg="#fff",fg="#666a88",font=("Cambria",16,"bold"),command=lambda:calendario(var_entry4))
    boton_calendario.place(rely=0.55,relx=0.5,anchor="center")
    def calendario(var_entry4):
        def obtener_fecha(calendari,var_entry4):
            fecha_seleccionada=calendari.get_date()
            boton_calendario.config(text=f"{fecha_seleccionada}")
            fecha_sin_barras = fecha_seleccionada.replace('/', '')
            var_entry4.set(fecha_sin_barras)
            top2.destroy()
            top.grab_set()
        fecha_inicial_remplazada=valorsito.replace('-','/')
        fecha_inicial=datetime.strptime(fecha_inicial_remplazada,"%d/%m/%Y")
        top2=tk.Toplevel(top)
        top2.geometry("260x245+550+200")#260x185 tamaño del calendario 
        top2.config(bg="#fff")
        top2.resizable(False,False)
        top2.grab_set()
        calendario = Calendar(top2, selectmode='day', date_pattern='dd/mm/yyyy', locale='es',background="#fff",foreground="#000",weekendbackground='#fff',othermonthbackground='#fff',daybackground="#fff",showweeknumbers=False,selectbackground="#eee",selectforeground="#000",bordercolor="#fff",headersbackground="#fff",othermonthwebackground="#fff",font=("cambria",11,"italic"),year=fecha_inicial.year,month=fecha_inicial.month,day=fecha_inicial.day,maxdate=fecha_actual)
        calendario.pack(side="top")
        botonsito=tk.Button(top2,text="Definir fecha",bg="#3C5BBA",fg="#fff",font=("Helvetica",11,"bold"),pady=0,bd=2,relief="flat",activebackground="#fff",activeforeground="#3C5BBA", overrelief="solid",width=26,command=lambda:obtener_fecha(calendario,var_entry4))
        botonsito.place(rely=0.88,relx=0.5,anchor="center")
    
    valor_boton=valorsito
    valor_btn=valor_boton.replace("-","/")
    boton_calendario.config(text=f"{valor_btn}")

    


    #entry5------------------------------------------------
    new_frame5=crear_frame_auxiliar(frame_inferior,60)
    validar_cmd = new_frame5.register(validar_entrada)
    img = imagen(4)
    label_img=tk.Label(new_frame5,image=img,bg="#fff")
    label_img.image=img
    label_img.place(relx=0.015,rely=0.0)

    label5=tk.Label(new_frame5,text="DNI:",font=("Times",14),fg="#666a88",bg="#fff")
    label5.place(relx=0.065,rely=0.0)
    entry5 = tk.Entry(new_frame5, textvariable=var_entry5, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID,validate="key", validatecommand=(validar_cmd, '%P'))
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
    
    boton_ingresar=tk.Button(top,text="Modificar Estudiante",bg="#3C5BBA",fg="#fff",font=("Helvetica",18,"bold"),pady=2,bd=2,relief="flat",activebackground="#fff",activeforeground="#3C5BBA", overrelief="solid",command=lambda:obtener_valores(var_entry1,var_entry2,var_entry3,var_entry4,var_entry5,var_entry6))
    boton_ingresar.place(relx=0.5,rely=0.95,anchor="center",relwidth=0.97)
    
    valor_textarea(tree,textarea,5)
    top.mainloop()