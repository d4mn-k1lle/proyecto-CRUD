import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplo de Entry con Imagen")

        self.entries = []  # Lista para almacenar referencias a los Entry widgets
        validate_cmd = self.root.register(self.validate_numbers)

        # Crear un Frame como contenedor
        self.frame = tk.Frame(root, bg="#fff")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Crear varios Entry widgets con imágenes
        self.crear_entry_con_img(self.frame, "imagen_path", 0.1, 0.1, "Texto 1", 0.1, 0.15, tk.StringVar(), 0.2, 0.15, 0.3, validate_cmd, only_numbers=True)
        self.crear_entry_con_img(self.frame, "imagen_path", 0.1, 0.3, "Texto 2", 0.1, 0.35, tk.StringVar(), 0.2, 0.35, 0.3, validate_cmd, only_numbers=False)

        # Botón para imprimir los valores de los Entry widgets
        print_button = tk.Button(self.frame, text="Imprimir Valores", command=self.print_entry_values)
        print_button.place(relx=0.1, rely=0.5)

    def crear_entry_con_img(self, new_frame, i, ubicacionx, ubicaciony, texto, ubi1, ubi2, textvar, ubirelx, ubirely, relwidth, validate_cmd, only_numbers=False):
        img = self.imagen(i)  # Función para obtener la imagen
        label_img = tk.Label(new_frame, image=img, bg="#fff")
        label_img.image = img  # Mantener la referencia de la imagen
        label_img.place(relx=ubicacionx, rely=ubicaciony)

        label1 = tk.Label(new_frame, text=texto, font=("Times", 14), fg="#666a88", bg="#fff")
        label1.place(relx=ubi1, rely=ubi2)

        if only_numbers:
            entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID, validate="key", validatecommand=(validate_cmd, '%S'))
        else:
            entry1 = tk.Entry(new_frame, textvariable=textvar, font=("Times", 13), fg="#222", bg="#fff", bd=1, relief=tk.SOLID)
        entry1.place(relx=ubirelx, rely=ubirely, relwidth=relwidth)

        self.entries.append(entry1)  # Agregar el Entry a la lista de entries

    def imagen(self, path):
        # Aquí deberías cargar y devolver la imagen a partir del path
        # Por ahora, solo devolvemos un placeholder
        return tk.PhotoImage(file=path)

    def validate_numbers(self, char):
        return char.isdigit()

    def print_entry_values(self):
        for entry in self.entries:
            print(entry.get())

# Configuración de la ventana principal
root = tk.Tk()
app = App(root)
root.mainloop()
