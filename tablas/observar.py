import tkinter as tk

def observar(root):
    
    seleccionado = tree.selection()
    if not seleccionado:
                # raise ValueError("No hay selección")
                print("No hay selección")
                return top.destroy()
    valores = tree.item(seleccionado, 'values')
    print(tree.item(seleccionado,'values'))
        
    top=tk.Toplevel(root)
    top.geometry("420x360")
    top.title("Observar estudiante")
    frame_titulo=tk.Frame(top,bg="#fff",height=100,width=420)
    frame_titulo.place(relx=0.0,rely=0.0)
    
    
    top.mainloop()
    
ventana=tk.Tk()
observar(ventana)
ventana.mainloop()