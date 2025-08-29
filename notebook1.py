#importacion de librerías
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
#"crear ventana principal"
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Libro pacientes y doctores")
ventanaPrincipal.geometry("600x800")

#crear contenedores notebook(pestañas)
pestañas=ttk.Notebook(ventanaPrincipal)
#crear frames(uno por pestañas)
frame_pacientes=ttk.Frame(pestañas)
#agregar pestañas al notebook
pestañas.add(frame_pacientes,text="Pacientes")

#mostrar las pestañas en la ventana
pestañas.pack(expand=True,fill="both")

#nombre
labelNombre=tk.Label(frame_pacientes,text="Nombre completo:")
labelNombre.grid(row=0,column=0,sticky="w",padx=5,pady=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1,padx=5,pady=5,sticky="w")

#fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes,text="Fecha de nacimiento:")
labelFechaN.grid(row=1,column=0,sticky="w",padx=5,pady=5)
fechaP=tk.Entry(frame_pacientes)
fechaP.grid(row=1,column=1,padx=5,pady=5,sticky="w") 

#edad(readonly)
labelEdad=tk.Label(frame_pacientes,text="Edad:")
labelEdad.grid(row=2,column=0,padx=5,pady=5,sticky="w")
edadP=tk.Entry(frame_pacientes,state="readonly")
edadP.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#genero(radio button)
labelGenero=tk.Label(frame_pacientes,text="Genero:")
labelGenero.grid(row=3,column=0,sticky="w",padx=5,pady=5)
genero=tk.StringVar()
genero.set("Maculino")#valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes,text="Mascuino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,sticky="w",padx=5,pady=5)
radioFemenino=ttk.Radiobutton(frame_pacientes,text="femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,padx=5,pady=5,sticky="w")

#Grupo Sanguíneo
labelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo sanguíneo:")
labelGrupoSanguineo.grid(row=5,column=0,sticky="w",padx=5,pady=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5,column=1,sticky="w",padx=5,pady=5)

#tipo de seguro
labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de seguro:")
labelTipoSeguro.grid(row=6,column=0,sticky="w",padx=5,pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Público")#valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes,values=["Público","Privado","Ninguno"],textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6,column=1,sticky="w",padx=5,pady=5)

#centro medico
labelCentroMedico=tk.Label(frame_pacientes,text="Centro de salud:")
labelCentroMedico.grid(row=7,column=0,sticky="w",padx=5,pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital central")#valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes,values=["Hospital central","Centro Sur","Clínica Norte"],textvariable=centro_medico)
comboCentroMedico.grid(row=7,column=1,sticky="w",padx=5,pady=5)
#crear frame doctores
frame_doctores=ttk.Frame(pestañas)
#añadir a la ventana principal 
pestañas.add(frame_doctores,text="Doctores")

ventanaPrincipal.mainloop()