import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk


ventana=tk.Tk()
ventana.title("Ventana Principal")
ventana.geometry("960x560")

def show_frame(frame):
    frame.tkraise()
    
def DosEnUno(label,texto):
    label.config(text=texto)

def crear_boton_izq(frame,texto,relx,rely,estado,pady):
    boton=tk.Button(frame,text=texto,font=("Times",14,"bold"),width=10,height=1,bg="#fff",fg="#111",borderwidth=2,relief="flat",activebackground="#fff",activeforeground="#111", overrelief="solid",state=estado,disabledforeground="#111",pady=pady)
    boton.place(relx=relx,rely=rely)#0.12,0.05


#-- para los botones superiores, asi ahorro mucho codigo y es mas facil entenderlo --#
def crear_boton_curso(frame, nombre, relx, rely,comando):
    boton = tk.Button(frame, text=nombre, width=10, height=1, bg="#4575F4", fg="#000", font=("Cambria", 10, "bold"), bd=2,relief="flat",activebackground="#4575F4",activeforeground="#111", overrelief="solid", pady=5,command=comando)#3C5BBA
    boton.place(relx=relx, rely=rely, anchor="center")
    return boton

#########

def crear_boton_cambio(frame,nombre,relx,rely,frame_elegido):
    boton=tk.Button(frame,text=nombre,width=10, height=1,pady=5, bg="#4575F4", fg="#000", font=("Cambria", 10, "bold"), bd=2,relief="flat",activebackground="#4575F4",activeforeground="#111", overrelief="solid",command=lambda:show_frame(frame_elegido))
    boton.place(relx=relx,rely=rely,anchor="center")#0.92,0.5

#-- creamos el frame izquierdo donde van a ir los botones para desplazarte entre distintas tablas y donde va estar el logo (por el momento al menos) --#
frame_izq=tk.Frame(ventana,width=165,height=560,bg="#3C5BBA")
frame_izq.pack(side="left")
frame_izq.pack_propagate(False)


##########


#-- creamos un frame para el logo dentro del frame del titulo y hacemos que no se puedaachicar ni agrandar --#
frame_logo=tk.Frame(frame_izq,width=165,height=125,bg="#3C5BBA")#,bd=1,relief=tk.SOLID
frame_logo.pack(side=tk.TOP)
frame_logo.pack_propagate(False)

#-- le damos la ruta de la imagen y lo metemos en image --# 
image_path = "login_intento-legible.8/imagenes/logo_escuela.png" 
image = Image.open(image_path)

#-- le damos el tamaño y la achicamos con calidad con lanczos --#
new_size = (93,100)  #
resized_image = image.resize(new_size, Image.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)

#--la metemos en un label para que se vea y ubicamos el label en el centro del frame del logo--#
image_label = tk.Label(frame_logo, image=photo,bg="#3C5BBA")
image_label.place(relx=0.5, rely=0.5, anchor='center')


#########

#--frame para los botones de la izquierda--#
frame_botones_izq=tk.Frame(frame_izq,width=165,height=435,bg="#3C5BBA")
frame_botones_izq.pack(side="bottom")


#########

#-- creamos el boton de ciclo basico --#
boton_Basico=crear_boton_izq(frame_botones_izq,"Basico",0.12,0.05,"active",1)

#-- creamos el boton de Ciclo Superior  --#
boton_Superior=crear_boton_izq(frame_botones_izq,"Superior:",0.12,0.20,"disabled",4)

#-- creamos el boton de MMO --#
boton_Mmo=crear_boton_izq(frame_botones_izq,"MMO",0.12,0.304,"active",4)

#-- creamos el boton de informatica --#
boton_Informatica=crear_boton_izq(frame_botones_izq,"Informatica",0.12,0.408,"active",4)

#-- creamos el boton de Programacion --#
boton_Programacion=crear_boton_izq(frame_botones_izq,"Programacion",0.12,0.511,"active",4)

#-- creamos el boton de Egresados --#
boton_Egresados=crear_boton_izq(frame_botones_izq,"Egresados",0.12,0.66,"active",1)

#-- creamos el boton de Exalumnos --#
boton_Exalumnos=crear_boton_izq(frame_botones_izq,"Exalumnos",0.12,0.8,"active",1)


#########################################


frame_cursos=tk.Frame(ventana,width=795,height=130,bg="#ccc")
frame_cursos.pack(side="top")
frame_cursos.pack_propagate(False)

frame_titulo_tabla=tk.Frame(frame_cursos,bg="#fff",width=795,height=80,)
frame_titulo_tabla.pack(side="bottom")

titulo_tabla=tk.Label(frame_titulo_tabla,text="Ciclo Basico 1ºA",bg="#fff",fg="#111",font=("Cambria",40,"bold"))
titulo_tabla.place(relx=0.5,rely=0.45,anchor=("center"))


##########################################


frame_botones_sup2=tk.Frame(frame_cursos,width=795,height=50,bg="#fff")
##############
frame_botones_sup3=tk.Frame(frame_cursos,width=795,height=50,bg="#fff")
##############
frame_botones_sup=tk.Frame(frame_cursos,width=795,height=50,bg="#fff")
############## 
# Añadir los frames a la ventana principal, uno sobre el otro
for frame in (frame_botones_sup,frame_botones_sup2,frame_botones_sup3):
    frame.place(x=0, y=0, width=795, height=50)

boton_1a=crear_boton_curso(frame_botones_sup,"1ºA",0.08,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 1ºA"))
boton_1b=crear_boton_curso(frame_botones_sup,"1ºB",0.22,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 1ºB"))
boton_1c=crear_boton_curso(frame_botones_sup,"1ºC",0.36,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 1ºC"))
boton_1d=crear_boton_curso(frame_botones_sup,"1ºD",0.50,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 1ºD"))
boton_2a=crear_boton_curso(frame_botones_sup,"2ºA",0.64,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 2ºA"))
boton_2b=crear_boton_curso(frame_botones_sup,"2ºB",0.78,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 2ºB"))
boton_siguiente_2=crear_boton_cambio(frame_botones_sup,"-->",0.92,0.5,frame_botones_sup2)

boton_volver_1=crear_boton_cambio(frame_botones_sup2,"<--",0.08,0.5,frame_botones_sup)
boton_2c=crear_boton_curso(frame_botones_sup2,"2ºC",0.22,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 2ºC"))
boton_2d=crear_boton_curso(frame_botones_sup2,"2ºD",0.36,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 2ºD"))
boton_3a=crear_boton_curso(frame_botones_sup2,"3ºA",0.50,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 3ºA"))
boton_3b=crear_boton_curso(frame_botones_sup2,"3ºB",0.64,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 3ºB"))
boton_3c=crear_boton_curso(frame_botones_sup2,"3ºC",0.78,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 3ºC"))
boton_siguiente_3=crear_boton_cambio(frame_botones_sup2,"-->",0.92,0.5,frame_botones_sup3)

boton_volver_2=crear_boton_cambio(frame_botones_sup3,"<--",0.08,0.5,frame_botones_sup2)
boton_3d=crear_boton_curso(frame_botones_sup3,"3ºD",0.22,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 3ºD"))

##################

frame_acciones=tk.Frame(ventana,width=795,height=60,bg="#fff")
frame_acciones.pack(side="bottom")
frame_acciones.pack_propagate(False)

boton_nuevo=tk.Button(frame_acciones,text="Nuevo",bg="#4575F4",fg="#111",relief="flat",width=10,pady=0,font=("Cambria",14,"bold"),borderwidth=2, overrelief="solid")#1751ED
boton_nuevo.place(relx=0.17,rely=0.5,anchor="center")

boton_modificar=tk.Button(frame_acciones,text="Modificar",bg="#4575F4",fg="#111",relief="flat",width=10,pady=0,font=("Cambria",14,"bold"),borderwidth=2, overrelief="solid")
boton_modificar.place(relx=0.39,rely=0.5,anchor="center")

boton_eliminar=tk.Button(frame_acciones,text="Eliminar",bg="#4575F4",fg="#111",relief="flat",width=10,pady=0,font=("Cambria",14,"bold"),borderwidth=2, overrelief="solid")
boton_eliminar.place(relx=0.61,rely=0.5,anchor="center")

boton_guardar=tk.Button(frame_acciones,text="Guardar",bg="#4575F4",fg="#111",relief="flat",width=10,pady=0,font=("Cambria",14,"bold"),borderwidth=2, overrelief="solid")
boton_guardar.place(relx=0.83,rely=0.5,anchor="center")


##################



# Crear un estilo para el Treeview
style = ttk.Style()

# Configurar el estilo del Treeview
style.configure("Custom.Treeview", borderwidth=0, relief="flat")
style.configure("Custom.Treeview.Heading", borderwidth=0, relief="flat")

tree=ttk.Treeview(ventana)
tree.pack(fill="both",side="right")

tree["columns"]=["Año","Nombre","Apellido","Ingreso","DNI","Obs"]

tree.column('#0', width=0, stretch=tk.NO)
tree.column('Año', anchor=tk.CENTER, width=85)
tree.column('Nombre', anchor=tk.CENTER, width=140)
tree.column('Apellido', anchor=tk.CENTER, width=140)
tree.column('Ingreso', anchor=tk.CENTER, width=115)
tree.column('DNI', anchor=tk.CENTER, width=115)
tree.column('Obs', anchor=tk.CENTER, width=210)

tree.heading("#0",text="",anchor=tk.CENTER)
tree.heading("Año",text="Curso:",anchor=tk.CENTER)
tree.heading("Nombre",text="Nombre/s",anchor=tk.CENTER)
tree.heading("Apellido",text="Apellido/s",anchor=tk.CENTER)
tree.heading("Ingreso",text="F.Ingreso",anchor=tk.CENTER)
tree.heading("DNI",text="DNI",anchor=tk.CENTER)
tree.heading("Obs",text="Observaciones",anchor=tk.CENTER)

tree.insert(parent='', index='end', id=0, text='', values=("5to","Matias","Gauto",2020,48384544,"qsy esto es un texto de prueba para ver como queda esta parte de la tabla"))
tree.insert(parent='', index='end', id=1, text='', values=("5to","Matias","Gauto",2020,48384544,"qsy esto es un texto de prueba para ver como queda esta parte de la tabla"))
tree.insert(parent='', index='end', id=2, text='', values=("5to","Matias","Gauto",2020,48384544,"qsy esto es un texto de prueba para ver como queda esta parte de la tabla"))
tree.insert(parent='', index='end', id=3, text='', values=("5to","Matias","Gauto",2020,48384544,"qsy esto es un texto de prueba para ver como queda esta parte de la tabla"))
tree.insert(parent='', index='end', id=4, text='', values=("5to","Matias","Gauto",2020,48384544,"qsy esto es un texto de prueba para ver como queda esta parte de la tabla"))
tree.insert(parent='', index='end', id=5, text='', values=("5to","Matias","Gauto",2020,48384544,"qsy esto es un texto de prueba para ver como queda esta parte de la tabla"))
tree.insert(parent='', index='end', id=6, text='', values=("5to","Matias","Gauto",2020,48384544,"qsy esto es un texto de prueba para ver como queda esta parte de la tabla"))
tree.insert(parent='', index='end', id=7, text='', values=("5to","Matias","Gauto",2020,48384544,"qsy esto es un texto de prueba para ver como queda esta parte de la tabla"))
tree.insert(parent='', index='end', id=8, text='', values=("5to","Matias","Gauto",2020,48384544,"qsy esto es un texto de prueba para ver como queda esta parte de la tabla"))



ventana.mainloop()