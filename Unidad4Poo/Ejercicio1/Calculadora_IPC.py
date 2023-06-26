#Ejercicio 1 - Unidad 4 - VB
from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion():
    
    __ventana = None
    __vestimenta_cantidad_entry = None
    __vestimenta_PrecioAñoBase_entry = None
    __vestimenta_PrecioAñoActual_entry = None
    __alimentos_cantidad_entry = None
    __alimentos_PrecioAñoBase_entry = None
    __alimentos_PrecioAñoActual_entry = None
    __educacion_cantidad_entry = None
    __educacion_PrecioAñoBase_entry = None
    __educacion_PrecioAñoActual_entry = None

    def __init__(self):
        # Crear la ventana principal
        self.__ventana = Tk()
        self.__ventana.title("Calculadora de IPC")
        
        #Creo la primera fila solo con labels(textos)
        titulo1_label = ttk.Label(self.__ventana, text="Item")
        titulo1_label.grid(row=0, column=0, columnspan=1, pady=10)
        
        titulo2_label = ttk.Label(self.__ventana, text="Cantidad")
        titulo2_label.grid(row=0, column=1, columnspan=1, pady=10)
        
        titulo3_label = ttk.Label(self.__ventana, text="Precio Año Base")
        titulo3_label.grid(row=0, column=2, columnspan=1, pady=10)
        
        titulo4_label = ttk.Label(self.__ventana, text="Precio Año Actual")
        titulo4_label.grid(row=0, column=3, columnspan=1, pady=10)
        
        
        #Creo la primera columna solo con textos
        vestimenta_label = ttk.Label(self.__ventana, text="Vestimenta")
        vestimenta_label.grid(row=1, column=0, padx=15)
        
        alimentos_label = ttk.Label(self.__ventana, text="Alimentos")
        alimentos_label.grid(row=2, column=0, padx=15)
        
        educacion_label = ttk.Label(self.__ventana, text="Educación")
        educacion_label.grid(row=3, column=0, padx=15)
        
        
        #Ahora si creo los inputs con los atributos definidos
        self.__vestimenta_cantidad_entry= ttk.Entry(self.__ventana, width=10, font=1)
        self.__vestimenta_cantidad_entry.grid(row=1, column=1, padx=15, pady=15)
        self.__alimentos_cantidad_entry = ttk.Entry(self.__ventana, width=10, font=1)
        self.__alimentos_cantidad_entry.grid(row=2, column=1, padx=15, pady=15)
        self.__educacion_cantidad_entry= ttk.Entry(self.__ventana, width=10, font=1)
        self.__educacion_cantidad_entry.grid(row=3, column=1, padx=15, pady=15)
        
        self.__vestimenta_PrecioAñoBase_entry = ttk.Entry(self.__ventana, width=10, font=1)
        self.__vestimenta_PrecioAñoBase_entry.grid(row=1, column=2, padx=15)
        self.__alimentos_PrecioAñoBase_entry = ttk.Entry(self.__ventana, width=10, font=1)
        self.__alimentos_PrecioAñoBase_entry.grid(row=2, column=2, padx=15)
        self.__educacion_PrecioAñoBase_entry= ttk.Entry(self.__ventana, width=10, font=1)
        self.__educacion_PrecioAñoBase_entry.grid(row=3, column=2, padx=15)
        
        self.__vestimenta_PrecioAñoActual_entry = ttk.Entry(self.__ventana, width=10, font=1)
        self.__vestimenta_PrecioAñoActual_entry.grid(row=1, column=3, padx=15)
        self.__alimentos_PrecioAñoActual_entry = ttk.Entry(self.__ventana, width=10, font=1)
        self.__alimentos_PrecioAñoActual_entry.grid(row=2, column=3, padx=15)
        self.__educacion_PrecioAñoActual_entry = ttk.Entry(self.__ventana, width=10, font=1)
        self.__educacion_PrecioAñoActual_entry.grid(row=3, column=3, padx=15)
        
        
        #Creo el boton que me permitira hacer el calculo
        calcular_button = ttk.Button(self.__ventana, text="Calcular IPC", command=self.calcular)
        calcular_button.grid(row=4, column=1, pady=10)
        
        salir_button = ttk.Button(self.__ventana, text="Salir", command=self.__ventana.quit)
        salir_button.grid(row=4, column=2, pady=10)
             
        self.__ventana.mainloop() #Inicio el programa
    
    #funcion
    def calcular(self):
        try:
             # Obtener los valores ingresados por el usuario
             vestimenta_cantidad = float(self.__vestimenta_cantidad_entry.get())
             alimentos_cantidad = float(self.__alimentos_cantidad_entry.get())
             educacion_cantidad = float(self.__educacion_cantidad_entry.get())
     
             vestimenta_precio_2022 = float(self.__vestimenta_PrecioAñoBase_entry.get())
             alimentos_precio_2022 = float(self.__alimentos_PrecioAñoBase_entry.get())
             educacion_precio_2022 = float(self.__educacion_PrecioAñoBase_entry.get())
     
             vestimenta_precio_2023 = float(self.__vestimenta_PrecioAñoActual_entry.get())
             alimentos_precio_2023 = float(self.__alimentos_PrecioAñoActual_entry.get())
             educacion_precio_2023 = float(self.__educacion_PrecioAñoActual_entry.get())
     
             # Calcular el costo de la canasta básica para cada año
             costo_2022 = (vestimenta_cantidad * vestimenta_precio_2022) + (alimentos_cantidad * alimentos_precio_2022) + (educacion_cantidad * educacion_precio_2022)
             costo_2023 = (vestimenta_cantidad * vestimenta_precio_2023) + (alimentos_cantidad * alimentos_precio_2023) + (educacion_cantidad * educacion_precio_2023)
     
             # Calcular el IPC
             ipc = int((costo_2023 / costo_2022 - 1) * 100)
     
             # Mostrar el resultado en un mensaje de diálogo
             messagebox.showinfo("Resultado", f"El IPC porcentual es: {ipc}%")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")
        
def testAPP():
   mi_app = Aplicacion()
if __name__ == '__main__':
   testAPP()
