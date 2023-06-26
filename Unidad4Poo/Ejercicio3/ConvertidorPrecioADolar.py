#Ejercicio 3 - Unidad 4 - VB
import requests
import json 
from tkinter import *
import tkinter as ttk
from tkinter import messagebox, font



def obtener_cotizacion_dolar():
    try:
        url = "https://www.dolarsi.com/api/api.php?type=dolar"
        response = requests.get(url)
        data = response.json()
        cotizacion = float(data[0]['casa']['venta'].replace(',', '.'))
        return cotizacion
    except:
        messagebox.showerror("Error", "No se pudo obtener la cotización del dólar.")
        return None

def convertir_a_pesos(event=None):
    try:
        precio_dolares = float(entry_dolares.get())
        cotizacion_dolar = obtener_cotizacion_dolar()
        if cotizacion_dolar is not None:
            precio_pesos = precio_dolares * cotizacion_dolar
            label_resultado.config(text=f" es equivalente a {precio_pesos:.2f} pesos")
    except ValueError:
        label_resultado.config(text="Ingrese un valor válido para el precio en dólares.")

def salir():
    window.destroy()

# Crear la ventana principal
window = Tk()
window.title("Conversor de Precio")

# Crear y posicionar los widgets en la ventana

entry_dolares = ttk.Entry(window)
entry_dolares.pack(side="left")
entry_dolares.configure(width=10, font="Arial")
texto = ttk.Label(window, text="dolares")
texto.pack(side="left")


entry_dolares.bind('<KeyRelease>', convertir_a_pesos)  # Llamar a convertir_a_pesos cuando se suelta una tecla en el Entry

label_resultado = ttk.Label(window, text="")
label_resultado.pack(side="left", pady=15)

btn_salir = ttk.Button(window, text="Salir", command=salir, width=10)
btn_salir.pack(side="bottom", padx=5, pady=5)

# Ejecutar el bucle principal de la aplicación
window.mainloop()
