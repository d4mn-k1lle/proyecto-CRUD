import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.geometry("300x200")

# Crear un Menubutton
menu_button = tk.Menubutton(root, text="Desplegar opciones", relief="raised")
menu_button.grid(pady=20)

# Crear un menú desplegable
menu = tk.Menu(menu_button, tearoff=0)
menu_button.config(menu=menu)

# Añadir opciones al menú desplegable
menu.add_command(label="Opción 1", command=lambda: print("Opción 1 seleccionada"))
menu.add_command(label="Opción 2", command=lambda: print("Opción 2 seleccionada"))
menu.add_command(label="Opción 3", command=lambda: print("Opción 3 seleccionada"))

# Ejecutar la ventana
root.mainloop()
