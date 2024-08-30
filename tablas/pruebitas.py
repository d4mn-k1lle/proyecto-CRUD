import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime

root = tk.Tk()

# Obtener la fecha actual
fecha_actual = datetime.now()

# Crear el widget DateEntry con la fecha máxima establecida en la fecha actual
calendario = DateEntry(root, maxdate=fecha_actual)
calendario.pack(pady=20)

root.mainloop()
