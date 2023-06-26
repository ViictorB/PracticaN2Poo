#Ejercicio 2 - Unidad 4 - VB
from tkinter import *
from tkinter import ttk, messagebox

def calcular_iva():
    precio_base = float(precio_base_entry.get())

    
    if tipo_iva_var == 1:
        iva = precio_base * 10.5 / 100
    else:
        iva = precio_base * 21 / 100
    
    precio_con_iva = precio_base + iva
    
    iva_entry.delete(1)
    iva_entry.insert(0, f"{iva:.2f}")
    
    precio_con_iva_entry.delete(1)
    precio_con_iva_entry.insert(0, f"{precio_con_iva:.2f}")

# Crear la ventana principal
window = Tk()
window.title("Cálculo de IVA")

# Crear las variables de control
tipo_iva_var = getint()

titulo = ttk.Label(window, text="Cálculo de IVA", background="#c5e2f6")

# Crear los widgets
precio_sin_iva_label = ttk.Label(window, text="Precio sin IVA:", padding=15)
precio_base_entry = ttk.Entry(window)

tipo_iva_checkbox1 = ttk.Radiobutton(window, text="10.5%", variable=tipo_iva_var, value=1)
tipo_iva_checkbox2 = ttk.Radiobutton(window, text="21%", variable=tipo_iva_var, value=2)

iva_label = ttk.Label(window, text="IVA:")
iva_entry = ttk.Entry(window)

precio_con_iva_label = ttk.Label(window, text="Precio con IVA:")
precio_con_iva_entry = ttk.Entry(window)

calcular_button = ttk.Button(window, text="Calcular", command=calcular_iva)
salir_button = ttk.Button(window, text="Salir", command=window.quit)

# Ubicar los widgets en la ventana
titulo.grid(row=0, sticky=NSEW)

precio_sin_iva_label.grid(row=1, column=0, padx=5, pady=5)
precio_base_entry.grid(row=1, column=1, padx=5, pady=5)

tipo_iva_checkbox1.grid(row=2, column=0, pady=5)
tipo_iva_checkbox2.grid(row=3, column=0, pady=5)

iva_label.grid(row=4, column=0, padx=5, pady=5)
iva_entry.grid(row=4, column=1, padx=5, pady=5)

precio_con_iva_label.grid(row=5, column=0, padx=5, pady=5)
precio_con_iva_entry.grid(row=5, column=1, padx=5, pady=5)

calcular_button.grid(row=6, column=0, padx=5, pady=5)
salir_button.grid(row=6, column=1, padx=5, pady=5)

# Ejecutar la aplicación
window.mainloop()
