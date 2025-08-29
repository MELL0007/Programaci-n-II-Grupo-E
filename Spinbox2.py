#Spinbox de números del 1 al 10 para edad
import tkinter as tk 
from tkinter import messagebox
ventana=tk.Tk()
ventana.geometry("300x400")
#funcion edad y genero
def mostrarEdad():
    tk.messagebox.showinfo("edad",f"la edad seleccionada es:{spin.get()}")
    
def mostrarGenero():
    tk.messagebox.showinfo("genero",f"el genero seleccionado es :{genero.get()}")

#SpinBox para edad    
#edad                      
labelEdad=tk.Label(ventana,text="edad")
labelEdad.grid(row=0,column=0,padx=5,pady=5,sticky="w")
spin=tk.Spinbox(ventana,from_=1,to=10)
spin.grid(row=0,column=1,padx=10,pady=10)
boton=tk.Button(ventana,text="obtener valor",command=mostrarEdad)
boton.grid(row=1,column=0,padx=10,pady=10)

#genero
labelGenero=tk.Label(ventana,text="Genero")
labelGenero.grid(row=2,column=0,padx=5,pady=5,sticky="w")
genero=tk.Spinbox(ventana,values=("Maculino","femenino","otro"))
genero.grid(row=2,column=1,padx=10,pady=10)
botonGenero=tk.Button(ventana,text="obtener valor",command=mostrarGenero)
botonGenero.grid(row=3,column=0,padx=10,pady=10)

ventana.mainloop()