# import tkinter as tk
# from tkinter import ttk

# # Funciones para cambiar de pantalla
# def mostrar_pantalla_curso(curso):
#     pantalla.config(text=f"Pantalla del curso: {curso}")

# def agregar_persona():
#     pass  # Implementar la lógica para agregar una persona

# def quitar_persona():
#     pass  # Implementar la lógica para quitar una persona

# def mostrar_pantalla_ciclo(ciclo):
#     pantalla.config(text=f"Pantalla del ciclo: {ciclo}")

# def mostrar_especialidad(especialidad):
#     pantalla.config(text=f"Pantalla de la especialidad: {especialidad}")

# def mostrar_pantalla_pases():
#     pantalla.config(text="Pantalla de Pases")

# def mostrar_pantalla_egresados():
#     pantalla.config(text="Pantalla de Egresados")

# # Crear la ventana principal
# root = tk.Tk()
# root.title("Sistema de Gestión Escolar")
# root.geometry("800x600")  # Ajustar el tamaño de la ventana principal

# # Frame de los cursos
# frame_cursos = tk.Frame(root)
# frame_cursos.pack(side=tk.TOP, fill=tk.X)

# # Botones de cursos
# cursos = ["Curso 1", "Curso 2", "Curso 3", "Curso 4"]
# for curso in cursos:
#     boton = tk.Button(frame_cursos, text=curso, command=lambda c=curso: mostrar_pantalla_curso(c))
#     boton.pack(side=tk.LEFT)

# # Frame de opciones laterales
# frame_opciones = tk.Frame(root)
# frame_opciones.pack(side=tk.LEFT, fill=tk.Y)

# # Botones de ciclo básico y superior
# boton_ciclo_basico = tk.Button(frame_opciones, text="Ciclo Básico", command=lambda: mostrar_pantalla_ciclo("Ciclo Básico"))
# boton_ciclo_basico.pack(fill=tk.X)

# menu_ciclo_superior = ttk.Menubutton(frame_opciones, text="Ciclo Superior")
# menu_superior = tk.Menu(menu_ciclo_superior, tearoff=0)
# menu_superior.add_command(label="MMO", command=lambda: mostrar_especialidad("MMO"))
# menu_superior.add_command(label="Informática", command=lambda: mostrar_especialidad("Informática"))
# menu_superior.add_command(label="Programación", command=lambda: mostrar_especialidad("Programación"))
# menu_ciclo_superior.config(menu=menu_superior)
# menu_ciclo_superior.pack(fill=tk.X)

# boton_pases = tk.Button(frame_opciones, text="Pases", command=mostrar_pantalla_pases)
# boton_pases.pack(fill=tk.X)

# boton_egresados = tk.Button(frame_opciones, text="Egresados", command=mostrar_pantalla_egresados)
# boton_egresados.pack(fill=tk.X)

# pantalla = tk.Label(root, text="Seleccione una opción", relief=tk.SUNKEN, anchor=tk.CENTER)
# pantalla.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# frame_personas = tk.Frame(root)
# frame_personas.pack(side=tk.BOTTOM, fill=tk.X)

# boton_agregar_persona = tk.Button(frame_personas, text="Agregar Persona", command=agregar_persona)
# boton_agregar_persona.pack(side=tk.LEFT)

# boton_quitar_persona = tk.Button(frame_personas, text="Quitar Persona", command=quitar_persona)
# boton_quitar_persona.pack(side=tk.LEFT)

# # Iniciar el bucle principal de la interfaz
# root.mainloop()
