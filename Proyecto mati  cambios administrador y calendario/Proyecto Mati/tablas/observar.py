import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def mostrar_informacion(treeview, ventana):
    
    # Obtener el item seleccionado en el Treeview
    selected_item = treeview.selection()

    # Verificar si hay un item seleccionado
    if not selected_item:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un estudiante.")
        return

    # Obtener los valores del item seleccionado
    item_values = treeview.item(selected_item)['values']

    # Crear una nueva ventana para mostrar la información del estudiante
    info_ventana = tk.Toplevel(ventana)
    info_ventana.title("Información del Estudiante")
    info_ventana.geometry("400x400")
    info_ventana.configure(bg="#f0f0f0")

    # Crear un frame para contener los detalles del estudiante
    frame_info = tk.Frame(info_ventana, bg="#f0f0f0")
    frame_info.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Título principal
    title_label = tk.Label(frame_info, text="Detalles del Estudiante", bg="#f0f0f0", fg="#3C5BBA", font=("Cambria", 17, "bold"))
    title_label.pack(pady=(0, 10))

    # Usar un ttk.Treeview para mostrar los detalles excepto "Observaciones"
    tree = ttk.Treeview(frame_info, columns=("Detalle", "Valor"), show="headings", height=5)
    tree.heading("Detalle", text="Detalle")
    tree.heading("Valor", text="Valor")
    tree.column("Detalle", anchor=tk.W, width=150)
    tree.column("Valor", anchor=tk.W, width=200)

    # Insertar los detalles del estudiante en el Treeview
    labels_text = ["Curso:", "Nombre:", "Apellido:", "F. Ingreso:", "DNI:"]
    for i, value in enumerate(item_values[:-1]):  # Excluir "Observaciones"
        tree.insert("", "end", values=(labels_text[i], value))

    tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Mostrar "Observaciones" en un Text widget para soportar texto largo
    observ_label = tk.Label(frame_info, text="Observaciones:", bg="#f0f0f0", fg="#3C5BBA", font=("Cambria", 12))
    observ_label.pack(anchor="w", pady=(10, 0))

    observaciones_text = tk.Text(frame_info, height=5, wrap="word", bg="#fff", fg="#000", font=("Helvetica", 10))
    observaciones_text.insert(tk.END, item_values[-1])  # Insertar observaciones
    observaciones_text.config(state=tk.DISABLED)  # Desactivar edición
    observaciones_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    # Botón para cerrar la ventana de información
    cerrar_btn = tk.Button(info_ventana, text="Cerrar", command=info_ventana.destroy, bg="#3C5BBA", fg="#fff", relief="flat", font=("Helvetica",11,"bold"), activebackground="#fff", activeforeground="#3C5BBA", overrelief="solid", width=20)
    cerrar_btn.pack(pady=(5, 10))