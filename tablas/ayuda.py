import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

# Crear la ventana principal
root = tk.Tk()
root.title("Selector de Fecha")

# Crear un campo de entrada para la fecha
label_fecha = ttk.Label(root, text="Seleccione una fecha:")
label_fecha.pack(padx=10, pady=5)

cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd-mm-yyyy')
cal.pack(padx=10, pady=10)

# Función para mostrar la fecha seleccionada
def mostrar_fecha():
    fecha = cal.get()
    label_resultado.config(text=f"Fecha seleccionada: {fecha}")

# Botón para obtener la fecha seleccionada
btn_mostrar_fecha = ttk.Button(root, text="Mostrar Fecha", command=mostrar_fecha)
btn_mostrar_fecha.pack(padx=10, pady=5)

# Etiqueta para mostrar el resultado
label_resultado = ttk.Label(root, text="")
label_resultado.pack(padx=10, pady=5)

# Iniciar el bucle principal de la aplicación
root.mainloop()
