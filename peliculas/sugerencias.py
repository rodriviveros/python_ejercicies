# Sugerencias de películas
# Le pide al usuario su género favorito y un rating mínimo,
# y le muestra las películas que cumplen con esos criterios.


# ---------------------------------------------------------------
# IMPORTS
# ---------------------------------------------------------------
from datetime import date


# ---------------------------------------------------------------
# FUNCIONES
# ---------------------------------------------------------------
def encabezado():
    # Muestra el título del programa
    print("=====================================\n")
    print("      SUGERENCIAS DE PELÍCULAS       \n")
    print("=====================================\n")


def mostrar_generos():
    # Muestra el menú de géneros disponibles
    generos = ["Acción", "Comedia", "Drama", "Animación", "Terror"]
    print("-------- GÉNEROS --------")
    for genero in generos:
        print(genero)


def perfil_usuario():
    # Muestra el perfil del usuario (usa el diccionario "usuario" del programa principal)
    print(f'PERFIL DE {usuario["nombre"]}')
    print(f'Género Favorito: {usuario["genero_fav"]}')
    print(f'Películas Vistas: {usuario["vistas"]}')

def sacar_tildes(texto):
    # Convierte un texto a minúsculas y reemplaza las vocales con tilde por sus equivalentes sin tilde.
    texto=texto.lower()
    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for con_tilde, sin_tilde in reemplazos.items():
        texto = texto.replace(con_tilde, sin_tilde)
    return texto


# ---------------------------------------------------------------
# DATOS
# ---------------------------------------------------------------
# Cada película es una lista: [nombre, género, estreno, rating]
peliculas = [
    {"nombre": "Rapidos y furiosos", "genero": "Acción", "estreno": 2001, "rating": 6.8},
    {"nombre": "Troya", "genero": "Acción", "estreno": 2004, "rating": 7.3},
    {"nombre": "Terminator 2", "genero": "Acción", "estreno": 1991, "rating": 8.6},
    {"nombre": "¿Y dónde está el piloto?", "genero": "Comedia", "estreno": 1980, "rating": 7.7},
    {"nombre": "¿Què pasò ayer?", "genero": "Comedia", "estreno": 2009, "rating": 7.7},
    {"nombre": "Sherk", "genero": "Comedia", "estreno": 2001, "rating": 7.8},
    {"nombre": "El padrino", "genero": "Drama", "estreno": 1972, "rating": 9.2},
    {"nombre": "El rey león", "genero": "Animación", "estreno": 1994, "rating": 8.5},
    {"nombre": "El Exorcista", "genero": "Terror", "estreno": 1973, "rating": 8.0}
]


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------

# Fecha y encabezado
hoy = date.today()
print(hoy)
encabezado()

# Datos del usuario
usuario = input("Buen día, ¿cuál es tu nombre? ")
print("¿Qué querés ver hoy, " + usuario + "?")

# Preferencias
mostrar_generos()
genero_favorito = input("¿Qué género te gusta? ")
rating_minimo = float(input("¿Cuál es el rating mínimo? "))

# A partir de acá, "usuario" pasa a ser un diccionario con el perfil
usuario = {"nombre": usuario, "genero_fav": genero_favorito, "vistas": []}

# Búsqueda de películas
print("Buscando Películas del Género " + genero_favorito)
encontrar_pelicula = False

for Pelicula in peliculas:
    if sacar_tildes(Pelicula["genero"])==sacar_tildes(genero_favorito) and Pelicula["rating"]>=rating_minimo:
        print(f'{Pelicula["nombre"]} - {Pelicula["estreno"]} - {Pelicula["rating"]}')
        usuario["vistas"].append(Pelicula["nombre"])
        encontrar_pelicula=True
if not encontrar_pelicula:
    print("No se ha encontrado ninguna película.")

# Perfil final
perfil_usuario()