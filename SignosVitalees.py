import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("SISTEMA DE REGISTRO DE PACIENTES")
ventana.geometry("600x400")
ventana.configure(bg="#bee2df")

# encabezado
titulolabel = tk.Label(ventana, text="Registro datos del paciente", font=("Arial", 16, "bold"))
titulolabel.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")
titulolabel.configure(bg="#bee2df", fg="black")

#--ACCION REGISTRAR DATOS--
def registrarDatos():
    info = (
        f"Nombre: {nombreD.get()}\n"
        f"Edad: {edadD.get()}\n"
        f"Frecuencia Cardiaca: {fcD.get()} lpm\n"
        f"Presión Arterial: {paD.get()}\n"
        f"Saturación de Oxígeno: {soD.get()} %\n"
        f"Temperatura: {tempD.get()} °C"
    )
    messagebox.showinfo("Datos Registrados", info)

# ================== FRAME 1: Datos del paciente ==================
frame_datos = tk.Frame(ventana, bg="#bee2df")
frame_datos.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# nombre
labelNombre = tk.Label(frame_datos, text="Nombre:", bg="#bee2df")
labelNombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)
nombreD = tk.Entry(frame_datos)
nombreD.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# edad
labelEdad = tk.Label(frame_datos, text="Edad:", bg="#bee2df")
labelEdad.grid(row=1, column=0, sticky="w", padx=5, pady=5)
edadD = tk.Entry(frame_datos)
edadD.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# ================== FRAME 2: Signos vitales ==================
frame_signos = tk.Frame(ventana, bg="#bee2df")
frame_signos.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# título signos vitales
signoslabel = tk.Label(frame_signos, text="Signos Vitales", font=("Arial", 14, "bold"), bg="#bee2df", fg="black")
signoslabel.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

# frecuencia cardíaca
labelFC = tk.Label(frame_signos, text="Frecuencia Cardiaca:", bg="#bee2df")
labelFC.grid(row=1, column=0, sticky="w", padx=5, pady=5)
fcD = tk.Entry(frame_signos)
fcD.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# presion arterial
labelPA = tk.Label(frame_signos, text="Presion Arterial:", bg="#bee2df")
labelPA.grid(row=2, column=0, sticky="w", padx=5, pady=5)
paD = tk.Entry(frame_signos)
paD.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# saturacion de oxigeno
labelSO = tk.Label(frame_signos, text="Saturacion de Oxigeno:", bg="#bee2df")
labelSO.grid(row=3, column=0, sticky="w", padx=5, pady=5)
soD = tk.Entry(frame_signos)       
soD.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# temperatura
labelTemp = tk.Label(frame_signos, text="Temperatura:", bg="#bee2df")
labelTemp.grid(row=4, column=0, sticky="w", padx=5, pady=5)
tempD = tk.Entry(frame_signos)
tempD.grid(row=4, column=1, padx=5, pady=5, sticky="w")

# ================== BOTÓN REGISTRAR ==================
btnRegistrar = tk.Button(ventana, text="Registrar", command=registrarDatos)
btnRegistrar.grid(row=3, column=0, pady=15)
btnRegistrar.configure(bg="#CCCDFA", fg="black")

ventana.mainloop()