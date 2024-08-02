import tkinter as tk
#arbol
from tkinter import ttk
from bd import mostrar_tabla,crear_conexion
from PIL import Image,ImageTk
#para moverse entre tablas
from ayudas import abrir_archivo
#boton agregar y modificar
from agregar import crear_agregar
from modificar import crear_modificar
from eliminar import crear_eliminar

def tablita(conexion,curso):
    consulta=f"select * from estudiantes where curso='{curso}';"
    data=mostrar_tabla(conexion,consulta)
    
    for item in arboledo.get_children():
        arboledo.delete(item)
    
    for row in data:
        arboledo.insert("", "end", values=row)
        
    conexion.close()
    

#creamos la ventana principal
ventana=tk.Tk()
ventana.title("Ventana Principal")
ventana.geometry("960x560")
ventana.resizable(False,False)
#es obligatoria ya que hace que se pueda superponer un frame sobre otro(botones de arriba 1a,1b,1c cunado pasas pagina se cambia a otro frame y asi la cantidad necesaria)
def show_frame(frame):
    frame.tkraise()
    
#esto dsp va hacer que al ejecutar un boton de los de arriba no solo modifique el titulo sino tambien la tabla para que muestre solo lo de ese curso
def DosEnUno(label,texto,curso):
    conexion=crear_conexion()
    label.config(text=texto)
    tablita(conexion,curso)
    
#funcion para crear los botones de la izquierda,(el estado es para que el boton de "superior no se pueda presionar ni interactue(deshabilitado)")
def crear_boton_izq(frame,texto,relx,rely,estado,pady,ruta):
    boton=tk.Button(frame,text=texto,font=("Times",14,"bold"),width=10,height=1,bg="#fff",fg="#111",borderwidth=2,relief="flat",activebackground="#fff",activeforeground="#111", overrelief="solid",state=estado,disabledforeground="#111",pady=pady,command=lambda:abrir_archivo(ventana,ruta))
    boton.place(relx=relx,rely=rely)#0.12,0.05


#-- para los botones superiores, asi ahorro mucho codigo y es mas facil entenderlo --#
#basicamente es una plantilla
def crear_boton_curso(frame, nombre, relx, rely,comando):
    boton = tk.Button(frame, text=nombre, width=10, height=1, bg="#4575F4", fg="#000", font=("Cambria", 10, "bold"), bd=2,relief="flat",activebackground="#4575F4",activeforeground="#111", overrelief="solid", pady=5,command=comando)#3C5BBA
    boton.place(relx=relx, rely=rely, anchor="center")
    return boton

#para los botones de arriba de pasar de "pagina" osea los "-->,<--", la diferencia esta en el comando que en vez de elegirlo ya solo pones el frame al cual vas a mandar al frente
def crear_boton_cambio(frame,nombre,relx,rely,frame_elegido):
    boton=tk.Button(frame,text=nombre,width=10, height=1,pady=5, bg="#4575F4", fg="#000", font=("Cambria", 10, "bold"), bd=2,relief="flat",activebackground="#4575F4",activeforeground="#111", overrelief="solid",command=lambda:show_frame(frame_elegido))
    boton.place(relx=relx,rely=rely,anchor="center")#0.92,0.5

#fin de las funciones secundarias
#-------------------------------------------------------------------------------#
#inicio del codigo 

#-- creamos el frame izquierdo donde van a ir los botones para desplazarte entre distintas tablas y donde va estar el logo (por el momento al menos), una idea mia es que al clickar el logo te mande al panel de control, no es muy dificil --#
frame_izq=tk.Frame(ventana,width=165,height=560,bg="#3C5BBA")
frame_izq.pack(side="left")
frame_izq.pack_propagate(False)

#---------------#

#-- creamos un frame para el logo dentro del frame del titulo y hacemos que no se pueda achicar ni agrandar --#
frame_logo=tk.Frame(frame_izq,width=165,height=125,bg="#3C5BBA")#,bd=1,relief=tk.SOLID
frame_logo.pack(side=tk.TOP)
frame_logo.pack_propagate(False)

#-- le damos la ruta de la imagen y lo metemos en image --# 
image_path = "login_intento-legible.8/imagenes/logo_escuela.png" 
image = Image.open(image_path)

#-- le damos el tamaño y la achicamos con calidad con lanczos --#
new_size = (93,100)  
resized_image = image.resize(new_size, Image.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)

#--la metemos en un label para que se vea y ubicamos el label en el centro del frame del logo--#
image_label = tk.Label(frame_logo, image=photo,bg="#3C5BBA")
image_label.place(relx=0.5, rely=0.5, anchor='center')
#a esta parte del logo lo ideal seria despues hacerla mas eficiente con una funcion
#---------------#

#frame para los botones de la izquierda
frame_botones_izq=tk.Frame(frame_izq,width=165,height=435,bg="#3C5BBA")
frame_botones_izq.pack(side="bottom")

#---------------#
#botones de la izquierda
#-- creamos el boton de ciclo basico --#
boton_Basico=crear_boton_izq(frame_botones_izq,"Basico",0.12,0.05,"active",1,"tablas/tabla_basico.py")

#-- creamos el boton de Ciclo Superior (deshabilitado)--#
boton_Superior=crear_boton_izq(frame_botones_izq,"Superior:",0.12,0.20,"disabled",4,"tablas/tabla-basico.py")

#-- creamos el boton de MMO --#
boton_Mmo=crear_boton_izq(frame_botones_izq,"MMO",0.12,0.304,"active",4,"tablas/tabla_MMO.py")

#-- creamos el boton de informatica --#
boton_Informatica=crear_boton_izq(frame_botones_izq,"Informatica",0.12,0.408,"active",4,"tablas/tabla_informatica.py")

#-- creamos el boton de Programacion --#
boton_Programacion=crear_boton_izq(frame_botones_izq,"Programacion",0.12,0.511,"active",4,"tablas/tabla_programacion.py")

#-- creamos el boton de Egresados --#
boton_Egresados=crear_boton_izq(frame_botones_izq,"Egresados",0.12,0.66,"active",1,"tablas/tabla_egresados.py")

#-- creamos el boton de Exalumnos --#
boton_est_pase=crear_boton_izq(frame_botones_izq,"Exalumnos",0.12,0.8,"active",1,"tablas/tabla_e_pases.py")

#---------------#

#creamos el frame superior(donde estan los botones de 1a,1b,1c)
frame_cursos=tk.Frame(ventana,width=795,height=130,bg="#ccc")
frame_cursos.pack(side="top")
frame_cursos.pack_propagate(False)

#---------------#

#creamos el frame donde va estar ubicado el titulo de cada tabla
frame_titulo_tabla=tk.Frame(frame_cursos,bg="#fff",width=795,height=80,)
frame_titulo_tabla.pack(side="bottom")

#---------------#

#creamos el titulo, que luego modificaremos dependiendo del boton
titulo_tabla=tk.Label(frame_titulo_tabla,text="Superior Programacion",bg="#fff",fg="#111",font=("Cambria",40,"bold"))
titulo_tabla.place(relx=0.5,rely=0.45,anchor=("center"))

#---------------#

#creamos los 3 frames donde van a estar los 1ros,2dos y 3ros
frame_botones_sup2=tk.Frame(frame_cursos,width=795,height=50,bg="#fff")
frame_botones_sup3=tk.Frame(frame_cursos,width=795,height=50,bg="#fff")
frame_botones_sup=tk.Frame(frame_cursos,width=795,height=50,bg="#fff")

#---------------#
 
# Añadir los frames a la ventana principal, uno sobre el otro(al superponerse se ocultan los demas)
for frame in (frame_botones_sup,frame_botones_sup2,frame_botones_sup3):
    frame.place(x=0, y=0, width=795, height=50)

#---------------#

#creamos los botones con las funciones del principio y con el lambda hacemos que solo se ejecuten si se presiona el boton
boton_1a=crear_boton_curso(frame_botones_sup,"4º2",0.08,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Superior 4º2","4-2"))#################################### me falta hacer que funcione
boton_1b=crear_boton_curso(frame_botones_sup,"4º5",0.22,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Superior 4º5","4-5"))
boton_1c=crear_boton_curso(frame_botones_sup,"5º2",0.36,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Superior 5º2","5-2"))
boton_1d=crear_boton_curso(frame_botones_sup,"5º3",0.50,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Superior 5º3","5-3"))
boton_2a=crear_boton_curso(frame_botones_sup,"6º2",0.64,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Superior 6º2","6-2"))
boton_2b=crear_boton_curso(frame_botones_sup,"6º5",0.78,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Superior 6º5","6-5"))
# boton_siguiente_2=crear_boton_cambio(frame_botones_sup,"-->",0.92,0.5,frame_botones_sup2)
#fin del primer frame
#---------------#
#inicio del segundo
# boton_volver_1=crear_boton_cambio(frame_botones_sup2,"<--",0.08,0.5,frame_botones_sup)
boton_2c=crear_boton_curso(frame_botones_sup,"7º4",0.92,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Superior 7º4","7-4"))
# boton_2d=crear_boton_curso(frame_botones_sup2,"2ºD",0.36,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 2ºD","2d"))
# boton_3a=crear_boton_curso(frame_botones_sup2,"3ºA",0.50,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 3ºA","3a"))
# boton_3b=crear_boton_curso(frame_botones_sup2,"3ºB",0.64,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 3ºB","3b"))
# boton_3c=crear_boton_curso(frame_botones_sup2,"3ºC",0.78,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 3ºC","3c"))
# boton_siguiente_3=crear_boton_cambio(frame_botones_sup2,"-->",0.92,0.5,frame_botones_sup3)
#fin del segundo frame
#---------------#
#inicio del tercero, en un futuro se pueden crear muchos mas frames, es facil
# boton_volver_2=crear_boton_cambio(frame_botones_sup3,"<--",0.08,0.5,frame_botones_sup2)
# boton_3d=crear_boton_curso(frame_botones_sup3,"3ºD",0.22,0.5,lambda:DosEnUno(titulo_tabla,"Ciclo Basico 3ºD","3d"))
#fin del tercero

#---------------#

#creamos el frame de abajo donde van a estar ubicados los botones de agregar,modificar,borrar,(pendiente), pero si tienen que ser 4 botones por la estetica
frame_acciones=tk.Frame(ventana,width=795,height=60,bg="#fff")
frame_acciones.pack(side="bottom")
frame_acciones.pack_propagate(False)

#---------------#

boton_guardar=tk.Button(frame_acciones,text="Guardar",bg="#4575F4",fg="#111",relief="flat",width=10,pady=0,font=("Cambria",14,"bold"),borderwidth=2, overrelief="solid")
boton_guardar.place(relx=0.83,rely=0.5,anchor="center")

#---------------#

#el nombre arbol es para que no de error al ponerle tree que es el mismo nombre que un parametro
arboledo=ttk.Treeview(ventana)
arboledo.pack(fill="both",side="right")

#definimos como vamos a acceder a las columnas 
arboledo["columns"]=["Año","Nombre","Apellido","Ingreso","DNI","Obs"]

#las creamos, la columna "#0" sinceramente no se para que sirve chat gpt me dijo que era necesaria
arboledo.column('#0', width=0, stretch=tk.NO)
arboledo.column('Año', anchor=tk.CENTER, width=85)
arboledo.column('Nombre', anchor=tk.CENTER, width=140)
arboledo.column('Apellido', anchor=tk.CENTER, width=140)
arboledo.column('Ingreso', anchor=tk.CENTER, width=115)
arboledo.column('DNI', anchor=tk.CENTER, width=115)
arboledo.column('Obs', anchor=tk.CENTER, width=210)
#---------------#
#les ponemos nombre a las columnas y donde se va ubicar el texto de cada cabecera
arboledo.heading("#0",text="",anchor=tk.CENTER)
arboledo.heading("Año",text="Curso:",anchor=tk.CENTER)
arboledo.heading("Nombre",text="Nombre/s",anchor=tk.CENTER)
arboledo.heading("Apellido",text="Apellido/s",anchor=tk.CENTER)
arboledo.heading("Ingreso",text="F.Ingreso",anchor=tk.CENTER)
arboledo.heading("DNI",text="DNI",anchor=tk.CENTER)
arboledo.heading("Obs",text="Observaciones",anchor=tk.CENTER)
#---------------#
#esto es provisional para saber cuanto ocupa y como queda con algunos datos
arboledo.insert(parent='', index='end', id=0, text='', values=("5to","Matias","Gauto",2020,48384544,"qsy esto es un texto de prueba para ver como queda esta parte de la tabla"))
arboledo.insert(parent='', index='end', id=1, text='', values=("5to","Matias","Gauto",2020,48384544,"qsy esto es un texto de prueba para ver como queda esta parte de la tabla"))

    
#el boton de crear esta dsp, pq sino no me toma el arboledo ya que sino no existiria, en resumen, los 4 botones deben ir dsp del arboledo
boton_nuevo=tk.Button(frame_acciones,text="agregar",bg="#4575F4",fg="#111",relief="flat",width=10,pady=0,font=("Cambria",14,"bold"),borderwidth=2, overrelief="solid",command=lambda:crear_agregar(ventana,arboledo))#1751ED
boton_nuevo.place(relx=0.17,rely=0.5,anchor="center")

boton_modificar=tk.Button(frame_acciones,text="Modificar",bg="#4575F4",fg="#111",relief="flat",width=10,pady=0,font=("Cambria",14,"bold"),borderwidth=2, overrelief="solid",command=lambda:crear_modificar(ventana,arboledo))
boton_modificar.place(relx=0.39,rely=0.5,anchor="center")

boton_eliminar=tk.Button(frame_acciones,text="Eliminar",bg="#4575F4",fg="#111",relief="flat",width=10,pady=0,font=("Cambria",14,"bold"),borderwidth=2, overrelief="solid",command=lambda:crear_eliminar(ventana,arboledo))
boton_eliminar.place(relx=0.61,rely=0.5,anchor="center")



#mostramos la ventana
ventana.mainloop()