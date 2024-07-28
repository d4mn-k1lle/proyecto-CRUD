import tkinter
from tkinter import messagebox

# Simulamos una base de datos con una lista
base_datos = ["47866259"]

# Función para validar que solo se ingresen números en la caja de texto
def solo_numeros(char):
    return char.isdigit()

# Función para eliminar un DNI de la base de datos
def eliminar_dni():
    dni = CajaTexto.get()
    if dni in base_datos:
        base_datos.remove(dni)
        messagebox.showinfo("Éxito", "El DNI ha sido eliminado de la base de datos.")
        ventana.destroy()  # Cierra la ventana principal y finaliza el programa
    else:
        messagebox.showerror("Error", "El DNI no existe en la base de datos.")

# Crear la ventana principal
ventana = tkinter.Tk()
ventana.geometry("300x200")

# Crear y centrar la primera etiqueta
etiqueta = tkinter.Label(ventana, text="Eliminar", bg="blue")
etiqueta.pack(fill = tkinter.X)

# Crear y centrar la segunda etiqueta
etiqueta2 = tkinter.Label(ventana, text="Indique el DNI del Alumno que quiera eliminar")
etiqueta2.place(relx=0.5, rely=0.4, anchor='center')

# Validar que solo se puedan ingresar números
vcmd = (ventana.register(solo_numeros), '%S')

# Crear y centrar la caja de texto
CajaTexto = tkinter.Entry(ventana, validate='key', validatecommand=vcmd)
CajaTexto.place(relx=0.5, rely=0.5, anchor='center')

# Crear y centrar el botón
botonE = tkinter.Button(ventana, text="Borrar", padx=40, pady=5, command=eliminar_dni)
botonE.place(relx=0.5, rely=0.7, anchor='center')

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
