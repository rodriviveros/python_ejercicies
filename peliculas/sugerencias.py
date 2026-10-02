#Imports
from datetime import date 

#Mostrar Encabezado
def encabezado():
    print("=====================================\n")
    print("      sugerencias de pelìculas       \n")
    print("=====================================\n")

#Mostrar Perfil de usuario del argumento que se le pasa al procedimiento.
def perfil_usuario(usuario):
    print("Perfil de "+usuario["nombre"])
    print("Género favorito: "+usuario["genero_fav"])
    print("Películas Sugeridas:", usuario["vistas"])
    with open("info_usuario.txt", "w") as archivo:
        archivo.write(usuario["nombre"]+"\n")
        archivo.write(usuario["genero_fav"]+"\n")
        archivo.write(str(usuario["vistas"]))

#Funcion para sacar tildes
def sacar_tildes(texto):
    texto=texto.lower()
    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for con_tilde, sin_tilde in reemplazos.items():
        texto = texto.replace(con_tilde, sin_tilde)
    return texto

#Mostrar Lista de generos de películas
def mostrar_generos():
    generos = ["Acción", "Comedia", "Drama", "Animación", "Terror"]
    print("-------- GÉNEROS --------")
    for genero in generos:
        print(genero)

#Datos de peliculas
Peliculas = [
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

#Codigo Principal
def main():
    hoy = date.today()
    print(hoy)
    encabezado()
    usuario=input("Buen dìa, cúal es tu nombre? ")
    print("¿Què quieres ver hoy, "+usuario+"?")
    mostrar_generos()
    genero_favorito=input("¿Que genero te gusta? ")
    rating_minimo=float(input("¿Cúal es tu rating mínimo? "))
    usuario={"nombre":usuario,"genero_fav":genero_favorito,"vistas":[] }
    encontrar_pelicula= False
    print ("Buscando Péliculas del Género: " +genero_favorito)
    for Pelicula in Peliculas:
        if sacar_tildes(Pelicula["genero"])==sacar_tildes(genero_favorito) and Pelicula["rating"]>=rating_minimo:
            print(f'{Pelicula["nombre"]} - {Pelicula["estreno"]} - {Pelicula["rating"]}')
            usuario["vistas"].append(Pelicula["nombre"])
            encontrar_pelicula=True
    if not encontrar_pelicula:
        print("No se ha encontrado ninguna película con ese rating.")
    perfil_usuario(usuario) # usurio es una variable (parámetro) dentro del main. Pasando esa variable al procedimiento perfil_usuario
if __name__ == "__main__":
    main()
