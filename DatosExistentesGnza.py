from tkinter import *  # Ejemplo usando Tkinter

def verificar_alumno(dni):
    # Simulación de verificación de alumno duplicado
    lista_alumnos = [
        {'id': 1, 'nombre': 'Juan', 'apellido': 'Pérez', 'dni': '12345678'},
        {'id': 2, 'nombre': 'Ana', 'apellido': 'Gómez', 'dni': '87654321'}
    ]

    # Verificar si el alumno existe en la lista
    for alumno in lista_alumnos:
        if alumno['dni'] == dni:
            print("Alumno duplicado encontrado:")
            print(alumno)
            return True
    return False

# Ejemplo de uso en Tkinter:
root = Tk()
entry_dni = Entry(root)
entry_dni.pack()

def verificar():
    dni = entry_dni.get()
    if verificar_alumno(dni):
        # Manejar el caso de alumno duplicado
        pass
    else:
        # Agregar el nuevo alumno a la lista o manejar el caso
        pass

# Botón para verificar
button = Button(root, text="Verificar", command=verificar)
button.pack()

root.mainloop()
