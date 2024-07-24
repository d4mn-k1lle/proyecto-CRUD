from PIL import ImageTk,Image
import tkinter as tk
import subprocess
from tkinter import messagebox

#creamos la clase para luego importarla entera 
class frames_imagenes:
    #usamos el metodo init y le asignamos los valores para que despues se pueda trabajar 
    def __init__(self,ventana,aplicacion_ancho,aplicacion_largo):
        self.ventana=ventana
        self.aplicacion_ancho=aplicacion_ancho        
        self.aplicacion_largo=aplicacion_largo

    #centramos la ventana, los argumentos deberian ser entonces:root,el width y el height
    def centrar_ventana(self):
            pantalla_ancho=self.ventana.winfo_screenwidth()
            pantalla_largo=self.ventana.winfo_screenheight()
            x=int((pantalla_ancho/2) - (self.aplicacion_ancho/2))
            y=int((pantalla_largo/2) - (self.aplicacion_largo/2))
            self.ventana.geometry(f"{self.aplicacion_ancho}x{self.aplicacion_largo}+{x}+{y}")

    #damos la ruta y el tamaño de la imagen para luego con un metodo como pack o place ubicarla
    def leer_imagen(self,ruta,tamaño):
        return ImageTk.PhotoImage(Image.open(ruta).resize(tamaño,Image.LANCZOS))

    #creamos una funcion para un frame auxiliar
    def crear_frame_auxiliar(self, master, altura):
        frame_auxiliar = tk.Frame(master, bg="#f0f0f0", width=420, height=altura)
        frame_auxiliar.pack(side=tk.TOP, fill="x")
        frame_auxiliar.pack_propagate(False)
        return frame_auxiliar
    
    #creamos la funcion para que me envie al registro
    def abrir_archivo(self):
        ruta_archivo = "login_intento-legible.8/intento-registro4.py"
        try:
            subprocess.Popen(["python", ruta_archivo])
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"No se pudo encontrar el archivo: {ruta_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {e}")
            
    #creamos la funcion igual nada mas que me envie al login
    def abrir_archivo_registro(self):
        ruta_archivo = "login_intento-legible.8/login-principal.py"
        try:
            subprocess.Popen(["python", ruta_archivo])
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"No se pudo encontrar el archivo: {ruta_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {e}")
            
    #destruye/cierra la ventana en la que estamos
    def cerrar_ventana(self):
        self.ventana.destroy()
    
    # def registro_ayuda(self,master,)
    #obtiene los valores de los entryr(no me acuerdo si lo termine usando)
    def obtener_valores(self):
        
        valor_entry1=self.var_entry1.get()
        valor_entry2=self.var_entry2.get()
        valor_entry3=self.var_entry3.get()
        valor_entry4=self.var_entry4.get()
        valor_entry5=self.var_entry5.get()
        valor_entry6=self.var_entry6.get()
        valor_entry7=self.var_entry7.get()