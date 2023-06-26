import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#Ejercicio 5 - Unidad 4 - VB

# Configura tu API key obtenida de themoviedb.org
API_KEY = 'de02ba621ac6c9ffa3f79dae027807bc'

# URL base de la API
BASE_URL = 'https://api.themoviedb.org/3'

# URL para obtener los géneros
GENRES_URL = f'{BASE_URL}/genre/movie/list?api_key={API_KEY}'

# URL para descubrir películas
DISCOVER_URL = f'{BASE_URL}/discover/movie?api_key={API_KEY}'

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title('Cinéfilos Argentinos')
        self.geometry('600x400')

        # Variable para almacenar las películas
        self.movies = []

        # Variable para almacenar los géneros
        self.genres = {}

        # Crear el listbox para mostrar los títulos de las películas
        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.listbox.bind('<Double-Button-1>', self.show_movie_details)

        # Obtener los géneros de la API
        self.get_genres()

        # Obtener las películas de la API
        self.get_movies()

    def get_genres(self):
        try:
            response = requests.get(GENRES_URL)
            response.raise_for_status()
            data = response.json()

            # Almacenar los géneros en un diccionario
            for genre in data['genres']:
                self.genres[genre['id']] = genre['name']
        except requests.RequestException as e:
            messagebox.showerror('Error', f'Error al obtener los géneros: {str(e)}')

    def get_movies(self):
        try:
            response = requests.get(DISCOVER_URL)
            response.raise_for_status()
            data = response.json()

            # Almacenar las películas en la variable de clase
            self.movies = data['results']

            # Mostrar los títulos de las películas en el listbox
            for movie in self.movies:
                self.listbox.insert(tk.END, movie['title'])
        except requests.RequestException as e:
            messagebox.showerror('Error', f'Error al obtener las películas: {str(e)}')

    def show_movie_details(self, event):
        # Obtener el índice de la película seleccionada en el listbox
        index = self.listbox.curselection()
        if index:
            movie = self.movies[index[0]]

            # Crear una ventana emergente para mostrar los detalles de la película
            details_window = tk.Toplevel(self)
            details_window.title(movie['title'])
            details_window.geometry('400x300')

            # Crear etiquetas para los datos de la película
            tk.Label(details_window, text='Resumen:').pack()
            tk.Label(details_window, text=movie['overview']).pack()

            tk.Label(details_window, text='Lenguaje Original:').pack()
            tk.Label(details_window, text=movie['original_language']).pack()

            tk.Label(details_window, text='Fecha de Lanzamiento:').pack()
            tk.Label(details_window, text=movie['release_date']).pack()

            tk.Label(details_window, text='Géneros:').pack()
            genres = [self.genres.get(genre_id, '') for genre_id in movie['genre_ids']]
            tk.Label(details_window, text=', '.join(genres)).pack()


if __name__ == '__main__':
    app = Application()
    app.mainloop()
