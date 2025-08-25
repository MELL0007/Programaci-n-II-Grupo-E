import tkinter as tk
from tkinter import messagebox
 
ventana=tk.Tk()
ventana.title("SISTEMA DE REGISTRO DE PACIENTES")
ventana.geometry("600x400")
ventana.configure(bg="#fdcae1")
 
#barra de menu
barraMenu=tk.Menu(ventana)
ventana.config(menu=barraMenu)
 
#funciones paciente
def nuevoPaciente():
    ventanaRegistro=tk.Toplevel(ventana)
    #crea una  ventana nueva secundaria (independiente asociada a ventana principal)
    ventanaRegistro.title("Registro paciente")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="#ffe5f0")
   
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre:")
    nombreLabel.grid(row=0,column=0,padx=10,pady=5,sticky="n")#"n=norte",s=sur,e=este,"w"=oeste,we,ns
    entryNombre=tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0,column=1,padx=10,pady=5,sticky="ns")
    nombreLabel.configure(bg="#ffe5f0")
   
    direccionLabel=tk.Label(ventanaRegistro,text="Dirección:")
    direccionLabel.grid(row=1,column=0,padx=10,pady=5,sticky="n")
    direccionLabel.configure(bg="#ffe5f0")
    entryDireccion=tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=1,column=1,padx=10,pady=5,sticky="ns")
   
    telefonoLabel=tk.Label(ventanaRegistro,text="Teléfono:")
    telefonoLabel.grid(row=2,column=0,padx=10,pady=5,sticky="n")
    telefonoLabel.configure(bg="#ffe5f0")
    entryTelefono=tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=2,column=1,padx=10,pady=5,sticky="ns")
   
    #sexo("RADIODIOBUTTOM")
    sexoLabel=tk.Label(ventanaRegistro,text="Sexo:")
    sexoLabel.grid(row=3,column=0,padx=10,pady=5,sticky="w")
    sexoLabel.configure(bg="#ffe5f0")
    sexo=tk.StringVar(value="Masculino")
    #es una variable espcial de tkinter que se utiliza para enlazar widgets ,que aprece eso por defecto
    rbMasculino=tk.Radiobutton(ventanaRegistro,text="Masculino",variable=sexo,value="Masculino")
    rbMasculino.grid(row=3,column=1,sticky="w")
    rbFemenino=tk.Radiobutton(ventanaRegistro,text="Femenino",variable=sexo,value="Femenino")
    rbFemenino.grid(row=4,column=1,sticky="w")
    rbFemenino.configure(bg="#ffe5f0")
    rbMasculino.configure(bg="#ffe5f0")
   
    #enefermedades base(chekbuttom)
    enfLabel=tk.Label(ventanaRegistro,text="Enfermedades base:")
    enfLabel.grid(row=5,column=0,padx=10,pady=5,sticky="w")
    diabetes=tk.BooleanVar()
    hipertension=tk.BooleanVar()
    asma=tk.BooleanVar()
    cbDiabetes=tk.Checkbutton(ventanaRegistro,text="Diabetes",variable=diabetes)
    cbDiabetes.grid(row=5,column=1,sticky="w")
    cbHipertension=tk.Checkbutton(ventanaRegistro,text="hipertension",variable=hipertension)
    cbHipertension.grid(row=6,column=1,sticky="w")
    cbAsma=tk.Checkbutton(ventanaRegistro,text="asma",variable=asma)
    cbAsma.grid(row=7,column=1,sticky="w")
    cbAsma.configure(bg="#ffe5f0")
    cbDiabetes.configure(bg="#ffe5f0")
    cbHipertension.configure(bg="#ffe5f0")
    enfLabel.configure(bg="#ffe5f0")
   
    #--ACCION RESGISTRAR DATOS--
    def registrarDatos():
        enfermedades=[]#es un vector
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("Hipertension")
        if asma.get():
            enfermedades.append("asma")
        if len(enfermedades)>0:
            enfermedadesTexto=','.join(enfermedades)
        else:
            enfermedadesTexto='ninguna'
        #cadena para mostrar todos los datos del formulario
        info=(
            f"Nombre:{entryNombre.get()}\n"
            f"Direccion:{entryDireccion.get()}\n"
            f"Telefono:{entryTelefono.get()}\n"
            f"Sexo:{sexo.get()}\n"
            f"Enfermedades:{enfermedadesTexto}"        
        )
        messagebox.showinfo("Datos Registrados",info)
        ventanaRegistro.destroy()#cierra ventana 
    btnRegistrar=tk.Button(ventanaRegistro,text="Datos Registrados",command=registrarDatos)
    btnRegistrar.grid(row=9,column=0,columnspan=2,pady=15)   

def buscarPaciente():
    messagebox.showinfo("buscar pacientes","este es el espacio para buscar pacientes")
   
def eliminarPaciente():
    messagebox.showinfo("eliminar paciente","este es el espacio para eliminar pacientes")
   
#menu pacientes
menuPacientes=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="PACIENTES",menu=menuPacientes)
menuPacientes.add_command(label="nuevo paciente",command=nuevoPaciente)
menuPacientes.add_command(label="buscar pacientes",command=buscarPaciente)
menuPacientes.add_command(label="eliminar paciente",command=eliminarPaciente)
menuPacientes.add_separator()
menuPacientes.add_command(label="salir",command=ventana.quit)

#funciones doctor
def nuevoDoctor():
    ventanaRegistro=tk.Toplevel(ventana)
    #crea una  ventana nueva secundaria (independiente asociada a ventana principal)
    ventanaRegistro.title("Registro doctor")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="#ffe5f0")
   
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre:")
    nombreLabel.grid(row=0,column=0,padx=10,pady=5,sticky="n")#"n=norte",s=sur,e=este,"w"=oeste,we,ns
    entryNombre=tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0,column=1,padx=10,pady=5,sticky="ns")
    nombreLabel.configure(bg="#ffe5f0")
   
    direccionLabel=tk.Label(ventanaRegistro,text="Dirección:")
    direccionLabel.grid(row=1,column=0,padx=10,pady=5,sticky="n")
    direccionLabel.configure(bg="#ffe5f0")
    entryDireccion=tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=1,column=1,padx=10,pady=5,sticky="ns")
   
    telefonoLabel=tk.Label(ventanaRegistro,text="Teléfono:")
    telefonoLabel.grid(row=2,column=0,padx=10,pady=5,sticky="n")
    telefonoLabel.configure(bg="#ffe5f0")
    entryTelefono=tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=2,column=1,padx=10,pady=5,sticky="ns")
   
    #sexo("RADIODIOBUTTOM")
    sexoLabel=tk.Label(ventanaRegistro,text="Sexo:")
    sexoLabel.grid(row=3,column=0,padx=10,pady=5,sticky="w")
    sexoLabel.configure(bg="#ffe5f0")
    sexo=tk.StringVar(value="Masculino")
    #es una variable espcial de tkinter que se utiliza para enlazar widgets ,que aprece eso por defecto
    rbMasculino=tk.Radiobutton(ventanaRegistro,text="Masculino",variable=sexo,value="Masculino")
    rbMasculino.grid(row=3,column=1,sticky="w")
    rbFemenino=tk.Radiobutton(ventanaRegistro,text="Femenino",variable=sexo,value="Femenino")
    rbFemenino.grid(row=4,column=1,sticky="w")
    rbFemenino.configure(bg="#ffe5f0")
    rbMasculino.configure(bg="#ffe5f0")
 
def buscarDoctor():
    messagebox.showinfo("nuevo paciente espacio para buscar doctor","este es el espacio para buscar doctor")
   
def eliminarDoctor():
    messagebox.showinfo("nuevo paciente espacio para eliminar paciente","este es el espacio para eliminar doctor")
 
#menu Doctor
menuDoctor=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="DOCTORES",menu=menuDoctor)
menuDoctor.add_command(label="nuevo doctor",command=nuevoDoctor)
menuDoctor.add_command(label="buscar doctor",command=buscarDoctor)
menuDoctor.add_command(label="eliminar doctor",command=eliminarDoctor)
menuDoctor.add_separator()
menuDoctor.add_command(label="salir",command=ventana.quit)
 
 
#menu ayuda
menuAyuda=tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="AYUDA",menu=menuAyuda)
menuAyuda.add_command(label="Acerca de ",command=lambda:messagebox.showinfo("acerca de ","version 1.0 -sistema Biomedicina"))
 
ventana.mainloop()